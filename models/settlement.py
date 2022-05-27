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
