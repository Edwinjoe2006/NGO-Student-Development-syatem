
# 🎓 NGO Student Management System

A web-based student management system developed to help NGOs efficiently manage student information, academic details, skills, and career goals in a centralized platform.

## 📌 About the Project

The NGO Student Management System provides an easy and organized way for NGOs to maintain student records digitally.

Instead of maintaining student information manually, administrators can use this system to add, view, update, delete, and manage student information through a web interface.

The system also provides career-goal-based student analysis to help understand students' future career interests.

## 🎯 Objectives

- Digitally manage student records
- Reduce manual paperwork
- Store student information in a centralized database
- Manage academic and personal information
- Track student skills and interests
- Track student career goals
- Search and manage student records easily
- Provide useful student statistics
- Help NGOs monitor student development

## 🚀 Features

### 👨‍🎓 Student Management

- Add new students
- View student details
- Update student information
- Delete student records
- Search student records
- Manage student profiles

### 📚 Academic Information

The system can store information such as:

- Student name
- Date of birth
- Gender
- Email
- Phone number
- Educational qualification
- Skills
- Interests
- Career goal

### 🎯 Career Goal Management

The system stores and analyzes students' career goals.

Examples:

- Software Developer
- Web Developer
- Data Scientist
- AI/ML Engineer
- Government Jobs
- Higher Studies
- Entrepreneur

Career goals can be analyzed using SQL queries to understand the interests of students.

### 📊 Dashboard

The dashboard provides useful information such as:

- Total number of students
- Student records
- Career goal information
- Student statistics
- Management information

### 🔍 Search

Administrators can search for student records quickly instead of manually checking every record.

### 🗄️ Database Management

Student information is stored in a database and can be:

- Created
- Read
- Updated
- Deleted

## 🏗️ System Architecture

```text
                 Admin
                   |
                   v
            Web Interface
          HTML / CSS / JS
                   |
                   v
            Flask Backend
                Python
                   |
                   v
              Database
               SQLite
                   |
                   v
          Student Information

🛠️ Technologies Used

Frontend

HTML5

CSS3

JavaScript


Backend

Python

Flask


Database

SQLite


Development Tools

Visual Studio Code

Git

GitHub


📂 Project Structure

student_management_pro/
│
├── app.py
├── database.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── login.html
│   ├── students.html
│   └── add_student.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│
└── database/
    └── students.db

> The exact project structure may vary depending on the current version of the application.



⚙️ Installation

1. Clone the Repository

git clone https://github.com/Edwinjoe2006/NGO-Student-Development-syatem.git

2. Open the Project

cd NGO-Student-Development-syatem

3. Create a Virtual Environment

python -m venv venv

4. Activate the Virtual Environment

For Windows:

venv\Scripts\activate

For Linux/macOS:

source venv/bin/activate

5. Install Dependencies

pip install -r requirements.txt

If requirements.txt is not available:

pip install flask

▶️ Run the Application

Start the Flask application:

python app.py

Then open your browser and visit:

http://127.0.0.1:5000

📊 Career Goal Analysis

The application can use SQL queries to analyze students based on their career goals.

Example:

SELECT career_goal, COUNT(*)
FROM students
GROUP BY career_goal;

This helps the NGO understand the career interests of students.

🗃️ Database Information

The system uses SQLite to store student information.

Typical student fields include:

Field	Description

Student ID	Unique student ID
Name	Student name
Date of Birth	Student date of birth
Gender	Student gender
Email	Student email
Phone	Student contact number
Education	Educational qualification
Skills	Student skills
Career Goal	Student's career goal


🔐 Security

The application should follow basic security practices:

Validate user input

Protect administrator access

Do not store passwords directly in source code

Do not upload sensitive information to GitHub

Do not upload .env files

Keep API keys and credentials private


Recommended .gitignore:

.env
venv/
.venv/
__pycache__/
*.pyc

🧪 Testing

The application can be tested for:

Student registration

Student viewing

Student updating

Student deletion

Student searching

Database operations

Login functionality

Dashboard functionality

Form validation


🔮 Future Enhancements

The project can be improved by adding:

📱 Mobile responsive design

📊 Advanced student analytics

📈 Interactive charts

📄 PDF report generation

📊 Excel report generation

📧 Email notifications

🔑 Role-based authentication

☁️ Cloud deployment

🤖 AI-based career recommendations

📚 Course recommendations

💼 Internship recommendations

📱 Mobile application


🌟 Advantages

Easy student management

Reduces paperwork

Centralized student database

Fast student record searching

Easy data management

Career goal analysis

User-friendly interface

Can be extended with AI and analytics


🎓 Project Information

Project Name: NGO Student Management System

Domain: Web Application Development

Purpose: Student Information and Development Management

Project Type: Academic / Educational Project

Backend: Python Flask

Database: SQLite

Frontend: HTML, CSS, JavaScript

👨‍💻 Developer

Edwin Joe.M

B.Tech Information Technology

📜 License

This project is developed for educational and learning purposes.

⭐ Support

If you find this project useful, please consider giving the repository a ⭐ on GitHub.


---

Thank you for visiting the NGO Student Management System! 🚀
