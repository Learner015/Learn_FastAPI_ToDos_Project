"""Create Phone Number for user column

Revision ID: 8539dec59c56
Revises: 
Create Date: 2026-01-28 10:22:16.237012

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from models import users_a


# revision identifiers, used by Alembic.
revision: str = '8539dec59c56'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users_a',sa.Column('phone_number',sa.String(),nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users_a','phone_number')
