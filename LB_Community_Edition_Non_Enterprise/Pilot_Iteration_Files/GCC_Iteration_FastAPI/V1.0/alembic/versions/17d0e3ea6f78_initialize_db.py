"""initialize_db

Revision ID: 17d0e3ea6f78
Revises: 
Create Date: 2024-09-02 04:03:14.261773

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '17d0e3ea6f78'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Create the schools table with PascalCase column names
    op.create_table(
        'schools',
        sa.Column('ID', sa.Integer, primary_key=True, index=True),
        sa.Column('SchoolCode', sa.String, unique=True, nullable=False),
        sa.Column('SchoolName', sa.String, nullable=False),
        sa.Column('Address', sa.String, nullable=True),
        sa.Column('City', sa.String, nullable=True),
        sa.Column('State', sa.String, nullable=True),
        sa.Column('ZipCode', sa.String, nullable=True),
        sa.Column('MetaData', postgresql.JSONB, nullable=True)
    )

    # Create the people table (with polymorphism)
    op.create_table(
        'people',
        sa.Column('ID', sa.Integer, primary_key=True, index=True),
        sa.Column('FirstName', sa.String, index=True),
        sa.Column('LastName', sa.String, index=True),
        sa.Column('Role', sa.Enum('administrator', 'aide', 'guardian', 'parent', 'proctor', 'relative', 'student', 'teacher', name='roleenum'), nullable=False, index=True),
        sa.Column('SourcedID', sa.String, unique=True, nullable=False, index=True),
        sa.Column('EnabledUser', sa.String, index=True),
        sa.Column('DateLastModified', sa.String, index=True),
        sa.Column('SchoolCode', sa.String, sa.ForeignKey('schools.SchoolCode'), nullable=True, index=True),
        sa.Column('AnonymizedStudentID', sa.String, nullable=True),
        sa.Column('AnonymizedTeacherID', sa.String, unique=True, nullable=True)
    )

    # Create the students table
    op.create_table(
        'students',
        sa.Column('ID', sa.Integer, sa.ForeignKey('people.ID'), primary_key=True, index=True),
        sa.Column('AnonymizedStudentID', sa.String, unique=True, nullable=False),
        sa.Column('AnonymizedStudentNumber', sa.String, nullable=True),
        sa.Column('MetaData', postgresql.JSONB, nullable=True),  # Updated to MetaData
        sa.Column('Sections', sa.String, nullable=True),
        sa.Column('SchlAssociated', sa.String, nullable=True),
        sa.Column('Birthdate', sa.String, nullable=True),  # Added birthdate field
        sa.Column('GradeLevels', sa.String, nullable=True)  # Added GradeLevels field
    )

    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('ID', sa.Integer, sa.ForeignKey('people.ID'), primary_key=True, index=True),
        sa.Column('AnonymizedTeacherID', sa.String, unique=True, nullable=False),
        sa.Column('Sections', sa.String, nullable=True),
        sa.Column('StuAssociated', postgresql.JSONB, nullable=True),
        sa.Column('SchlAssociated', sa.String, nullable=True),
        sa.Column('Credentials', sa.String, nullable=True),
        sa.Column('Subjects', sa.String, nullable=True),
        sa.Column('SiteDuties', sa.String, nullable=True),
        sa.Column('GradeLevels', sa.String, nullable=True),
        sa.Column('MetaData', postgresql.JSONB, nullable=True)
    )

def downgrade() -> None:
    # Drop the teachers table
    op.drop_table('teachers')

    # Drop the students table
    op.drop_table('students')

    # Drop the people table
    op.drop_table('people')

    # Drop the schools table
    op.drop_table('schools')
