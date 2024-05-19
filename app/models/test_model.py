from sqlalchemy.orm import Mapped

from app.models import BaseModel


class TestModel(BaseModel):
    __tablename__ = "test_model"
    name: Mapped[int]
