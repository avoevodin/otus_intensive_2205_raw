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

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"title={self.title!r}, "
            f"yandex_code={self.yandex_code}, "
            f"created_at={self.created_at}"
            ")"
        )

    if TYPE_CHECKING:
        regions: Region
        settlements: List[Settlement]
