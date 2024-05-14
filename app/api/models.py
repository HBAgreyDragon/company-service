from pydantic import BaseModel
from typing import List, Optional


class CompanyIn(BaseModel):
    name: str
    description: str
    count_users: str
    year: str
    plane_id: List[int]


class CompanyOut(CompanyIn):
    id: int


class CompanyUpdate(CompanyIn):
    name: Optional[str] = None
    description: Optional[str] = None
    count_users: Optional[str] = None
    year: Optional[str] = None
    currency_id: Optional[List[int]] = None