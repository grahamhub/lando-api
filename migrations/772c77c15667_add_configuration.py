"""add_configuration

Revision ID: 772c77c15667
Revises: 0bf5ff89b7fd
Create Date: 2021-04-20 12:58:25.640285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "772c77c15667"
down_revision = "0bf5ff89b7fd"
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "configuration_variable",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("key", sa.String(), nullable=True),
        sa.Column("raw_value", sa.String(length=254), nullable=True),
        sa.Column(
            "variable_type",
            sa.Enum("BOOL", "INT", "STR", name="variabletype"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("key"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("configuration_variable")
    # ### end Alembic commands ###
