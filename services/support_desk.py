import json
from services.ai_classifier import ai_classifier
from models.ticket import Ticket
from exceptions.custom_exceptions import (
    TicketNotFoundError,
    AgentNotAvailableError
)
from utils.logger import logger


class SupportDesk:

    def __init__(self):
        self.tickets = {}
        self.agents = []

    # ----------------------------
    # Agent Functions
    # ----------------------------

    def add_agent(self, agent):
        self.agents.append(agent)
        logger.info(f"Agent Added : {agent.name}")

    def display_agents(self):

        if len(self.agents) == 0:
            print("\nNo Agents Available.\n")
            return

        print("\n========== Agents ==========\n")

        for agent in self.agents:
            print(f"Name  : {agent.name}")
            print(f"Email : {agent.email}")
            print(f"Assigned Tickets : {len(agent.assigned_tickets)}")
            print("-" * 40)

    # ----------------------------
    # Ticket Functions
    # ----------------------------

    def create_ticket(self, ticket):

        if ticket.ticket_id in self.tickets:
            print("Ticket ID already exists.")
            return

    # Automatically classify the priority
        ticket.priority = ai_classifier(ticket.description)
        self.tickets[ticket.ticket_id] = ticket

        logger.info(f"Ticket Created : {ticket.ticket_id}")

        print("Ticket Created Successfully.")

    def display_tickets(self):

        if len(self.tickets) == 0:
            print("\nNo Tickets Found.\n")
            return

        print("\n========== Tickets ==========\n")

        for ticket in self.tickets.values():

            print(f"Ticket ID    : {ticket.ticket_id}")
            print(f"Title        : {ticket.title}")
            print(f"Description  : {ticket.description}")
            print(f"Priority     : {ticket.priority}")
            print(f"Status       : {ticket.status}")
            print(f"Created By   : {ticket.created_by.name}")

            if ticket.assigned_to:
                print(f"Assigned To  : {ticket.assigned_to.name}")
            else:
                print("Assigned To  : Not Assigned")

            print("-" * 50)

    def get_all_tickets(self):
            return list(self.tickets.values())
    def get_all_agents(self):
            return self.agents

    # ----------------------------
    # Search Ticket
    # ----------------------------

    def search_ticket(self, ticket_id):

        if ticket_id not in self.tickets:
            raise TicketNotFoundError(
                f"Ticket {ticket_id} not found."
            )

        return self.tickets[ticket_id]

    # ----------------------------
    # Assign Ticket
    # ----------------------------

    def assign_ticket(self, ticket_id, agent):

        if agent not in self.agents:
            raise AgentNotAvailableError(
                "Agent not available."
            )

        ticket = self.search_ticket(ticket_id)

        ticket.assigned_to = agent

        agent.assign_ticket(ticket)

        logger.info(
            f"Ticket {ticket_id} Assigned To {agent.name}"
        )

        print("Ticket Assigned Successfully.")

    # ----------------------------
    # Close Ticket
    # ----------------------------

    def close_ticket(self, ticket_id):

        ticket = self.search_ticket(ticket_id)

        ticket.status = "Closed"

        logger.info(
            f"Ticket {ticket_id} Closed"
        )

        print("Ticket Closed Successfully.")

    # ----------------------------
    # Save Data
    # ----------------------------

    def save_to_file(self):

        data = []

        for ticket in self.tickets.values():

            data.append({

                "ticket_id": ticket.ticket_id,
                "title": ticket.title,
                "description": ticket.description,
                "status": ticket.status,
                "priority": ticket.priority,
                "created_by": ticket.created_by.name,

                "assigned_to":
                ticket.assigned_to.name
                if ticket.assigned_to
                else None

            })

        with open("data/support.json", "w") as file:

            json.dump(data, file, indent=4)

        logger.info("All Tickets Saved")

        print("Data Saved Successfully.")

    # ----------------------------
    # Load Data
    # ----------------------------

    def load_from_file(self):

        try:

            with open("data/support.json", "r") as file:

                data = json.load(file)

            print("\n========== Saved Tickets ==========\n")

            for ticket in data:

                print(ticket)

        except FileNotFoundError:

            print("support.json file not found.")

    # ----------------------------
    # Pending Tickets
    # ----------------------------

    def pending_tickets(self):

        for ticket in self.tickets.values():

            if ticket.status == "Open":
                yield ticket

    # ----------------------------
    # Priority Dashboard
    # ----------------------------

    def priority_dashboard(self):

        priority_order = {
            "Urgent": 4,
            "High": 3,
            "Medium": 2,
            "Low": 1
        }

        sorted_tickets = sorted(

            self.tickets.values(),

            key=lambda ticket:
            priority_order.get(ticket.priority, 0),

            reverse=True

        )

        print("\n========== Priority Dashboard ==========\n")

        for ticket in sorted_tickets:

            print(ticket)