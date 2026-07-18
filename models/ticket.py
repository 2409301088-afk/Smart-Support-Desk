class Ticket:

    def __init__(self, ticket_id, title, description, created_by):

        self.ticket_id = ticket_id
        self.title = title
        self.description = description
        self.status = "Open"
        self.priority = "Medium"

        self.created_by = created_by
        self.assigned_to = None

    def __str__(self):
        return f"{self.ticket_id} | {self.title} | {self.priority}"