"""empty message

Revision ID: cb18f79c0a9e
Revises: 
Create Date: 2024-03-21 13:42:37.005946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb18f79c0a9e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(), nullable=False),
    sa.Column('event_num', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_event_table'))
    )
    op.create_table('fighter_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_fighter_table'))
    )
    op.create_table('user_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user_table')),
    sa.UniqueConstraint('name', name=op.f('uq_user_table_name'))
    )
    op.create_table('match_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('fighter1_id', sa.Integer(), nullable=True),
    sa.Column('fighter2_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['event_table.id'], name=op.f('fk_match_table_event_id_event_table')),
    sa.ForeignKeyConstraint(['fighter1_id'], ['fighter_table.id'], name=op.f('fk_match_table_fighter1_id_fighter_table')),
    sa.ForeignKeyConstraint(['fighter2_id'], ['fighter_table.id'], name=op.f('fk_match_table_fighter2_id_fighter_table')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_match_table'))
    )
    op.create_table('comment_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('review', sa.String(), nullable=True),
    sa.Column('reviewer_id', sa.Integer(), nullable=True),
    sa.Column('match_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['match_id'], ['match_table.id'], name=op.f('fk_comment_table_match_id_match_table')),
    sa.ForeignKeyConstraint(['reviewer_id'], ['user_table.id'], name=op.f('fk_comment_table_reviewer_id_user_table')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_comment_table'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment_table')
    op.drop_table('match_table')
    op.drop_table('user_table')
    op.drop_table('fighter_table')
    op.drop_table('event_table')
    # ### end Alembic commands ###