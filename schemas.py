from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Subscriber(BaseModel):
    """
    Newsletter subscribers collection
    Collection name: "subscriber" (lowercase of class name)
    """
    email: EmailStr = Field(..., description="Subscriber email address")
    source: Optional[str] = Field('website', description="Signup source")
