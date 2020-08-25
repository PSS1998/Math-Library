from abc import ABC, abstractmethod
import math


class Iexpression(ABC):
	@abstractmethod
	def derive(self):
		pass

	@abstractmethod
	def eval(self):
		pass

class expression(Iexpression):
	def derive(self):
		self.derive()

	def eval(self):
		self.eval()

class operator(Iexpression):
	def __init__(self, left_exp, right_exp):
		self.left_exp = left_exp
		self.right_exp = right_exp

	def derive(self):
		pass

	def eval(self):
		pass

	def check_number(self):
		if(isinstance(self.left_exp, number) and isinstance(self.right_exp, number)):
			return True
		elif(isinstance(self.left_exp, number) and isinstance(self.right_exp, operator) and self.right_exp.check_number()):
			return True
		elif(isinstance(self.left_exp, operator) and isinstance(self.right_exp, number) and self.left_exp.check_number()):
			return True
		elif(isinstance(self.left_exp, operator) and isinstance(self.right_exp, operator) and self.left_exp.check_number() and self.right_exp.check_number()):
			return True
		else:
			return False

class add_operator(operator):
	def derive(self, var):
		return add_operator(self.left_exp.derive(var), self.right_exp.derive(var))

	def eval(self, var, value):
		return add_operator(self.left_exp.eval(var, value), self.right_exp.eval(var, value))

	def print(self):
		return self.left_exp.print() + self.right_exp.print()

class sub_operator(operator):
	def derive(self, var):
		return sub_operator(self.left_exp.derive(var), self.right_exp.derive(var))

	def eval(self, var, value):
		return sub_operator(self.left_exp.eval(var, value), self.right_exp.eval(var, value))

	def print(self):
		return self.left_exp.print() - self.right_exp.print()

class mult_operator(operator):
	def derive(self, var):
		return add_operator(mult_operator(self.left_exp.derive(var), self.right_exp), mult_operator(self.right_exp.derive(var), self.left_exp))

	def eval(self, var, value):
		if((isinstance(self.left_exp.eval(var, value), number) and self.left_exp.eval(var, value).print()==0) or (isinstance(self.right_exp.eval(var, value), number) and self.right_exp.eval(var, value).print()==0)):
			return number(0)
		else:
			return mult_operator(self.left_exp.eval(var, value), self.right_exp.eval(var, value))

	def print(self):
		if((isinstance(self.left_exp, number) and self.left_exp.print()==0) or (isinstance(self.right_exp, number) and self.right_exp.print()==0)):
			return 0
		elif(self.left_exp==0 or self.right_exp==0):
			return 0
		else:
			return self.left_exp.print() * self.right_exp.print()

class div_operator(operator):
	def derive(self, var):
		return div_operator(sub_operator(mult_operator(self.left_exp.derive(var), self.right_exp), mult_operator(self.right_exp.derive(var), self.left_exp)), (mult_operator(self.right_exp,self.right_exp)))

	def eval(self, var, value):
		return div_operator(self.left_exp.eval(var, value), self.right_exp.eval(var, value))

	def print(self):
		if((isinstance(self.left_exp, number) and self.left_exp.print()==0)):
			return 0
		else:
			return self.left_exp.print() / self.right_exp.print()

class operator_factory():
	def operation(self, operator, left_exp, right_exp):
		if(operator == "+"):
			return add_operator(left_exp, right_exp)
		elif(operator == "-"):
			return sub_operator(left_exp, right_exp)
		elif(operator == "*"):
			return mult_operator(left_exp, right_exp)
		elif(operator == "/"): 
			return div_operator(left_exp, right_exp)

class variable(Iexpression):
	def __init__(self, name):
		self.variable_name = name

	def derive(self, var):
		if (var.variable_name == self.variable_name):
			return number(1)
		else:
			return number(0)

	def eval(self, var, value):
		if (var.variable_name == self.variable_name):
			return value
		else:
			return self

	def print(self):
		return 0

class number(Iexpression):
	def __init__(self, value):
		self.value = value

	def derive(self, var):
		return number(0)

	def eval(self, var, value):
		return number(self.value)

	def print(self):
		return self.value

class function(Iexpression):
	def derive(self):
		pass

	def eval(self):
		pass

class sin_function(function):
	def __init__(self, exp):
		self.exp = exp

	def derive(self, var):
		if(self.exp != self.exp.derive(var)):
			return mult_operator(cos_function(self.exp), self.exp.derive(var))
		else:
			number(0)

	def eval(self, var, value):
		if(isinstance(self.exp, number)):
			return number(math.sin(self.var.print()))
		else:
			if(isinstance(self.exp.eval(var, value), number)):
				return number(math.sin(self.exp.eval(var, value).print()))
			elif(isinstance(self.exp.eval(var, value), operator) and self.exp.eval(var, value).check_number()):
				return number(math.sin(self.exp.eval(var, value).print()))
			else:
				return sin_function(self.exp.eval(var, value))

class cos_function(function):
	def __init__(self, exp):
		self.exp = exp

	def derive(self, var):
		if(self.exp != self.exp.derive(var)):
			return mult_operator(sin_function(self.exp), self.exp.derive(var))
		else:
			number(0)

	def eval(self, var, value):
		if(isinstance(self.exp, number)):
			return number(math.cos(self.var.print()))
		else:
			if(isinstance(self.exp.eval(var, value), number)):
				return number(math.cos(self.exp.eval(var, value).print()))
			elif(isinstance(self.exp.eval(var, value), operator) and self.exp.eval(var, value).check_number()):
				return number(math.cos(self.exp.eval(var, value).print()))
			else:
				return cos_function(self.exp.eval(var, value))

class function_factory():
	def __init__(self):
		self.map_function = {"sin":sin_function, "cos":cos_function}
		self.user_function = {}

	def get_function(self, function, input_variable=None):
		if(function in self.user_function):
			return self.user_function[function]
		else:
			return self.map_function[function](input_variable)

	def add_function(self, name, exp):
		self.user_function[name] = exp
