class Person:
    def __init__(self, full_name=""):
        self.full_name = full_name

    # def __str__(self):
    #     return f"{self.full_name} is a {self.__class__}"

josh = Person("Josh Dalton")
print(josh)
print(josh.full_name)
heather = Person("Heather Purser")
print(heather)
print(heather.full_name)