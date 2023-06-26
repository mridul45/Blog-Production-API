"""add content column to post table

Revision ID: 929eb15b3ddb
Revises: 198246612835
Create Date: 2023-06-26 23:03:38.372592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '929eb15b3ddb'
down_revision = '198246612835'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String,nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
