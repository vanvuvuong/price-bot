from json2sql.utils.sql import Connection
import sqlalchemy


connection = Connection()
Base = connection.init_base()


def get_column(data):
	columns = data.keys()
	result = []
	for column in columns:
		globals()[column] = sqlalchemy.Column(column,sqlalchemy.Text, nullable=True)
		result.append(globals()[column])
	params = tuple(result)
	return params

# THIS CODE USE THE MODEL DYNAMIC CLASS
# constructor
def constructor(self, **args):
	for column in args:
		self.column = column

# method
def method(self, arg):
	# NO NEED FOR METHOD
	print(arg)

# class method
@classmethod
def class_method(cls, arg):
	# NO NEED FOR CLASS METHOD
	print(arg)

Model = type("Model", (Base, ),
		{
	# constructor
	"__init__": constructor,
	# properties
	"type": "Dynamic Instance",
	# functions and method
	"func_arg": method,
	"class_func": class_method
	})
