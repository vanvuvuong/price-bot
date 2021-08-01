from config import yaml_config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import sqlalchemy


class Connection(object):

	def __init__(self) -> None:
		pass
	
	def init_engine(self, config_file_path):
		config = yaml_config(config_file_path)
		engine_url = f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}/{config['database']}"
		try:
			engine = sqlalchemy.create_engine(engine_url, encoding='utf-8', echo=True)
			return engine
		except Exception as e:
			print("Couldn't get the engine. Please re-checking the config.yaml")
			print(e)
			return None

	def init_session(self, engine):
		session = Session(engine)
		return session

	def init_base(self):
		Base = declarative_base()
		return Base
