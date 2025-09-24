"""add facilities

Revision ID: 0d9ff8a0d92c
Revises: 85efe50826b0
Create Date: 2024-12-14 17:06:05.013981

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "0d9ff8a0d92c"
down_revision: Union[str, None] = "85efe50826b0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "facilities",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=25), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "facilities_rooms",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("room_id", sa.Integer(), nullable=False),
        sa.Column("facility_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["facility_id"],
            ["facilities.id"],
        ),
        sa.ForeignKeyConstraint(
            ["room_id"],
            ["rooms.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("facilities_rooms")
    op.drop_table("facilities")
