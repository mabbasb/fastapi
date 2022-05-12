"""Create test table

Revision ID: a1d76e6c4eeb
Revises: 91db9e5ec45f
Create Date: 2022-05-12 15:41:34.036047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
def upgrade():
    op.create_table('Test',
    sa.Column('id', sa.Integer(), nullable=False), 
    sa.Column('humidity', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'))
    pass


def downgrade():
    op.drop_table('Test')
    pass
