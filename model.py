class Scope:
    def __init__(self, parent=None):
        self.parent = parent

    def __getitem__(self, key):
        if self.__dict__.__contains__(key):
            return self.__dict__[key]
        else:
            if self.parent:
                return self.parent[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value


class Number:
    def __init__(self, value):
        self.val = value

    def evaluate(self, scope):
        return self


class Function:
    def __init__(self, args, body):
        self.args = args
        self.body = body

    def evaluate(self, scope):
        a = Number(42)
        for op in self.body:
            a = op.evaluate(scope)
        return a


class FunctionDefinition:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def evaluate(self, scope):
        scope[self.name] = self.function
        return scope[self.name]


class Conditional:
    def __init__(self, condition, if_true, if_false=None):
        self.condition = condition
        self.true = if_true
        self.false = if_false

    def __evaluate_path(self, path, scope):
        if path:
            a = Number(42)
            for op in path:
                a = op.evaluate(scope)
            return a
        else:
            return Number(42)

    def evaluate(self, scope):
        if self.condition.evaluate(scope).val == 0:
            return self.__evaluate_path(self.false, scope)
        else:
            return self.__evaluate_path(self.true, scope)


class Print:
    def __init__(self, expr):
        self.expr = expr

    def evaluate(self, scope):
        a = self.expr.evaluate(scope)
        print(a.val)
        return a


class Read:
    def __init__(self, name):
        self.name = name

    def evaluate(self, scope):
        num = Number(int(input()))
        scope[self.name] = num
        return scope[self.name]


class FunctionCall:
    def __init__(self, fun_expr, args):
        self.fun_expr = fun_expr
        self.args = args

    def evaluate(self, scope):
        function = self.fun_expr.evaluate(scope)
        call_scope = Scope(scope)
        for i in range(len(function.args)):
            op = self.args[i]
            call_scope[function.args[i]] = op.evaluate(scope)

        return function.evaluate(call_scope)


class Reference:
    def __init__(self, name):
        self.name = name

    def evaluate(self, scope):
        return scope[self.name]


class BinaryOperation:
    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs

    def evaluate(self, scope):
        a = self.lhs.evaluate(scope).val
        b = self.rhs.evaluate(scope).val
        ops = {'+': lambda a, b: a + b, '*': lambda a, b: a * b, '-': lambda a, b: a - b, '/': lambda a, b: a // b,
               '>': lambda a, b: int(a > b),
               '==': lambda a, b: int(a == b), '<=': lambda a, b: int(a <= b), '%': lambda a, b: a % b,
               '!=': lambda a, b: int(a != b), '<': lambda a, b: int(a < b),
               '>=': lambda a, b: int(a >= b), '&&': lambda a, b: int(a and b),
               '||': lambda a, b: int(a or b)}
        return Number(ops[self.op](a, b))


class UnaryOperation:
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr

    def evaluate(self, scope):
        a = self.expr.evaluate(scope).val
        ops = {'!': lambda a: int(not a), '-': lambda a: -a}
        return Number(ops[self.op](a))


if __name__ == "__main__":
    parent = Scope()
    r = Read(1)
    r.evaluate(parent)
    parent[2] = Number(1)
    parent[3] = Number(6)
    parent[4] = Number(1)
    con1 = BinaryOperation(parent[3], '>', parent[1])
    BO1 = BinaryOperation(parent[1], '*', parent[2])
    BO2 = BinaryOperation(parent[4], '+', parent[4])
    UO1 = UnaryOperation('!', BO2)
    CON = Conditional(con1, [UO1])
    print(CON.evaluate(parent).val)
    func = Function([parent[1], parent[2]], [BO1, BO2])
    f1 = FunctionDefinition(1, func)
    f1.evaluate(parent)
    p = Print(parent[1])
    p.evaluate(parent)
    p.evaluate(parent)
    r = Reference(1)
    son = Scope(parent)
    son['f2'] = Number(4)
    r2 = Reference(1)
    print(r2.evaluate(son).evaluate(parent).val)
    grandson = Scope(son)
    grandson['f3'] = Number(3)
    r3 = Reference(2)
    print(r.evaluate(parent).evaluate(parent).val)
    p.evaluate(parent)

