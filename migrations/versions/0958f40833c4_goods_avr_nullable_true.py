"""goods.avr nullable=true

Revision ID: 0958f40833c4
Revises: abeb37f2adf6
Create Date: 2024-06-11 00:13:27.983204

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0958f40833c4'
down_revision: Union[str, None] = 'abeb37f2adf6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('goods', 'average_rating',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('goods', 'average_rating',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=False)
    # ### end Alembic commands ###
