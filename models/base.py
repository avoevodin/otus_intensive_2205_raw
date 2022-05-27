from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declared_attr, declarative_base


class Base:
    @declared_attr
    def __tablename__(cls):
        cls_name = cls.__name__.lower()
        plural_sfx = "ies" if cls_name[-1] == "y" else "s"
        cls_name = cls_name[:-1] if cls_name[-1] == "y" else cls_name
        return f"{cls_name}{plural_sfx}"

    id = Column(Integer, primary_key=True)
    yandex_code = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=False, default="", server_default="")

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.title


Base = declarative_base(cls=Base)
