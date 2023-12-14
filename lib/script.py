#!/usr/bin/env python3
import click
from models import Client, session
import re


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


def Homepage():
    pass


@welcome.command()
@click.option('--email', '-e', prompt="Enter your email")
@click.option('--password', '-p', prompt="Enter your password")
def sign_in(email, password):
    """Log in using name and password"""
    user = session.query(Client).filter_by(
        email=email, password=password).first()

    if user:
        click.secho(("Login successful"), fg="green")
    else:
        click.secho(("Login failed"), fg="red")


@welcome.command()
@click.option('--name', prompt=True)
@click.option('--email', prompt=True)
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
@click.option('--contact_number', prompt=True)
def sign_up(name, email, password, contact_number):
    """Create a new account"""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    reg = re.compile(pattern)
    valid_email = reg.fullmatch(email)
    if valid_email:
        client = Client(
            client_name=name,
            email=email,
            password=password,
            contact_number=contact_number
        )
        session.add(client)
        session.commit()
        session.close()
        click.secho(("Account has been created successfuly"), fg="green")

    else:
        click.secho(("Invalid email address.Please try again.."), fg="red")


if __name__ == '__main__':
    welcome()


# login and signup of clients
# import the Client model call => Client
# def signup
# def login
# def welcome L S
