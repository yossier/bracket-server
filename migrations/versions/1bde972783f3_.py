"""empty message

Revision ID: 1bde972783f3
Revises: 3df8e30ac52e
Create Date: 2015-12-09 19:29:33.847135

"""

# revision identifiers, used by Alembic.
revision = '1bde972783f3'
down_revision = '3df8e30ac52e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('score', sa.Column('completed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('score', 'completed')
    ### end Alembic commands ###
