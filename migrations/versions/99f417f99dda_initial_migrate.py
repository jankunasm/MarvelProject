"""Initial Migrate.

Revision ID: 99f417f99dda
Revises: 
Create Date: 2021-11-13 20:07:29.407161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99f417f99dda'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.Column('last_name', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('g_auth_verify', sa.Boolean(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('character',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('comics_appeared_in', sa.String(length=100), nullable=True),
    sa.Column('super_power', sa.String(length=100), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('owner', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['owner'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('character')
    op.drop_table('user')
    # ### end Alembic commands ###
