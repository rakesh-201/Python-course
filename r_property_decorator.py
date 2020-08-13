class A:
    def __init__(self):
        self.fname="rakesh"
        self.lname="rajpurohit"
        self.email=f"{self.fname}.{self.lname}@gmail.com"
    # @property
    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"
    @email.setter
    def email(self,string):
        z=string.split("@")
        self.fname=z.split(".")[0]
        self.lname=z.split(".")[1]
        return f"{self.fname}.{self.lname}@gmail.com"
    @email.setter
    def email(self):
        del self.fname

a=A()
print(a.email( ))