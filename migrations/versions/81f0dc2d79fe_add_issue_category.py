"""add issue category

Revision ID: 81f0dc2d79fe
Revises: 7f4645ea94a6
Create Date: 2022-06-21 16:14:48.788224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "81f0dc2d79fe"
down_revision = "7f4645ea94a6"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("issue_type", sa.Column("category", sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("issue_type", "category")
    # ### end Alembic commands ###
