import uuid
import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from datetime import date, datetime   
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from decimal import Decimal

class User(Base):
    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(sqlalchemy.String, unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(sqlalchemy.String, nullable=False)
    full_name: Mapped[str] = mapped_column(sqlalchemy.String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(sqlalchemy.DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(sqlalchemy.DateTime, nullable=False)

class Account(Base):
    __tablename__ = "accounts"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    name: Mapped[str] = mapped_column(sqlalchemy.String, nullable=False)
    balance: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(sqlalchemy.DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(sqlalchemy.DateTime, nullable=False)
    
class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    name: Mapped[str] = mapped_column(sqlalchemy.String, nullable=False)

import enum
from sqlalchemy import Enum as SQLEnum

class TransactionType(str, enum.Enum):
    RECEITA = "RECEITA"
    DESPESA = "DESPESA"

class Transaction(Base):
    __tablename__ = "transactions"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    account_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("accounts.id"), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)
    amount:Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False, default=0)
    type: Mapped[TransactionType] = mapped_column(SQLEnum(TransactionType), nullable=False)
    created_at: Mapped[datetime] = mapped_column(sqlalchemy.DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(sqlalchemy.DateTime, nullable=False)
    
class Goal(Base):
    __tablename__ = "goals"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    name: Mapped[str] = mapped_column(sqlalchemy.String, nullable=False)
    target_amount:Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False, default=0)
    deadline: Mapped[date] = mapped_column(sqlalchemy.Date, nullable=False)
    created_at: Mapped[datetime] = mapped_column(sqlalchemy.DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(sqlalchemy.DateTime, nullable=False)
        
    
        