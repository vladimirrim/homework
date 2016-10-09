class Scope(object):
    def __init__(self, parent=None):
        self.parent = parent

    def __getitem__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        else:
            return self.parent.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value


class Number:
    def __init__(self, value):
        self.val = value

    def evaluate(self, scope):
        if scope.parent is None:
            return self
        else:
            return self.evaluate(self, scope.parent)


class Function:
    def __init__(self, args, body):
        self.args = args
        self.body = body

    def evaluate(self, scope):
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

    def evaluate(self, scope):
        if self.condition.evaluate(scope).val == 0:
            for op in self.false:
                a = op.evaluate(scope)
            return a
        else:
            for op in self.true:
                a = op.evaluate(scope)
            return a


class Print:
    def __init__(self, expr):
        self.expr = expr

    def evaluate(self, scope):
        print(self.expr.evaluate(scope).val)
        return self.expr.evaluate(scope)


class Read:
    def __init__(self, name):
        self.name = name

    def evaluate(self, scope):
        Num = Number(int(input()))
        scope[self.name] = Num
        return scope[self.name]


class FunctionCall:
    def __init__(self, fun_expr, args):
        self.fun_expr = fun_expr
        self.args = args

    def evaluate(self, scope):
        function = self.fun_expr.evaluate(scope)
        new_args = []
        for op in self.args:
            new_args.append(op)
            new_args.append(op.evaluate(scope))
        call_scope = Scope(scope)
        for op, arg in new_args:
            call_scope[op] = arg
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
        if self.op == '+':
            return Number(a + b)
        if self.op == '-':
            return Number(a - b)
        if self.op == '*':
            return Number(a * b)
        if self.op == '/':
            return Number(a // b)
        if self.op == '%':
            return Number(a % b)
        if self.op == '==':
            return Number(a == b)
        if self.op == '!=':
            return Number(a != b)
        if self.op == '<':
            return Number(a < b)
        if self.op == '>':
            return Number(a > b)
        if self.op == '<=':
            return Number(a <= b)
        if self.op == '>=':
            return Number(a >= b)
        if self.op == '&&':
            if a == Number(0) or b == Number(0):
                return Number(0)
            else:
                return Number(1)
        if self.op == '||':
            if a == Number(0) and b == Number(0):
                return Number(0)
            else:
                return Number(1)


class UnaryOperation:
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr

    def evaluate(self, scope):
        a = self.expr.evaluate(scope).val
        if self.op == '-':
            return Number(-a)
        if self.op == '!':
            if a == Number(0):
                return Number(1)
            else:
                return Number(0)


if __name__ == "__main__":
    parent = Scope()
    r = Read(1)
    r.evaluate(parent)
    parent[2] = Number(1)
    parent[3] = Number(6)
    parent[4] = Number(7)
    con1 = BinaryOperation(parent[1], '>', parent[1])
    BO1 = BinaryOperation(parent[1], '*', parent[2])
    BO2 = BinaryOperation(parent[3], '+', parent[4])
    UO1 = UnaryOperation('!', BO2)
    print(UO1.evaluate(parent).val)
    CON = Conditional(con1, [BO1], [BO2])
    print(CON.evaluate(parent).val)
    func = Function([parent[1], parent[2]], [BO1, BO2])
    f1 = FunctionDefinition('f1', func)
    f1.evaluate(parent)
    p = Print(parent['f1'])
    r=Reference('f1')
    print(r.evaluate(parent).evaluate(parent).val)
    p.evaluate(parent)

