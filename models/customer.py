from models.person import Person

class Customer(Person):

    def __init__(self, name, email):
        super().__init__(name, email)