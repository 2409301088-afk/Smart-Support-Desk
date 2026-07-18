from abc import ABC, abstractmethod

class TicketHandler(ABC):

    @abstractmethod
    def resolve(self, ticket):
        pass


class StandardHandler(TicketHandler):

    def resolve(self, ticket):
        ticket.status = "Resolved"
        print("Standard Ticket Resolved")


class UrgentHandler(TicketHandler):

    def resolve(self, ticket):
        ticket.status = "Resolved"
        print("Urgent Ticket Escalated & Resolved")