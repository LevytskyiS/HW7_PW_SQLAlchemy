from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:hello@localhost/hw7")
Session = sessionmaker(bind=engine)
session = Session()
