from typing import TYPE_CHECKING, List

from sqlalchemy.orm import relationship

from .base import Base
from .mixins import TimestampMixin

if TYPE_CHECKING:
    from .region import Region
    from .settlement import Settlement


class Country(TimestampMixin, Base):
    regions = relationship("Region", back_populates="country")
    settlements = relationship("Settlement", back_populates="country")

    if TYPE_CHECKING:
        regions: Region
        settlements: List[Settlement]
