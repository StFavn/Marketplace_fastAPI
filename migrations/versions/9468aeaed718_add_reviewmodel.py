"""Add ReviewModel

Revision ID: 9468aeaed718
Revises: bf5faf1a7f51
Create Date: 2024-06-12 20:37:14.736052

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9468aeaed718'
down_revision: Union[str, None] = 'bf5faf1a7f51'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('when', sa.DateTime(timezone=True), nullable=False),
    sa.Column('positive_msg', sa.String(length=100), nullable=True),
    sa.Column('negative_msg', sa.String(length=100), nullable=True),
    sa.Column('verdict_msg', sa.String(length=1000), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('goods_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['goods_id'], ['goods.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    # ### end Alembic commands ###
