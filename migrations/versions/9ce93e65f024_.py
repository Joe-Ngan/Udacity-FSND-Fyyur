"""empty message

Revision ID: 9ce93e65f024
Revises: b7496ce6a4f2
Create Date: 2021-11-24 09:50:45.476136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ce93e65f024'
down_revision = 'b7496ce6a4f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('past_shows_count', sa.Integer(), nullable=True))
    op.add_column('venue', sa.Column('upcoming_shows_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'upcoming_shows_count')
    op.drop_column('venue', 'past_shows_count')
    # ### end Alembic commands ###
