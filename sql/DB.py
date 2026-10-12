from sqlalchemy import create_engine, Column, INTEGER, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///Social_Media.db")

Base = declarative_base()


class User(Base):
    __tablename__ = "usersInfo"

    id = Column(INTEGER, primary_key=True)
    name = Column(String)
    username = Column(String)

    posts = relationship("Post", back_populates="owner")


class Post(Base):
    __tablename__ = "postsInfo"

    id = Column(INTEGER, primary_key=True)
    title = Column(String)

    user_id = Column(INTEGER, ForeignKey("usersInfo.id"))

    owner = relationship("User", back_populates="posts")


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sessionLocal = Session()


#---------------- Users ----------------

user1 = User(name="Mohammad azizi", username="mkm79")
user2 = User(name="Mahan kz", username="mkz80")

sessionLocal.add_all([user1, user2])
sessionLocal.commit()


#---------------- Posts ----------------

post1 = Post(title="Subject 1", user_id=1)
post2 = Post(title="Subject 2", user_id=2)

sessionLocal.add_all([post1, post2])
sessionLocal.commit()


# ---------------- Query ----------------

temp = sessionLocal.query(User).filter_by(id=1).first()

if temp is not None:
    print(temp.name)
    print(temp.posts)