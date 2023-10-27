# Database Documentation for Learning Blocks

## Database setup

### Install PostgreSQL

Install PostgreSQL database with your operating system's preferred method.

#### Linux (Linux Mint)

```shell
sudo apt install postgresql postgresql-contrib
```

### Connect to PostgreSQL

Check if the database is running.

```shell
sudo systemctl status postgresql 
sudo pg_isready
```

Use [psql](https://www.postgresql.org/docs/current/app-psql.html) to enter SQL queries in Postgres. The following
command shows how to login as the postgres user and enter/exit the `psql` command.

```shell
sudo -i -u postgres
psql
\q 
```

### Create an application admin database user

Connect to the database as the postgres user. Enter the following commands in `psql` create a database and user with
admin access.

```postgresql
create user admin;
create database app;
alter user admin with encrypted password 'change-me-password-8943ryhiu';
grant all privileges on database app to admin; 
```

You can alternatively run the following commands on the command line.

```shell
createuser admin 
createdb app 
```

## Database development

### Configure the database credentials

While we develop a way to read credentials from an `.env` file, we need a way to load environment variables used
by [pydantic-settings](https://github.com/pydantic/pydantic-settings). This can be achieved for now by adding
environment variables to your system path.

#### Linux (Linux Mint)

Add the following exports to your `.bashrc` or `.zshrc` file.

> Make sure to reload your terminal after saving for the changes to take effect.

```env
domain=localhost
project_name="Learning Blocks"
postgres_server=localhost
postgres_user=admin
postgres_password=change-me-password-8943ryhiu
postgres_db=app
pgadmin_listen_port=5050
pgadmin_default_email=my-email@gmail.com
pgadmin_default_password=change-me-password-8943ryhiu
```

#### Windows

Add an environment variable on Windows with
the [set command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/set_1) or use the
graphical dialog.

### Initialize data in the database

When you first run the application, run `alembic upgrade head` and then populate the database
with [initial_data.py](initial_data.py). These steps can be found in [prestart.sh](prestart.sh).

### Alembic migrations

#### Initialize Alembic

Initialize Alembic in the migrations folder. `alembic.ini` is also generated.

```shell
alembic init migrations
```

#### Create initial migration

Create an initial migration that adds the first table to the database.

```shell
alembic revision -m "Create item table"
```

**migrations/versions/7676b7dc4cb0_create_org_table.py**

```python
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
```

### Populate database data

Run the [initial_data.py](initial_data.py) Python script.

> Make sure to run an Alembic migration first to create the table and columns.

```shell
python initial_data.py
```

### Create a model

To create a model, create a Python file in the models folder.

**models/item.py**

```python
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base


class Item(Base):
    id: int = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner: "User" = relationship("User", back_populates="items")
```

### Create a schema

To create a schema, create a Python file in the schemas folder.

**schemas/item.py**

```python
from pydantic import BaseModel


# Shared properties
class ItemBase(BaseModel):
    title: str | None
    description: str | None


# Properties to receive on item creation
class ItemCreate(ItemBase):
    title: str


# Properties to receive on item update
class ItemUpdate(ItemBase):
    pass


# Properties shared by models stored in DB
class ItemInDBBase(ItemBase):
    id: int
    title: str
    owner_id: int

    class Config:
        from_attributes = True


# Properties to return to client
class Item(ItemInDBBase):
    pass


# Properties properties stored in DB
class ItemInDB(ItemInDBBase):
    pass
```

### Create a CRUD (Create, Readm Update, and Delete) operation

CRUD objects are used to access the database from the application code. To create a CRUD operation, add a file to the
crud folder.

**crud/crud_item.py**

```python
from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.item import Item
from schemas.item import ItemCreate, ItemUpdate


class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):
    def create_with_owner(
            self, db: Session, *, obj_in: ItemCreate, owner_id: int
    ) -> Item:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
            self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Item]:
        return (
            db.query(self.model)
            .filter(Item.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


item = CRUDItem(Item)
```

### Create an API endpoint

Add a file in the endpoints folder.

**api/api_v1/enpoints/items.py**

```python
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Item])
def read_items(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve items.
    """
    if crud.user.is_superuser(current_user):
        items = crud.item.get_multi(db, skip=skip, limit=limit)
    else:
        items = crud.item.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return items


@router.post("/", response_model=schemas.Item)
def create_item(
        *,
        db: Session = Depends(deps.get_db),
        item_in: schemas.ItemCreate,
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new item.
    """
    item = crud.item.create_with_owner(db=db, obj_in=item_in, owner_id=current_user.id)
    return item


@router.put("/{id}", response_model=schemas.Item)
def update_item(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        item_in: schemas.ItemUpdate,
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an item.
    """
    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    item = crud.item.update(db=db, db_obj=item, obj_in=item_in)
    return item


@router.get("/{id}", response_model=schemas.Item)
def read_item(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get item by ID.
    """
    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return item


@router.delete("/{id}", response_model=schemas.Item)
def delete_item(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an item.
    """
    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    item = crud.item.remove(db=db, id=id)
    return item
```

Add an entry to the router file.

**api/api_v1/api.py**

```python
from fastapi import APIRouter

from api.api_v1.endpoints import items, login, users, utils

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
```

### Install pgAdmin 4

Install pgAdmin4 with Pip.

```shell
pip install pgAdmin4
```

Navigate to the virtual environment folder and add the file `pgadmin4/config_local.py` with the following
Python code.

Virtual environment path example: `./venv/lib/python3.10/site-packages/pgadmin4/config_local.py`.

```python
import os

DATA_DIR = os.path.realpath(os.path.expanduser(u'~/.pgadmin/'))
LOG_FILE = os.path.join(DATA_DIR, 'pgadmin4.log')
SQLITE_PATH = os.path.join(DATA_DIR, 'pgadmin4.db')
SESSION_DB_PATH = os.path.join(DATA_DIR, 'sessions')
STORAGE_DIR = os.path.join(DATA_DIR, 'storage')
SERVER_MODE = False
```

### Run pgAdmin.

You can start pgAdmin after you have installed it in an active virtual environment.

```shell
pgadmin4
```

On first run, it will ask you to configure a username and password to be used to log into pgAdmin. You can use anything
you want, such as my-email@gmail.com and `randompassword`.

> Make sure to save your username and password somewhere; it won't be visible again. To recover a lost password, see the
> section below.

Visit [localhost:5050](localhost:5050) in your browser and login.

### Recover lost pgAdmin username and password

To recover a lost pgAdmin username and password, enter the following command.
