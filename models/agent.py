from models.person import Person

class Agent(Person):

    def __init__(self, name, email):
        super().__init__(name, email)
        self.assigned_tickets = []

    def assign_ticket(self, ticket):
        self.assigned_tickets.append(ticket)