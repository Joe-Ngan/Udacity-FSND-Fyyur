"""empty message

Revision ID: 27c736095c20
Revises: 30f06b91d56f
Create Date: 2021-11-24 16:45:18.065850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27c736095c20'
down_revision = '30f06b91d56f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artist', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_unique_constraint(None, 'artist', ['name'])
    op.alter_column('show', 'start_time',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('venue', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_unique_constraint(None, 'venue', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'venue', type_='unique')
    op.alter_column('venue', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('show', 'start_time',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.drop_constraint(None, 'artist', type_='unique')
    op.alter_column('artist', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###