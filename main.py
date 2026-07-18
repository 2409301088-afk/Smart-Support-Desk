from models.customer import Customer
from models.agent import Agent
from models.ticket import Ticket
from services.support_desk import SupportDesk

# Create Support Desk
desk = SupportDesk()

# Create Agents
agent1 = Agent("Rahul", "rahul@gmail.com")
agent2 = Agent("Priya", "priya@gmail.com")

desk.add_agent(agent1)
desk.add_agent(agent2)

# Create Customers
customer1 = Customer("Aman", "aman@gmail.com")
customer2 = Customer("Riya", "riya@gmail.com")

# Create Tickets
ticket1 = Ticket(
    "T101",
    "Server Issue",
    "Server is down after payment failed.",
    customer1
)

ticket2 = Ticket(
    "T102",
    "Login Error",
    "Unable to login into the application.",
    customer2
)

# Add Tickets
desk.create_ticket(ticket1)
print("Ticket Priority:", ticket1.priority)
desk.create_ticket(ticket2)

# Display Tickets
desk.display_tickets()

# Assign Tickets
desk.assign_ticket("T101", agent1)
desk.assign_ticket("T102", agent2)

# Close One Ticket
desk.close_ticket("T101")

# Save Data
desk.save_to_file()

# Load Data
desk.load_from_file()

# Show Priority Dashboard
desk.priority_dashboard()

