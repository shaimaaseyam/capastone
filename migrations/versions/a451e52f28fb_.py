"""empty message

Revision ID: a451e52f28fb
Revises: 
Create Date: 2020-08-21 20:10:41.493746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a451e52f28fb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets ')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets ',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"planets _id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('moons_numbers', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='planets _pkey')
    )
    # ### end Alembic commands ###
