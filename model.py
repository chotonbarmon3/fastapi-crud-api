from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column

class base(DeclarativeBase):
    pass

class user(base):
    __tablename__="users"
    id : Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]
    role:Mapped[str]
    password:Mapped[str]


