"""Added ClientTask model

Revision ID: 62099e343240
Revises: a911309cbfe7
Create Date: 2023-12-12 14:12:19.024853

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '62099e343240'
down_revision: Union[str, None] = 'a911309cbfe7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client_tasks',
    sa.Column('client_task_id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['clients.client_id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['cleaning_tasks.task_id'], ),
    sa.PrimaryKeyConstraint('client_task_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('client_tasks')
    # ### end Alembic commands ###
