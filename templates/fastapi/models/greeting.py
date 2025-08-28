# models/greeting.py
from pydantic import BaseModel
from typing import Optional

class Greeting(BaseModel):
    message: str
    greeting_type: str
    recipient: Optional[str] = None