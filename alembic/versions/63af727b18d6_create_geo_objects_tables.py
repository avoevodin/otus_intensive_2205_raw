"""create geo objects tables

Revision ID: 63af727b18d6
Revises: 
Create Date: 2022-05-27 16:59:26.241990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "63af727b18d6"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "countries",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("yandex_code", sa.String(), nullable=False),
        sa.Column("title", sa.String(), server_default="", nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("yandex_code"),
    )
    op.create_table(
        "regions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("yandex_code", sa.String(), nullable=False),
        sa.Column("title", sa.String(), server_default="", nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("country_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["country_id"],
            ["countries.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("yandex_code"),
    )
    op.create_table(
        "settlements",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("yandex_code", sa.String(), nullable=False),
        sa.Column("title", sa.String(), server_default="", nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("region_id", sa.Integer(), nullable=True),
        sa.Column("country_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["country_id"],
            ["countries.id"],
        ),
        sa.ForeignKeyConstraint(
            ["region_id"],
            ["regions.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("yandex_code"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("settlements")
    op.drop_table("regions")
    op.drop_table("countries")
    # ### end Alembic commands ###
