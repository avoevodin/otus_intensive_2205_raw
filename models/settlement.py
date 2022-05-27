from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import TimestampMixin

if TYPE_CHECKING:
    from .country import Country
    from .region import Region


class Settlement(TimestampMixin, Base):
    region_id = Column(Integer, ForeignKey("regions.id"), nullable=True)
    country_id = Column(Integer, ForeignKey("countries.id"))

    region = relationship("Region", back_populates="settlements")
    country = relationship("Country", back_populates="settlements")

    if TYPE_CHECKING:
        country: Country
        region: Region

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"title={self.title!r}, "
            f"yandex_code={self.yandex_code}, "
            f"country_id={self.country_id}, "
            f"region_id={self.region_id}, "
            f"created_at={self.created_at}"
            ")"
        )

    def get_code(self):
        return {
            "title": self.title,
            "country_code": self.country.id,
            "region_code": self.region.id if self.region else "",
            "code": self.yandex_code,
        }
