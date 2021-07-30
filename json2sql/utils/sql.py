from config import yaml_config
import sqlalchemy

class Connection(object):

	def __init__(self) -> None:
		pass
	
	def make_engine(self, config_file_path):
		config = yaml_config(config_file_path)

