"""add test and dev environments

Revision ID: 154a816cd25d
Revises: 61a0ccda0bde
Create Date: 2020-11-13 15:54:30.078771

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '154a816cd25d'
down_revision = '61a0ccda0bde'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('letters', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_letters_email'), 'letters', ['email'], unique=False)
    op.create_index(op.f('ix_letters_timestamp'), 'letters', ['timestamp'], unique=False)
    op.create_index(op.f('ix_subscribers_email'), 'subscribers', ['email'], unique=True)
    op.drop_index('email', table_name='subscribers')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('email', 'subscribers', ['email'], unique=True)
    op.drop_index(op.f('ix_subscribers_email'), table_name='subscribers')
    op.drop_index(op.f('ix_letters_timestamp'), table_name='letters')
    op.drop_index(op.f('ix_letters_email'), table_name='letters')
    op.drop_column('letters', 'timestamp')
    # ### end Alembic commands ###
