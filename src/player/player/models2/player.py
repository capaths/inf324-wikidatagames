import sqlalchemy, json
from sqlalchemy import create_engine, Column, Integer,String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from nameko_sqlalchemy import Database, transaction_retry



engine = create_engine('sqlite:///player.db', echo=False)
Base = declarative_base()
class Player(Base):
	__tablename__='players'
	id = Column(Integer, Sequence('player_id_seq') ,primary_key=True)
	username = Column(String(50))
	password = Column(String(50))
	country = Column(String(50))
	elo = Column(Integer)

	def __repr__(self):
		return "<Player(username='%s', password='%s',country='%s', elo='%d')>" % (self.username, self.password, self.country, self.elo)
	    
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def get_all():
        array = []
        for instance in session.query(Player).order_by(Player.id):
                dicto = {}
                dicto['id'] = instance.id
                dicto['username'] = instance.username
                dicto['password'] = instance.password
                dicto['country'] = instance.country
                dicto['elo'] = instance.elo
                array.append(dicto)
        return json.dumps(array)

def get_by_id(ide):
        searched = session.query(Player).filter_by(id=ide).first()
        if searched is None:
                return None
        dicto = {}
        dicto['id'] = searched.id
        dicto['username'] = searched.username
        dicto['password'] = searched.password
        dicto['country'] = searched.country
        dicto['elo'] = searched.elo
        return json.dumps(dicto)

def get_by_username(iusername):
        
        searched = session.query(Player).filter_by(username=iusername).first()
        if searched is None:
                return None
        dicto = {}
        dicto['id'] = searched.id
        dicto['username'] = searched.username
        dicto['password'] = searched.password
        dicto['country'] = searched.country
        dicto['elo'] = searched.elo
        
        return dicto



def add(iusername,ipassword,icountry='unknown',ielo=1000):
        new_player = Player(username=iusername, password=ipassword, country=icountry, elo=ielo)
        session.add(new_player)
        session.commit()
        return new_player


def delete(ide):
        if get(ide) == None:
                return None
        else:
                print("Eliminando: ",get(ide))
                del_player = session.query(Player).filter_by(id=ide).delete()

def update(ide,iusername,ipassword,icountry):
        upd_player =  session.query(Player).filter_by(id=ide).first()
        if iusername != '':
                upd_player.username = iusername
        if ipassword != '':
                upd_player.password = ipassword
        if icountry != '':
                upd_player.country = icountry

        print(session.dirty)
        session.commit()
        



        


        



        
