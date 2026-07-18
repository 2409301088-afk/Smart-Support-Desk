import streamlit as st

from services.support_desk import SupportDesk
from models.agent import Agent
from models.customer import Customer
from models.ticket import Ticket

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Smart Support Desk",
    page_icon="🎫",
    layout="wide"
)

st.title("🎫 Smart Support Desk")
st.write("AI Powered Ticket Management System")

# -----------------------------
# Session State
# -----------------------------
if "desk" not in st.session_state:
    st.session_state.desk = SupportDesk()

desk = st.session_state.desk

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Option",
    [
        "Add Agent",
        "Create Ticket",
        "View Tickets"
    ]
)

# ======================================
# ADD AGENT
# ======================================

if page == "Add Agent":

    st.header("➕ Add Agent")

    agent_name = st.text_input("Agent Name")

    agent_email = st.text_input("Agent Email")

    if st.button("Add Agent"):

        if agent_name and agent_email:

            agent = Agent(agent_name, agent_email)

            desk.add_agent(agent)

            st.success("Agent Added Successfully!")

        else:

            st.error("Please fill all fields.")

# ======================================
# CREATE TICKET
# ======================================

elif page == "Create Ticket":

    st.header("🎫 Raise New Ticket")

    customer_name = st.text_input("Customer Name")

    customer_email = st.text_input("Customer Email")

    ticket_id = st.text_input("Ticket ID")

    title = st.text_input("Ticket Title")

    description = st.text_area("Problem Description")

    if st.button("Create Ticket"):

        if (
            customer_name
            and customer_email
            and ticket_id
            and title
            and description
        ):

            customer = Customer(
                customer_name,
                customer_email
            )

            ticket = Ticket(
                ticket_id,
                title,
                description,
                customer
            )

            desk.create_ticket(ticket)

            st.success("Ticket Created Successfully!")

            st.write("### AI Assigned Priority")

            st.info(ticket.priority)

        else:

            st.error("Please fill all fields.")

# ======================================
# VIEW TICKETS
# ======================================

elif page == "View Tickets":

    st.header("📋 All Tickets")

    tickets = desk.get_all_tickets()

    if len(tickets) == 0:

        st.warning("No Tickets Available")

    else:

        for ticket in tickets:

            with st.expander(ticket.ticket_id):

                st.write(f"**Title:** {ticket.title}")

                st.write(f"**Description:** {ticket.description}")

                st.write(f"**Priority:** {ticket.priority}")

                st.write(f"**Status:** {ticket.status}")

                st.write(
                    f"**Customer:** {ticket.created_by.name}"
                )

                if ticket.assigned_to:

                    st.write(
                        f"**Assigned To:** {ticket.assigned_to.name}"
                    )

                else:

                    st.write("**Assigned To:** Not Assigned")


# ======================================
# ASSIGN TICKET
# ======================================

st.markdown("---")
st.header("👨‍💻 Assign Ticket")

tickets = desk.get_all_tickets()
agents = desk.get_all_agents()

if tickets and agents:

    ticket_ids = [ticket.ticket_id for ticket in tickets]

    agent_names = [agent.name for agent in agents]

    selected_ticket = st.selectbox(
        "Select Ticket",
        ticket_ids
    )

    selected_agent = st.selectbox(
        "Select Agent",
        agent_names
    )

    if st.button("Assign Ticket"):

        agent = None

        for a in agents:
            if a.name == selected_agent:
                agent = a
                break

        desk.assign_ticket(selected_ticket, agent)

        st.success("Ticket Assigned Successfully!")

else:

    st.warning("Please create Agents and Tickets first.")

# ======================================
# CLOSE TICKET
# ======================================

st.markdown("---")
st.header("✅ Close Ticket")

if tickets:

    close_ticket = st.selectbox(
        "Select Ticket to Close",
        [ticket.ticket_id for ticket in tickets],
        key="close"
    )

    if st.button("Close Ticket"):

        desk.close_ticket(close_ticket)

        st.success("Ticket Closed Successfully!")

else:

    st.warning("No Tickets Available.")

# ======================================
# SAVE DATA
# ======================================

st.markdown("---")
st.header("💾 Save Data")

if st.button("Save All Tickets"):

    desk.save_to_file()

    st.success("Data Saved Successfully!")

# ======================================
# LOAD DATA
# ======================================

st.markdown("---")
st.header("📂 Load Saved Data")

if st.button("Load Saved Tickets"):

    desk.load_from_file()

    st.success("Data Loaded Successfully! (Check Terminal Output)")

# ======================================
# PRIORITY DASHBOARD
# ======================================

st.markdown("---")
st.header("📊 Priority Dashboard")

if st.button("Show Priority Dashboard"):

    priority = {
        "Urgent": [],
        "High": [],
        "Medium": [],
        "Low": []
    }

    for ticket in desk.get_all_tickets():

        priority[ticket.priority].append(ticket)

    for level in ["Urgent", "High", "Medium", "Low"]:

        st.subheader(level)

        if len(priority[level]) == 0:

            st.write("No Tickets")

        else:

            for ticket in priority[level]:

                st.write(
                    f"{ticket.ticket_id} - {ticket.title}"
                )

# ======================================
# PENDING TICKETS
# ======================================

st.markdown("---")
st.header("🕒 Pending Tickets")

pending = list(desk.pending_tickets())

if len(pending) == 0:

    st.success("No Pending Tickets")

else:

    for ticket in pending:

        st.write(
            f"{ticket.ticket_id} | {ticket.title} | {ticket.priority}"
        )

# ======================================
# FOOTER
# ======================================

st.markdown("---")

st.caption("Smart Support Desk | Python OOP + AI + Streamlit")