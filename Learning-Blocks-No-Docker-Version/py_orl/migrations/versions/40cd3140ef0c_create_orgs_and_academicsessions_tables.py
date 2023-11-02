"""Create orgs and academicsessions tables

Revision ID: 40cd3140ef0c
Revises: 
Create Date: 2023-10-29 07:02:00.833479

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '40cd3140ef0c'
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
    op.create_table(
        'academicsessions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('sourcedId', sa.String, nullable=False),
        sa.Column('status', sa.Enum('active', 'tobedeleted', 'inactive', name='enum1'), nullable=False),
        sa.Column('dateLastModified', sa.DateTime),
        sa.Column('title', sa.String(50)),
        sa.Column('type', sa.Enum('gradingPeriod', 'semester', 'schoolYear', 'term', name='enum2'),
                  nullable=False),
        sa.Column('startDate', sa.DateTime),
        sa.Column('endDate', sa.DateTime),
        sa.Column('parentSourcedId', sa.String(256), primary_key=True, unique=True, nullable=False),
    )

    def downgrade():
        op.drop_table('orgs')
        op.drop_table('academicsessions')
