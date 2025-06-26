from typing import Optional
from sqlmodel import SQLModel, Field


class Customer(SQLModel, table=True):
    """
    A customer who brings in equipment for repair.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    created_at: Optional[str] = Field(default=None, alias="created_at")
    updated_at: Optional[str] = Field(default=None, alias="updated_at")
