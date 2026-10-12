from sqlalchemy import create_engine, Column, INTEGER, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("sqlite:///digishop.db")
engine.connect()

Base = declarative_base()

# --------------- user database ---------------------
class User(Base):
    __tablename__ = "userInfo"

    id = Column(INTEGER, primary_key=True)
    name = Column(String)
    address = Column(String)
    score = Column(Float)

# --------------- product database ------------------
class Product(Base):
    __tablename__ = "productInfo"

    id = Column(INTEGER, primary_key=True)
    name = Column(String)
    num = Column(INTEGER)
    price = Column(INTEGER)
    rate = Column(Float)


Base.metadata.create_all(engine)

session: sqlalchemy.orm.session.sessionmaker[Session] = sessionmaker(bind=engine)
sessionLocal = session()

###################################################
# user1 = User(name="Mohammad", address="Ahwaz", score=4.9)
# user2 = User(name="Ali", address="Tehran", score=4.95)

# sessionLocal.add(user1)
# sessionLocal.add(user2)
# sessionLocal.commit()

# user3 = User(name="Mahan", address="Shiraz", score=4)
# user4 = User(name="Matin", address="Ahwaz", score=4.2)
# sessionLocal.add_all([user3, user4])
# sessionLocal.commit()

# users = sessionLocal.query(User).all()
# print(users)
# for item in users:
#     print("name: ", item.name)
#     print("add: ", item.address)
#     print("score: ", item.score)
#     print("-" * 30)


# #------------------products-------------

# Pro1 = Product(name = "Asus" , num = 10 , price = 200000 , rate = 1.6)
# Pro2 = Product(name = "morteza" , num = 1 , price = 1 , rate = 0.0001)
# Pro3 = Product(name = "mamad_mehdi" , num = 1 , price = 1 , rate = 0.00001)

# sessionLocal.add(Pro1)
# sessionLocal.add(Pro2)
# sessionLocal.add(Pro3)
# sessionLocal.commit()


#_________________filter__________________

# temp_user = sessionLocal.query(User).filter_by(address = "Ahwaz").first()
# print(temp_user.name)
# print(temp_user.address)

#-------------------------filter2------------------]

# temp_user = sessionLocal.query(User).filter(User.score > 4.9).all()

# print(temp_user)

# for item in temp_user :
#     print(item.name)
#     print(item.score)

# temp_user =sessionLocal.query(User).filter(User.name.like("%Ali%")).all
# print(temp_user)

# for item in temp_user:
#     print(item.name)
#     print(item.score)

user = sessionLocal.query(User).filter_by(id=1).first()

user.name = "saeed"
user.address = "tabriz"
sessionLocal.commit()

if user !=None:
    sessionLocal.delete(user)
    sessionLocal.commit()