import datetime
from app.core.sql import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import false, func


class Backup(Base):
    __tablename__ = "backup"
    id: Mapped[str] = mapped_column(primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        nullable=False,
        server_default=func.now(),
        insert_default=func.now(),
    )
    is_deleted: Mapped[bool] = mapped_column(
        nullable=False,
        server_default=false(),
        insert_default=false(),
    )
