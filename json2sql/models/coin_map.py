from utils.sql import Connection
import sqlalchemy


connection = Connection()
Base = connection.init_base()


# THIS CODE USE THE DYNAMIC CLASS
def constructure(self, **kwargs):
	self.kwargs = kwargs


