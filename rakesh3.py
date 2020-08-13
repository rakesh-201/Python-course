class ElectronicDevices:
    name = "ElectronicDevices"
    @staticmethod
    def intro():
        print(f"This is a class of {name}")

class PocketGadgets(ElectronicDevices):
    name = "PocketGadgets"
    @staticmethod
    def intro():
        print(f"This is a class of {name}")

class Mobile(PocketGadgets):
    name = "Mobile"
    @staticmethod
    def intro():
        print(f"This is a class of samsung") 

samsung = Mobile()
print(samsung.name)
print(samsung.intro())