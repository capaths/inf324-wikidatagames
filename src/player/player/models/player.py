import sqlalchemy, json
from sqlalchemy import create_engine, Column, Integer,String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from nameko_sqlalchemy import Database, transaction_retry



engine = create_engine('sqlite:///user.db', echo=False)
Base = declarative_base()
class User(Base):
	__tablename__='users'
	id = Column(Integer, Sequence('user_id_seq') ,primary_key=True)
	name = Column(String(50))
	password = Column(String(50))
	country = Column(String(50))
	elo = Column(Integer)

	def __repr__(self):
		return "<User(name='%s', password='%s',country='%s', elo='%d')>" % (self.name, self.password, self.country, self.elo)
	    
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def get_all():
        array = []
        for instance in session.query(User).order_by(User.id):
                dicto = {}
                dicto['id'] = instance.id
                dicto['name'] = instance.name
                dicto['password'] = instance.password
                dicto['country'] = instance.country
                dicto['elo'] = instance.elo
                array.append(dicto)
        return json.dumps(array)

def get(item):
        searched = session.query(User).filter_by(id=item).first()
        dicto = {}
        dicto['id'] = searched.id
        dicto['name'] = searched.name
        dicto['password'] = searched.password
        dicto['country'] = searched.country
        dicto['elo'] = searched.elo
        return json.dumps(dicto)
        

def add(iname,ipassword,icountry='Chile',ielo=1000):
        new_user = User(name=iname, password=ipassword, country=icountry, elo=ielo)
        session.add(new_user)
        session.commit()
        return new_user
