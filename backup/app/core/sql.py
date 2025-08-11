import logging

from functools import wraps
from typing import Callable
from sqlalchemy import create_engine, event
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    DeclarativeBase,
    MappedAsDataclass,
)
from app.core.config import settings

logger = logging.getLogger(__name__)


class Base(DeclarativeBase, MappedAsDataclass):
    """
    Base class to be inherited by all models in the application.
    """

    pass


engine = create_engine(
    settings.SQLITE_FILE,
    connect_args={"autocommit": False},
)


# This is necessary to enable foreign key constraints in SQLite.
# LINK: https://stackoverflow.com/questions/2614984/sqlite-sqlalchemy-how-to-enforce-foreign-keys
# https://docs.sqlalchemy.org/en/20/dialects/sqlite.html#foreign-key-support
def _fk_pragma_on_connect(dbapi_con, con_record):
    dbapi_con.execute("pragma foreign_keys=ON")


event.listen(engine, "connect", _fk_pragma_on_connect)

# LINK: https://docs.sqlalchemy.org/en/20/orm/contextual.html#sqlalchemy.orm.scoped_session
session = scoped_session(
    session_factory=sessionmaker(
        bind=engine,
        autocommit=False,
        expire_on_commit=False,
    )
)


def transaction(func: Callable):
    """
    Decorator to handle database transactions in the application

    params:
    session: scoped_session - SQLAlchemy session object.

    LINK: https://docs.sqlalchemy.org/en/20/orm/session_transaction.html
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        with session() as s:
            with s.begin():
                try:
                    called = func(
                        *args,
                        **kwargs,
                        transaction_session=s,
                    )
                    s.commit()
                    return called
                except Exception as e:
                    logger.error(f"Transaction failed: {e}")
                    s.rollback()
                    raise
                finally:
                    s.close()

    return wrapper
