"""re add waste water table

Revision ID: 6a0f7f1c9aa1
Revises: 3b335def241d
Create Date: 2022-05-18 19:37:01.790470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a0f7f1c9aa1'
down_revision = '3b335def241d'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('waste_water_monitoring')
    op.create_table('waste_water_monitoring',
    sa.Column('id', sa.Integer(), nullable=False), 
    sa.Column('water_status', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default= sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'))
    pass


def downgrade():
    op.drop_table('waste_water_monitoring')
    pass
