"""empty message

Revision ID: 30f06b91d56f
Revises: 0fdf971f53d8
Create Date: 2021-11-24 12:46:26.366867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30f06b91d56f'
down_revision = '0fdf971f53d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('artist', 'upcoming_shows')
    op.drop_column('artist', 'past_shows')
    op.drop_column('venue', 'upcoming_shows')
    op.drop_column('venue', 'past_shows')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('past_shows', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('venue', sa.Column('upcoming_shows', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('artist', sa.Column('past_shows', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('artist', sa.Column('upcoming_shows', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_table('show')
    # ### end Alembic commands ###
