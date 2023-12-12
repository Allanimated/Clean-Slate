"""Changed CleningTask model table name

Revision ID: a911309cbfe7
Revises: 88f59f1e7abc
Create Date: 2023-12-12 13:26:50.104289

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a911309cbfe7'
down_revision: Union[str, None] = '88f59f1e7abc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table('claening_tasks', 'cleaning_tasks')


def downgrade() -> None:
    op.rename_table('cleaning_tasks', 'claening_tasks')
