from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.db.session import Base


class Transaction(Base):
    __tablename__ = "transactions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    amount: Mapped[float] = mapped_column(Float, nullable=False )
    description: Mapped[str] = mapped_column(String(200),nullable=False)
    type: Mapped[str] = mapped_column(String(20), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, nullable=False)
    