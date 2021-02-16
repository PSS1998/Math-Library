import unittest

import math_library


class TestMathLibrary(unittest.TestCase):

    def setUp(self):
        self.var1 = math_library.variable("x")
        self.var2 = math_library.variable("y")
        self.op_factory = math_library.operator_factory()
        self.func_factory = math_library.function_factory()

    def test_calculate_one_variable(self):
        exp = self.op_factory.operation("*", math_library.number(5), self.var1)
        exp = self.op_factory.operation("*", exp, self.var1)
        exp = self.op_factory.operation("+", exp, math_library.number(2))
        exp = exp.eval(self.var1, math_library.number(2))
        self.assertEqual(exp.print(), 22)

    def test_calculate_two_variable(self):
        exp = self.op_factory.operation("*", math_library.number(5), self.var1)
        exp = self.op_factory.operation("*", exp, self.var1)
        exp = self.op_factory.operation("+", exp, math_library.number(2))
        exp = self.op_factory.operation("+", exp, self.var2)
        exp = exp.eval(self.var1, math_library.number(2))
        exp = exp.eval(self.var2, math_library.number(3))
        self.assertEqual(exp.print(), 25)

    def test_calculate_deriative_simple_variable(self):
        exp = self.op_factory.operation("*", math_library.number(5), self.var1)
        exp = self.op_factory.operation("*", exp, self.var1)
        exp = self.op_factory.operation("+", exp, math_library.number(2))
        exp = self.op_factory.operation("+", exp, self.var2)
        exp = exp.derive(self.var2)
        self.assertEqual(exp.print(), 1)

    def test_calculate_deriative_complicated_variable(self):
        exp = self.op_factory.operation("*", math_library.number(5), self.var1)
        exp = self.op_factory.operation("*", exp, self.var1)
        exp = self.op_factory.operation("+", exp, math_library.number(2))
        exp = self.op_factory.operation("+", exp, self.var2)
        exp = exp.derive(self.var1)
        exp = exp.eval(self.var1, math_library.number(2))
        self.assertEqual(exp.print(), 20)

    def test_calculate_deriative_second_order(self):
        exp = self.op_factory.operation("*", math_library.number(5), self.var1)
        exp = self.op_factory.operation("*", exp, self.var1)
        exp = self.op_factory.operation("+", exp, math_library.number(2))
        exp = self.op_factory.operation("+", exp, self.var2)
        exp = exp.derive(self.var1)
        exp = exp.derive(self.var1)
        self.assertEqual(exp.print(), 10)

    def test_calculate_special_function(self):
        exp = self.op_factory.operation("*", math_library.number(5), self.var1)
        exp = self.op_factory.operation("*", exp, self.var1)
        exp = self.op_factory.operation("+", exp, math_library.number(2))
        exp = self.op_factory.operation("+", exp, self.var2)
        exp = self.func_factory.get_function("sin", exp)
        exp = exp.eval(self.var1, math_library.number(2))
        exp = exp.eval(self.var2, math_library.number(3))
        self.assertAlmostEqual(exp.print(), -0.13235175009)

    def test_calculate_deriative_with_special_function(self):
        exp = self.op_factory.operation("*", math_library.number(5), self.var1)
        exp = self.op_factory.operation("+", exp, math_library.number(2))
        exp = self.func_factory.get_function("sin", exp)
        exp = exp.derive(self.var1)
        exp = exp.eval(self.var1, math_library.number(2))
        self.assertAlmostEqual(exp.print(), 4.21926979366)

    def test_calculate_deriative_with_user_defined_function(self):
        exp = self.op_factory.operation("*", math_library.number(5), self.var1)
        exp = self.op_factory.operation("*", exp, self.var1)
        exp = self.op_factory.operation("+", exp, math_library.number(2))
        exp = self.op_factory.operation("+", exp, self.var2)
        self.func_factory.add_function("simple_function", exp)
        exp = self.func_factory.get_function("simple_function")
        exp = self.op_factory.operation("*", exp, self.var1)
        exp = self.op_factory.operation("+", exp, math_library.number(5))
        exp = exp.derive(self.var1)
        exp = exp.eval(self.var1, math_library.number(3))
        exp = exp.eval(self.var2, math_library.number(10))
        self.assertEqual(exp.print(), 147)

    def test_calculate_deriative_with_user_defined_function_with_variable_non_zero_order(self):
        exp = self.op_factory.operation("*", math_library.number(5), self.var1)
        exp = self.op_factory.operation("*", exp, self.var1)
        exp = self.op_factory.operation("+", exp, math_library.number(2))
        exp = self.op_factory.operation("+", exp, self.var2)
        self.func_factory.add_function("simple_function2", exp)
        exp = self.func_factory.get_function("simple_function2")
        func_input2 = self.op_factory.operation("*", math_library.number(3), self.var1)
        exp = exp.eval(self.var2, func_input2)
        exp = exp.eval(self.var1, math_library.number(3))
        self.assertEqual(exp.print(), 56)


if __name__ == '__main__':
    unittest.main()
