from sqlalchemy.orm import (
    MappedAsDataclass, 
    DeclarativeBase,
    Mapped,
    mapped_column,
)

from datetime import datetime

class Base(MappedAsDataclass, DeclarativeBase):
    pass

class FightToUi(Base):
    __tablename__ = "fight_to_ui_table"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    
    horde_name:         Mapped[str] = mapped_column(nullable=True, default=None)
    horde_level:        Mapped[int] = mapped_column(nullable=True, default=None)
    horde_health:       Mapped[int] = mapped_column(nullable=True, default=None)
    horde_constitution: Mapped[int] = mapped_column(nullable=True, default=None)
    horde_strength:     Mapped[int] = mapped_column(nullable=True, default=None)
    horde_dexterity:    Mapped[int] = mapped_column(nullable=True, default=None)
    horde_wisdom:       Mapped[int] = mapped_column(nullable=True, default=None)
    horde_bi:           Mapped[str] = mapped_column(nullable=True, default=None)
    horde_color:        Mapped[str] = mapped_column(nullable=True, default=None)
    
    alliance_name:         Mapped[str] = mapped_column(nullable=True, default=None)
    alliance_level:        Mapped[int] = mapped_column(nullable=True, default=None)
    alliance_health:       Mapped[int] = mapped_column(nullable=True, default=None)
    alliance_constitution: Mapped[int] = mapped_column(nullable=True, default=None)
    alliance_strength:     Mapped[int] = mapped_column(nullable=True, default=None)
    alliance_dexterity:    Mapped[int] = mapped_column(nullable=True, default=None)
    alliance_wisdom:       Mapped[int] = mapped_column(nullable=True, default=None)
    alliance_bi:           Mapped[str] = mapped_column(nullable=True, default=None)
    alliance_color:        Mapped[str] = mapped_column(nullable=True, default=None)