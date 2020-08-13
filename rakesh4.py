class A:
    def __init__(self):
        self.var="Hello! By class A"
        
class B(A):
    def __init__(self):
        self.var="Hello! By class B"
        super().__init__()

a = A()
b = B()
print(b.var)
print(a.var)