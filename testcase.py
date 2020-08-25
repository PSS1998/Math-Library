import math_library

def test():
    var1 = math_library.variable("x")
    var2 = math_library.variable("y")
    op_factory = math_library.operator_factory()
    func_factory = math_library.function_factory()

    # test 1
    exp = op_factory.operation("*", math_library.number(5), var1)
    exp = op_factory.operation("*", exp, var1)
    exp = op_factory.operation("+", exp, math_library.number(2))
    exp = exp.eval(var1, math_library.number(2))
    print(exp.print())

    # test 2
    exp = op_factory.operation("*", math_library.number(5), var1)
    exp = op_factory.operation("*", exp, var1)
    exp = op_factory.operation("+", exp, math_library.number(2))
    exp = op_factory.operation("+", exp, var2)
    exp = exp.eval(var1, math_library.number(2))
    exp = exp.eval(var2, math_library.number(3))
    print(exp.print())

    # test 3
    exp = op_factory.operation("*", math_library.number(5), var1)
    exp = op_factory.operation("*", exp, var1)
    exp = op_factory.operation("+", exp, math_library.number(2))
    exp = op_factory.operation("+", exp, var2)
    exp = exp.derive(var2)
    print(exp.print())

    # test 4
    exp = op_factory.operation("*", math_library.number(5), var1)
    exp = op_factory.operation("*", exp, var1)
    exp = op_factory.operation("+", exp, math_library.number(2))
    exp = op_factory.operation("+", exp, var2)
    exp = exp.derive(var1)
    exp = exp.eval(var1, math_library.number(2))
    print(exp.print())

    # test 5
    exp = op_factory.operation("*", math_library.number(5), var1)
    exp = op_factory.operation("*", exp, var1)
    exp = op_factory.operation("+", exp, math_library.number(2))
    exp = op_factory.operation("+", exp, var2)
    exp = exp.derive(var1)
    exp = exp.derive(var1)
    print(exp.print())

    # test 6
    exp = op_factory.operation("*", math_library.number(5), var1)
    exp = op_factory.operation("*", exp, var1)
    exp = op_factory.operation("+", exp, math_library.number(2))
    exp = op_factory.operation("+", exp, var2)
    exp = func_factory.get_function("sin", exp)
    exp = exp.eval(var1, math_library.number(2))
    exp = exp.eval(var2, math_library.number(3))
    print(exp.print())

    # test 7
    exp = op_factory.operation("*", math_library.number(5), var1)
    exp = op_factory.operation("+", exp, math_library.number(2))
    exp = func_factory.get_function("sin", exp)
    exp = exp.derive(var1)
    exp = exp.eval(var1, math_library.number(2))
    print(exp.print())

    # test 8
    exp = op_factory.operation("*", math_library.number(5), var1)
    exp = op_factory.operation("*", exp, var1)
    exp = op_factory.operation("+", exp, math_library.number(2))
    exp = op_factory.operation("+", exp, var2)
    func_factory.add_function("simple_function", exp)
    exp = func_factory.get_function("simple_function")
    exp = op_factory.operation("*", exp, var1)
    exp = op_factory.operation("+", exp, math_library.number(5))
    exp = exp.derive(var1)
    exp = exp.eval(var1, math_library.number(3))
    exp = exp.eval(var2, math_library.number(10))
    print(exp.print())

    # test 9
    exp = op_factory.operation("*", math_library.number(5), var1)
    exp = op_factory.operation("*", exp, var1)
    exp = op_factory.operation("+", exp, math_library.number(2))
    exp = op_factory.operation("+", exp, var2)
    func_factory.add_function("simple_function2", exp)
    exp = func_factory.get_function("simple_function2")
    func_input2 = op_factory.operation("*", math_library.number(3), var1)
    exp = exp.eval(var2, func_input2)
    exp = exp.eval(var1, math_library.number(3))
    print(exp.print())


if __name__ == "__main__":
    test()