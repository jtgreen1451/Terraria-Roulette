from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped


from db_models.base import Base

class WeaponDB(Base):
    __tablename__ = "processed_weapons"

    Name: Mapped[str] = mapped_column(String, primary_key=True)
    Image: Mapped[str] = mapped_column(String, nullable=False)
    Stage: Mapped[str] = mapped_column(String, nullable=False)