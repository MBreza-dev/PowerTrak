from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field, Column
from sqlalchemy import DateTime


class Job(SQLModel, table=True):
    """
    A repair job for a customer’s equipment.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id")
    equipment_id: int = Field(foreign_key="equipment.id")
    description: Optional[str] = None
    status: str = Field(default="pending")
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), default=datetime.utcnow),
    )
    completed_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), nullable=True),
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), onupdate=datetime.utcnow),
    )
