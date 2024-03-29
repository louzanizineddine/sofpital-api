"""Enums causing trouble removing them

Revision ID: 26c5608cabbf
Revises: 4718d3bfed37
Create Date: 2024-01-21 00:57:56.142800

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '26c5608cabbf'
down_revision = '4718d3bfed37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('learner', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('tutor', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=postgresql.ENUM('MALE', 'FEMALE', name='gender'),
               type_=sa.String(length=6),
               existing_nullable=True)
        batch_op.alter_column('role',
               existing_type=postgresql.ENUM('LEARNER', 'TUTOR', name='role'),
               type_=sa.String(length=10),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('role',
               existing_type=sa.String(length=10),
               type_=postgresql.ENUM('LEARNER', 'TUTOR', name='role'),
               existing_nullable=False)
        batch_op.alter_column('gender',
               existing_type=sa.String(length=6),
               type_=postgresql.ENUM('MALE', 'FEMALE', name='gender'),
               existing_nullable=True)

    with op.batch_alter_table('tutor', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('learner', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
