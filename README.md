Integrated Child Development Services (ICDS) Management System 👶⚕️

The ICDS Management System is a comprehensive, multi-stakeholder platform designed to centralize and optimize maternal and child health and nutrition services. It provides critical tracking and resource management capabilities for administrative staff, healthcare workers, and users across web and mobile interfaces.

✨ Key Project Highlights

Multi-Role Access Control: Implemented a robust access control system across five distinct user roles (Admin, Anganwadi, Healthcare, Hospital, and Mobile User) to ensure data segregation and role-specific functionality.

RESTful API Design: Developed a scalable and secure RESTful API using Flask (Python) to facilitate seamless, real-time data exchange between the server, web portals, and external Java-based mobile clients.

Full-Cycle Health Management: Centralized critical services, including maternal check-up scheduling, child vaccination tracking, nutrition program monitoring, and postnatal care coordination.

Custom SQL Integration: Managed data integrity and complex querying logic by writing and optimizing custom SQL queries against the MySQL database.

⚙️ Architecture & Core Features

1. Centralized Stakeholder Management

The application provides unique portals tailored to institutional needs:

Admin Section 🛠️: Full oversight of operations, managing user roles, institution hierarchy (Anganwadi/Hospitals), and generating performance reports and analytics.

Healthcare Center 🏥 & Hospital 🏨: Managed appointment scheduling, maintained longitudinal health records for mothers and infants, and coordinated postnatal care and emergency data management.

Anganwadi Section 🏫: Dedicated tracking of nutrition program participation, monitoring child development milestones, and disseminating educational resources to mothers.

2. User Experience (Web & Mobile)

Personalized Data Access: Users can access their individual healthcare data (health progress, nutrition tracking, check-up history) via dedicated web and mobile interfaces.

Automated Notifications: Implemented a notification system for timely reminders regarding vaccination schedules, upcoming appointments, and essential health tips.

💻 Technical Stack

This project was built leveraging a Python back-end for core stability and a multi-platform access strategy.

Component

Technology

Role in the Project

Back-End

Flask (Python)

Core application logic, request handling, and business rule enforcement.

API

RESTful Services

Defined clear endpoints for data retrieval and submission for all web and mobile clients.

Database

MySQL (via WAMP)

Persistent storage for all user, health, and operational data.

SQL Management

Direct SQL Implementation

Utilized Python's database connector to execute custom SQL queries for complex data manipulation.

Web Front-End

HTML, CSS, Bootstrap, JavaScript

Responsive and user-friendly interface for administrative and institutional portals.

Mobile Client

Java (Android) & Volley

Developed the mobile application for user data access and notifications.

🏃 How to Run the Project Locally

Follow these steps to set up the ICDS Management System on your local machine:

1. Clone the Repository and Set Up Python Environment

git clone [Your GitHub URL Here]
cd ICDS-Management-System-Repo # Replace with your actual folder name
# Assuming you use a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt


2. Database Setup (WAMP/MySQL)

Start WAMP Services: Ensure the Apache and MySQL services are running via the WAMP control panel.

Create Database: Log in to MySQL (e.g., via phpMyAdmin) and create a database named icds_db.

Configure Connection: Update the MySQL connection credentials in your Flask application's configuration file (e.g., config.py or directly in app.py).

Initialize Schema: Run the database initialization script to create the necessary tables:

python init_db.py # Or whatever your script is named (e.g., python db_setup.py)


3. Run the Flask Server

python app.py


Access: The web application for the Admin/Anganwadi portals will be available at http://127.0.0.1:5000/.
