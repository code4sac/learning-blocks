"""Create org table

Revision ID: e58158fe1665
Revises: 73278caf16bb
Create Date: 2023-10-21 15:35:41.533330

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'e58158fe1665'
down_revision: Union[str, None] = '73278caf16bb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'orgs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table('orgs')
