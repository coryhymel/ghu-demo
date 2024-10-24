from fastapi import FastAPI, HTTPException

from database import engine, SessionLocal, Base
from models import Plan

from schemas import UserCreate
from models import User

app = FastAPI()

Base.metadata.create_all(bind=engine)


# initiate DATA
def init_db():
    db = SessionLocal()
    try:
        if db.query(Plan).count() == 0:
            plan1 = Plan(
                title="Silver Plan",
                description="Basic plan which renews monthly",
                renewalPeriod=1,
                tier=1,
                discount=0.0,
            )
            plan2 = Plan(
                title="Gold Plan",
                description="Standard plan which renews every 3 months",
                renewalPeriod=3,
                tier=2,
                discount=0.05,
            )
            plan3 = Plan(
                title="Platinum Plan",
                description="Premium plan which renews every 6 months",
                renewalPeriod=6,
                tier=3,
                discount=0.10,
            )
            plan4 = Plan(
                title="Diamond Plan",
                description="Exclusive plan which renews annually",
                renewalPeriod=12,
                tier=4,
                discount=0.25,
            )
            db.add(plan1)
            db.add(plan2)
            db.add(plan3)
            db.add(plan4)
            db.commit()
    finally:
        db.close()


@app.on_event("startup")
def on_startup():
    init_db()


@app.post("users/register/", response_model=UserCreate)
def register_user(user: UserCreate):
    db = SessionLocal()
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    # need to hash password
    db_user = User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/print_users/")
def register_user():
    import ipdb

    ipdb.set_trace
    db = SessionLocal()
    db_user = db.query(User)
    return list(db_user)
