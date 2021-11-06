import sqlalchemy
from sqlalchemy import Column, Text, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine("postgresql://postgres:789456@localhost:5432/test1")

conn = engine.connect()

result = conn.execute("SELECT * FROM hands")

for row in result:
    print(f"{row=}")

# with conn.begin() as trans:
#     conn.execute(
#         "INSERT INTO hands (user_name, time_left, jail) VALUES ('neo', 100, 'p9')"
#     )
#
# result.close()

Base = declarative_base()


class Hands(Base):
    __tablename__ = "hands"

    user_name = Column(String(100), primary_key=True)
    opened_cards = Column(Text)
    available_cards = Column(Text)
    time_left = Column(Integer)
    police = Column(Integer)
    police_cards = Column(Text)
    last_card = Column(String(5))
    jail = Column(String(5))
    rate = Column(Integer)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

n = Hands(user_name="lub", jail="p3", time_left=12)
session.add(n)
session.commit()

for item in session.query(Hands).filter(Hands.user_name == "lub"):
    print(f"{item.time_left=}")
