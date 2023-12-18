#!/usr/bin/env python3
import click
from models import Client, session, CleaningTask, ClientTask
import re
from rich.table import Table, Column
from rich.console import Console


@click.group()
@click.version_option(version="1.0", prog_name="Clean Slate CLI")
def welcome():
    """ Welcome to Clean Slate.\n
        To sign-in use the sign-in command\n
        ie. lib/script sign-in
    """
    welcome_message = """
======================================================================================
    Welcome to 🧼Clean Slate Services🧼
    Hello Client 😁,
    Thank you for choosing Clean Slate. 
    Explore our services, schedule cleanings, and connect with your dedicated cleaner. 
    We're here to assist and provide a seamless experience. 
    Welcome!
    Best regards,
    The Cleaning Managing Team
======================================================================================
"""
    click.secho((welcome_message), fg="yellow", bold=True)


def home_page(current_user):
    # fetch all tasks
    cleaning_tasks = session.query(CleaningTask).all()
    # click.echo(cleaning_tasks)

    console = Console()

    table = Table(show_header=True, header_style="bold cyan")

    table.add_column("task_id", style='bold')
    table.add_column("task_description", style='bold')
    table.add_column("price", style='bold')
    table.add_column("cleaner", style='bold')

    # fill table with fetched tasks
    for item in cleaning_tasks:
        table.add_row(str(item.task_id), item.task_description,
                      str(item.price), item.cleaner.full_name)

    console.print(
        f"Hello {current_user.client_name} 👋👋👋.\nHere are the variety of services we offer. Enter a task id to choose and book a cleaning session with us", style="blue")
    console.print(table)
    client_input = click.prompt("Please select task id", type=int)
    if client_input in range(1, (cleaning_tasks[-1].task_id + 1)):
        client_task = ClientTask(
            client_id=current_user.id,
            task_id=client_input
        )
        session.add(client_task)
        session.commit()

        for task in cleaning_tasks:
            if task.task_id == client_input:
                console.print(
                    f"{task.task_description} service has been booked successfully!! {task.cleaner.full_name} will arrive at your premises in the next hour. Thank you for choosing clean slate😁", style="green")

    else:
        console.print(
            "Invalid task choice, please select a valid task id", style="bold red")
        home_page(current_user)


@welcome.command()
@click.option('--email', '-e', prompt="Enter your email")
@click.option('--password', '-p', prompt="Enter your password", hide_input=True)
def sign_in(email, password):
    """Log in using name and password"""
    user = session.query(Client).filter_by(
        email=email, password=password).first()

    if user:
        click.secho(("Login successful"), fg="green")
        home_page(user)
    else:
        click.secho(("Login failed"), fg="red")


@welcome.command()
@click.option('--name', prompt=True)
@click.option('--email', prompt=True)
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
@click.option('--contact_number', prompt=True)
def sign_up(name, email, password, contact_number):
    """Create a new account"""
    # email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    reg = re.compile(pattern)
    valid_email = reg.fullmatch(email)
    # seeding new user to database
    if valid_email:
        client = Client(
            client_name=name,
            email=email,
            password=password,
            contact_number=contact_number
        )
        session.add(client)
        session.commit()
        click.secho(("Account has been created successfuly"), fg="green")
        home_page(client)
    else:
        click.secho(("Invalid email address.Please try again.."), fg="red")


if __name__ == '__main__':
    welcome()
