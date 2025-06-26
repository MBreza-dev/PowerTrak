from typing import Optional
from sqlmodel import SQLModel, Field


class Equipment(SQLModel, table=True):
    """
    A piece of equipment owned by a customer.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id")
    name: str
    serial_number: Optional[str] = None
    model: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[str] = Field(default=None, alias="created_at")
    updated_at: Optional[str] = Field(default=None, alias="updated_at")
