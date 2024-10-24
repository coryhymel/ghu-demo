from datetime import date

from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    username: str
    email: EmailStr
    password: str


class Magazine(BaseModel):
    name: str
    description: str
    base_price: float = Field(gt=0, description="The price must be greater than zero")


class Plan(BaseModel):
    title: str
    description: str
    renewalPeriod: int = Field(
        gt=0,
        description="A numerical value that represents the number of months in which the subscription would renew.",
    )
    tier: int = Field(
        gt=0,
        max_digits=1,
        description="The tier is a numerical value that represents the level of the plan.",
    )
    discount: float = Field(description="A percentage, expressed as a decimal")


class Subscription(BaseModel):
    user_id: int
    magazine_id: int
    plan_id: int
    price: float
    renewal_date: date
    is_active: bool
