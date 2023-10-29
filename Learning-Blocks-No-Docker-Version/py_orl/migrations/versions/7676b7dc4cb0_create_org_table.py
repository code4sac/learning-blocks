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
        'orgs',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('sourcedId', sa.String(36), unique=True, nullable=False),
        sa.Column('status', sa.Enum('active', 'tobedeleted', 'inactive', name='enum1'), nullable=False),
        sa.Column('dateLastModified', sa.DateTime, nullable=False),
        sa.Column('name', sa.String(36), nullable=False),
        sa.Column('type', sa.Enum('department', 'school', 'district', 'local', 'state', 'national', name='enum_type'),
                  nullable=False),
        sa.Column('identifier', sa.String, nullable=True),
        sa.Column('parentSourcedId', sa.String(36), nullable=False),
        sa.Column('national', sa.Boolean, default=False),
        sa.Column('state', sa.Boolean, default=False),
        sa.Column('local', sa.Boolean, default=False),
        sa.Column('district', sa.Boolean, default=False),
        sa.Column('school', sa.Boolean, default=False),
    )
    # op.create_table(
    #     'academicsession',
    #     sa.Column('id', sa.Integer, primary_key=True),
    #     sa.Column('sourcedId', sa.String, nullable=False),
    #     sa.Column('name', sa.String(50), nullable=False),
    # )


def downgrade():
    op.drop_table('orgs')
    # op.drop_table('academicsession')
    op.drop_index(op.f("enum1"), table_name="orgs")
