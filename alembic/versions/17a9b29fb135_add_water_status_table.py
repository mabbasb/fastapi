"""add water status table

Revision ID: 17a9b29fb135
Revises: 761e1c0f64f9
Create Date: 2022-05-18 18:48:03.910559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17a9b29fb135'
down_revision = '761e1c0f64f9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('waste_water_monitoring'), 
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('water_status', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default= sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    pass


def downgrade():
    op.drop_table('waste_water_monitoring')
    pass
