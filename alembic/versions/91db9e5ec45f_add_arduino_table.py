"""add Arduino table

Revision ID: 91db9e5ec45f
Revises: 17985e22a455
Create Date: 2022-04-28 12:23:43.219222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91db9e5ec45f'
down_revision = '17985e22a455'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('ArduinoClient1',
    sa.Column('id', sa.Integer(), nullable=False), 
    sa.Column('humidity', sa.Integer(), nullable=False),
    sa.Column('temperature', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'))
    pass


def downgrade():
    op.drop_table('ArduinoClient1')
    pass
