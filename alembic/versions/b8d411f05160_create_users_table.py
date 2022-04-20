"""create users table

Revision ID: b8d411f05160
Revises: bfe7ae37d470
Create Date: 2022-04-14 23:22:38.612304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8d411f05160'
down_revision = 'bfe7ae37d470'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default= sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
