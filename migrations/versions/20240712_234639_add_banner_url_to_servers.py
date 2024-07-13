"""add banner url to servers

Revision ID: 117acc303990
Revises: e603c554ed14
Create Date: 2024-07-12 23:46:39.908774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '117acc303990'
down_revision = 'e603c554ed14'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('servers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('banner_url', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('servers', schema=None) as batch_op:
        batch_op.drop_column('banner_url')

    # ### end Alembic commands ###