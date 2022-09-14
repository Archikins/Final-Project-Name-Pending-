"""empty message

Revision ID: 8204b055e325
Revises: ff9ee75d5218
Create Date: 2022-09-14 20:35:27.131577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8204b055e325'
down_revision = 'ff9ee75d5218'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('first_block',
    sa.Column('daily_plan_id', sa.Integer(), nullable=True),
    sa.Column('meal_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['daily_plan_id'], ['daily_plan.id'], ),
    sa.ForeignKeyConstraint(['meal_id'], ['meal.id'], )
    )
    op.create_table('second_block',
    sa.Column('daily_plan_id', sa.Integer(), nullable=True),
    sa.Column('meal_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['daily_plan_id'], ['daily_plan.id'], ),
    sa.ForeignKeyConstraint(['meal_id'], ['meal.id'], )
    )
    op.create_table('third_block',
    sa.Column('daily_plan_id', sa.Integer(), nullable=True),
    sa.Column('meal_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['daily_plan_id'], ['daily_plan.id'], ),
    sa.ForeignKeyConstraint(['meal_id'], ['meal.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('third_block')
    op.drop_table('second_block')
    op.drop_table('first_block')
    # ### end Alembic commands ###
