"""empty message

Revision ID: a2b10f5c6f41
Revises: ca9ad5a58665
Create Date: 2023-05-06 09:51:11.778792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2b10f5c6f41'
down_revision = 'ca9ad5a58665'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'category', 'user', ['owner_id'], ['id'])
    op.add_column('permissions', sa.Column('user_id', sa.Integer(), nullable=False))
    op.add_column('permissions', sa.Column('category_id', sa.Integer(), nullable=False))
    op.add_column('permissions', sa.Column('level', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'permissions', 'category', ['category_id'], ['id'])
    op.create_foreign_key(None, 'permissions', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'permissions', type_='foreignkey')
    op.drop_constraint(None, 'permissions', type_='foreignkey')
    op.drop_column('permissions', 'level')
    op.drop_column('permissions', 'category_id')
    op.drop_column('permissions', 'user_id')
    op.drop_constraint(None, 'category', type_='foreignkey')
    op.drop_column('category', 'owner_id')
    # ### end Alembic commands ###
