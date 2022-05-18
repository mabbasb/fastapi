"""add columns for waste water

Revision ID: 3b335def241d
Revises: 17a9b29fb135
Create Date: 2022-05-18 19:10:00.997059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b335def241d'
down_revision = '17a9b29fb135'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('waste_water_monitoring', sa.Column('id', sa.Integer(), nullable=False), primary_key = True)
    op.add_column('waste_water_monitoring', sa.Column('water_status', sa.Integer(), nullable=False))
    op.add_column('waste_water_monitoring', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default= sa.text('now()'), nullable=False))
    pass


def downgrade():
    op.drop_column('waste_water_monitoring', 'id')
    op.drop_column('waste_water_monitoring', 'water_status')
    op.drop_column('waste_water_monitoring', 'created_at')
    pass
