"""Модели базы данных — User, Channel + доменные модели (Proverb, Favorite, ProverbOfDay)"""
from datetime import date as date_t, datetime

from sqlalchemy import (
    BigInteger,
    Date,
    DateTime,
    Integer,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Базовый класс для всех моделей"""
    pass


class User(Base):
    """Пользователь бота"""
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True)
    username: Mapped[str | None] = mapped_column(String(255), nullable=True)
    full_name: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    # язык интерфейса: ru / uz_latn / uz_cyrl / en
    language: Mapped[str] = mapped_column(String(10), default="ru")

    def __repr__(self) -> str:
        return f"<User {self.telegram_id} ({self.username})>"


class Channel(Base):
    """Канал/группа для обязательной подписки"""
    __tablename__ = "channels"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    channel_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    title: Mapped[str] = mapped_column(String(255))
    invite_link: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    def __repr__(self) -> str:
        return f"<Channel {self.channel_id} ({self.title})>"


class Proverb(Base):
    """Мақол — узбекская пословица"""
    __tablename__ = "proverbs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text_latn: Mapped[str] = mapped_column(String(1000))            # латиница (обязательно)
    text_cyrl: Mapped[str] = mapped_column(String(1000))            # кириллица (обязательно)
    meaning_uz: Mapped[str | None] = mapped_column(String(2000), nullable=True)     # толкование
    translation_ru: Mapped[str | None] = mapped_column(String(1000), nullable=True) # перевод
    translation_en: Mapped[str | None] = mapped_column(String(1000), nullable=True)
    equivalent_ru: Mapped[str | None] = mapped_column(String(500), nullable=True)   # русский аналог
    equivalent_en: Mapped[str | None] = mapped_column(String(500), nullable=True)
    source: Mapped[str] = mapped_column(String(500))                # источник (обязателен)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    def __repr__(self) -> str:
        return f"<Proverb {self.id}: {self.text_latn[:40]}...>"


class Favorite(Base):
    """Избранные мақолы пользователя"""
    __tablename__ = "favorites"
    __table_args__ = (
        UniqueConstraint("telegram_id", "proverb_id", name="uq_favorite_user_proverb"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, index=True)
    proverb_id: Mapped[int] = mapped_column(Integer, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    def __repr__(self) -> str:
        return f"<Favorite user={self.telegram_id} proverb={self.proverb_id}>"


class ProverbOfDay(Base):
    """История мақол дня (по одной записи на дату)"""
    __tablename__ = "proverbs_of_day"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    proverb_id: Mapped[int] = mapped_column(Integer, index=True)
    day: Mapped[date_t] = mapped_column(Date, unique=True, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    def __repr__(self) -> str:
        return f"<ProverbOfDay {self.day}: proverb={self.proverb_id}>"
