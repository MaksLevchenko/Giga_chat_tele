"""Add style

Revision ID: a8de2840102f
Revises: c5ed28d44de5
Create Date: 2025-05-04 10:46:45.925008

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a8de2840102f'
down_revision: Union[str, None] = 'c5ed28d44de5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('conversation_history', sa.Column('style', sa.String(), server_default='Обычном', nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('conversation_history', 'style')
    # ### end Alembic commands ###
