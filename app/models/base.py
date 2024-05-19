from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.core.config import settings


class BaseModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    metadata = MetaData(naming_convention=settings.db.naming_convention)
