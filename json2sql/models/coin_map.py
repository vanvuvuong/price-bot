from json2sql.utils.sql import Connection
import sqlalchemy


connection = Connection()
Base = connection.init_base()


# THIS CODE USE THE DYNAMIC CLASS
# constructor
def constructor(self, **args):
	self.args = args

# method
def method(self, arg):
	print(arg)

# class method
@classmethod
def class_method(cls, arg):
	print(arg)

dynamic_class = type("DynamicClass", (object, ),
		{
	# constructor
	"__init__": constructor,
	# properties
	"type": "column",
	# functions and method
	"func_arg": method,
	"class_func": class_method
	})
