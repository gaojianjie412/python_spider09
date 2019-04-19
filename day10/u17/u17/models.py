# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
# from sqlalchemy.orm import sessionmaker, relationship
# from sqlalchemy import create_engine
#
# engine = create_engine("mysql+pymysql://root:ganyouheng@127.0.0.1:3306/u17?charset=utf8", max_overflow=5,encoding='utf-8')
# Base = declarative_base()
#
# class U17(Base):
#     __tablename__ = 'comic'
#     id = Column(Integer, primary_key=True, autoincrement=True)    #主键，自增
#     comic_id = Column(String(32))
#     name = Column(String(128))
#     cover = Column(String(1024))
#     line2 = Column(String(512))
#
#     def __repr__(self):
#         output = "(%d,%s)" % (self.id, self.name)
#         return output
#
# Base.metadata.create_all(engine)
