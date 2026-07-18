# 🎫 Smart Support Desk

A Python-based AI-powered Support Ticket Management System built using Object-Oriented Programming (OOP), Streamlit, JSON, Logging, Exception Handling, and Hugging Face AI.

---

## 📌 Project Overview

Smart Support Desk is a ticket management system that helps customers raise support tickets and allows support agents to manage them efficiently.

The project automatically assigns ticket priority using AI (Hugging Face API) with a rule-based fallback system. It also provides a simple Streamlit web interface for managing tickets.

---

## ✨ Features

- 👤 Add Support Agents
- 👥 Create Customers
- 🎫 Raise Support Tickets
- 🤖 AI-based Ticket Priority Classification
- 🔄 Rule-Based Priority Fallback
- 👨‍💻 Assign Tickets to Agents
- ✅ Close Tickets
- 📋 View All Tickets
- 💾 Save Ticket Data to JSON
- 📂 Load Saved Ticket Data
- 📝 Logging Support
- ⚠️ Custom Exception Handling
- ⏱️ Context Manager Example
- 📢 Notifications using *args and **kwargs
- 🌐 Streamlit User Interface

---

## 🛠️ Technologies Used

- Python 3
- Streamlit
- Requests
- Python-dotenv
- JSON
- Logging
- Hugging Face Inference API
- Object-Oriented Programming (OOP)

---

## 📁 Project Structure

```
Smart-Support-Desk/
│
├── data/
│   ├── support.json
│   └── support_desk.log
│
├── exceptions/
│   └── custom_exceptions.py
│
├── models/
│   ├── person.py
│   ├── customer.py
│   ├── agent.py
│   └── ticket.py
│
├── services/
│   ├── support_desk.py
│   └── ai_classifier.py
│
├── utils/
│   ├── logger.py
│   ├── decorators.py
│   ├── context_manager.py
│   └── notifications.py
│
├── main.py
├── ui.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/2409301088-afk/Smart-Support-Desk.git
```

Move into the project folder:

```bash
cd Smart-Support-Desk
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

Example:

```
HF_TOKEN=your_huggingface_api_token
```

---

## ▶️ Run the Console Application

```bash
python main.py
```

---

## 🌐 Run the Streamlit Application

```bash
streamlit run ui.py
```

---

## 🧠 AI Ticket Classification

The project uses the Hugging Face Inference API to classify ticket priorities.

Priority Levels:

- Urgent
- High
- Medium
- Low

If the API is unavailable, the application automatically switches to the built-in rule-based classifier.

---

## 📄 Output

The application stores ticket information in:

```
data/support.json
```

Logs are stored in:

```
data/support_desk.log
```

---

## 📚 OOP Concepts Used

- Classes and Objects
- Inheritance
- Encapsulation
- Polymorphism
- Exception Handling
- Decorators
- Context Managers
- Generators

---

## 🚀 Future Improvements

- Email Notifications
- Ticket Search
- Admin Login
- Dashboard Analytics
- Database Integration (MySQL)
- User Authentication
- Charts and Reports

---

## 👩‍💻 Author

**Muskan**

Python Developer | AI & Machine Learning Student

---

## 📜 License

This project is created for educational and learning purposes.
