"""first migrate after redo

Revision ID: c72cd39d08a4
Revises: 
Create Date: 2020-09-16 14:55:35.827157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c72cd39d08a4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first', sa.String(), nullable=True),
    sa.Column('last', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('promo_code', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Users')
    # ### end Alembic commands ###
