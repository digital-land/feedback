"""add organisation

Revision ID: 882a26822214
Revises:
Create Date: 2022-06-13 15:39:47.907997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "882a26822214"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "organisation",
        sa.Column("organisation", sa.Text(), nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("organisation"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("organisation")
    # ### end Alembic commands ###