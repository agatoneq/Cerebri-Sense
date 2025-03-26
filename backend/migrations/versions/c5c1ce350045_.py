"""empty message

Revision ID: c5c1ce350045
Revises: 33b223c2068b
Create Date: 2025-01-10 14:52:31.014759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5c1ce350045'
down_revision = '33b223c2068b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('analysis_results')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('analysis_results',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('file_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('probability', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('classification', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['file_id'], ['processed_files.id'], name='analysis_results_file_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='analysis_results_pkey')
    )
    # ### end Alembic commands ###
