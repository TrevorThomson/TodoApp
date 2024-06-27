"""rename database file

Revision ID: 93ce0439a3e3
Revises: 649a5f7ff4ef
Create Date: 2024-06-27 15:13:15.470291

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93ce0439a3e3'
down_revision: Union[str, None] = '649a5f7ff4ef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# NOTE: We erroneously added a new revision to try and recreate the db with a new name.
#       we should look in to deleting this revision from alembic

def upgrade() -> None:
    pass

def downgrade() -> None:
    pass

