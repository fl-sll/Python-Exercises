class Object:
    def __init__(self):
        pass

class X(Object):
    def __init__(self):
        pass

class Y(Object):
    def __init__(self):
        pass

class Z(Object):
    def __init__(self):
        pass

class A(X, Y):
    def __init__(self):
        pass

class B(Y, Z):
    def __init__(self):
        pass

class M(A, B, Z):
    def __init__(self):
        pass