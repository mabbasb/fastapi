"""Add camera_id column

Revision ID: 86c872dd5f3b
Revises: 17a9b29fb135
Create Date: 2022-05-24 16:12:30.650907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86c872dd5f3b'
down_revision = '17a9b29fb135'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('waste_water_monitoring', sa.Column('camera_id', sa.Integer(), nullable=False))
    pass


def downgrade():
    op.drop_column('waste_water_monitoring', 'camera_id')
    pass
