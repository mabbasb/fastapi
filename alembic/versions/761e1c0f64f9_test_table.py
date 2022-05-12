"""test table

Revision ID: 761e1c0f64f9
Revises: a1d76e6c4eeb
Create Date: 2022-05-12 16:00:08.513623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '761e1c0f64f9'
down_revision = 'a1d76e6c4eeb'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('Test')
    op.create_table('test',
    sa.Column('id', sa.Integer(), nullable=False), 
    sa.Column('humidity', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'))
    pass


def downgrade():
    op.drop_table('test')
    pass
