"""add foreign key to posts table

Revision ID: 0e7b63a19f14
Revises: b8d411f05160
Create Date: 2022-04-14 23:35:32.699456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e7b63a19f14'
down_revision = 'b8d411f05160'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", 
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_column('posts','owner_id')
    op.drop_constraint('posts_users_fk', 'posts')
    pass
