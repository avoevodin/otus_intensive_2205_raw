from typing import TYPE_CHECKING, List

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import TimestampMixin

if TYPE_CHECKING:
    from .country import Country
    from .settlement import Settlement


class Region(TimestampMixin, Base):
    country_id = Column(Integer, ForeignKey("countries.id"), nullable=False)

    country = relationship("Country", back_populates="regions")
    settlements = relationship("Settlement", back_populates="region")

    if TYPE_CHECKING:
        country: Country
        settlements: List[Settlement]

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"title={self.title!r}, "
            f"yandex_code={self.yandex_code}, "
            f"country_id={self.country_id}, "
            f"created_at={self.created_at}"
            ")"
        )
