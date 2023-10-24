"""Create org table

Revision ID: 7676b7dc4cb0
Revises: 
Create Date: 2023-10-24 14:02:47.276128

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '7676b7dc4cb0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'org',
        sa.Column('source_id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table('org')
