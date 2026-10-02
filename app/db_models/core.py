from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey, UniqueConstraint
from sqlalchemy.sql import func
from app.database import Base

class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    source_url = Column(String(255))
    created_at = Column(TIMESTAMP, server_default=func.now())


class ImageClass(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    dataset_id = Column(Integer, ForeignKey("datasets.id"), nullable=False)
    name = Column(String(50), nullable=False)

    __table_args__ = (UniqueConstraint("dataset_id", "name"),)


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, autoincrement=True)
    dataset_id = Column(Integer, ForeignKey("datasets.id"), nullable=False)
    file_name = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=False)
    width = Column(Integer)
    height = Column(Integer)
    split = Column(Enum("train", "val", "test", name="split_enum"), default="train")
    status = Column(
        Enum("ingested", "prelabeled", "flagged", "passed", name="status_enum"),
        default="ingested",
    )
    created_at = Column(TIMESTAMP, server_default=func.now())

    __table_args__ = (UniqueConstraint("dataset_id", "file_name"),)