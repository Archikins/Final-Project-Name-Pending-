"""empty message

Revision ID: a1f86a733264
Revises: 578165493c78
Create Date: 2022-09-26 16:47:07.014026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1f86a733264'
down_revision = '578165493c78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'daily_plan', ['id'])
    op.create_unique_constraint(None, 'meal', ['id'])
    op.create_unique_constraint(None, 'user', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'meal', type_='unique')
    op.drop_constraint(None, 'daily_plan', type_='unique')
    # ### end Alembic commands ###
