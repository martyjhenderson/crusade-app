"""orderofbattle

Revision ID: 5ade169d042b
Revises: 053e7a93b05d
Create Date: 2020-09-05 23:05:42.010517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ade169d042b'
down_revision = '053e7a93b05d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order_of_battle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('player', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['player'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_of_battle')
    # ### end Alembic commands ###