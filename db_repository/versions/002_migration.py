from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
author = Table('author', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=120)),
    Column('last_name', String(length=120)),
)

book = Table('book', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=64)),
    Column('author_id', Integer),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=64)),
    Column('email', String(length=120)),
    Column('role', SmallInteger, default=ColumnDefault(0)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['author'].create()
    post_meta.tables['book'].create()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['author'].drop()
    post_meta.tables['book'].drop()
    post_meta.tables['user'].drop()
