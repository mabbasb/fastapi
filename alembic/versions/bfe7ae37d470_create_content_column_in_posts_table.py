"""create content column in posts table

Revision ID: bfe7ae37d470
Revises: 30147ed5c95e
Create Date: 2022-04-14 23:13:08.208248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfe7ae37d470'
down_revision = '30147ed5c95e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
