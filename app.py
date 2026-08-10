from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="airline@123",
    database="student_development"
)
@app.route('/')
def start():
    return redirect('/dashboard')

@app.route('/login')
def login_page():
    return render_template("login.html")
@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    cursor = db.cursor(dictionary=True,buffered=True)

    cursor.execute(
        """
        SELECT *
        FROM admins
        WHERE username=%s
        AND password=%s
        """,
        (username,password)
    )

    admin = cursor.fetchone()

    if admin:
        return redirect('/dashboard')

    return "Invalid Login"
# =========================
# DASHBOARD
# =========================

@app.route('/dashboard')
def home():

    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM students WHERE gender='Male'")
    male = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM students WHERE gender='Female'")
    female = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM students WHERE difficult_subject='Maths'")
    help_needed = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM students WHERE internet_access='Yes'")
    internet = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM students WHERE smartphone_access='Yes'")
    smartphone = cursor.fetchone()[0]

    return render_template(
        "dashboard.html",
        total=total_students,
        male=male,
        female=female,
        help_needed=help_needed,
        internet=internet,
        smartphone=smartphone
    )

# =========================
# STUDENTS LIST
# =========================

@app.route('/students')
def students():

    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM students ORDER BY id"
    )

    data = cursor.fetchall()

    return render_template(
        "students.html",
        students=data
    )

# =========================
# SEARCH STUDENT
# =========================

@app.route('/search')
def search():

    name = request.args.get('name')

    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM students WHERE name LIKE %s",
        ('%' + name + '%',)
    )

    students = cursor.fetchall()

    return render_template(
        "students.html",
        students=students
    )

# =========================
# ADD STUDENT PAGE
# =========================

@app.route('/add_student')
def add_student():

    return render_template(
        "add_student.html"
    )

# =========================
# SAVE STUDENT
# =========================
@app.route('/edit/<int:id>')
def edit(id):

    cursor = db.cursor(dictionary=True)

    cursor.execute(
    "SELECT * FROM students WHERE id=%s",
    (id,)
    )

    student = cursor.fetchone()

    return render_template(
    "edit_student.html",
    student=student
    )

@app.route('/save_student', methods=['POST'])
def save_student():

    cursor = db.cursor()

    cursor.execute(
    """
    INSERT INTO students
    (
        name,
        age,
        gender,
        school,
        class_name,
        favorite_subject,
        difficult_subject,
        hobbies,
        career_goal,
        smartphone_access,
        internet_access,
        ngo_support
    )

    VALUES
    (
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
    )
    """,

    (
        request.form['name'],
        request.form['age'],
        request.form['gender'],
        request.form['school'],
        request.form['class_name'],
        request.form['favorite_subject'],
        request.form['difficult_subject'],
        request.form['hobbies'],
        request.form['career_goal'],
        request.form['smartphone_access'],
        request.form['internet_access'],
        request.form['ngo_support']
    ))

    db.commit()

    return redirect('/students')
@app.route('/update_student/<int:id>', methods=['POST'])
def update_student(id):

    cursor = db.cursor()

    cursor.execute("""
        UPDATE students
        SET
            name=%s,
            age=%s,
            gender=%s,
            school=%s,
            class_name=%s,
            favorite_subject=%s,
            difficult_subject=%s,
            hobbies=%s,
            career_goal=%s,
            smartphone_access=%s,
            internet_access=%s,
            ngo_support=%s
        WHERE id=%s
    """,
    (
        request.form['name'],
        request.form['age'],
        request.form['gender'],
        request.form['school'],
        request.form['class_name'],
        request.form['favorite_subject'],
        request.form['difficult_subject'],
        request.form['hobbies'],
        request.form['career_goal'],
        request.form['smartphone_access'],
        request.form['internet_access'],
        request.form['ngo_support'],
        id
    ))

    db.commit()

    return redirect('/students')
# =========================
# STUDENT PROFILE
# =========================

@app.route('/student/<int:id>')
def student(id):

    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM students WHERE id=%s",
        (id,)
    )

    student = cursor.fetchone()

    recommendations = []

    if student["favorite_subject"] == "Maths":
        recommendations.append(
            "Khan Academy Mathematics"
        )

    if student["career_goal"] == "Engineer":
        recommendations.extend([
            "Coding Basics",
            "Python Programming",
            "Aptitude Practice",
            "STEM Career Guidance"
        ])

    elif student["career_goal"] == "Doctor":
        recommendations.extend([
            "Biology Videos",
            "NEET Foundation",
            "Science Quiz"
        ])

    elif student["career_goal"] == "Teacher":
        recommendations.extend([
            "Communication Skills",
            "Public Speaking"
        ])

    elif student["career_goal"] == "Scientist":
        recommendations.extend([
            "Science Projects",
            "Research Basics"
        ])

    if student["smartphone_access"] == "No":
        recommendations.append(
            "Printed Worksheets"
        )

    if student["internet_access"] == "No":
        recommendations.append(
            "Volunteer Mentoring"
        )

    # =====================
    # RISK PREDICTION
    # =====================

    risk = "Low"

    if (
        student["internet_access"] == "No"
        and
        student["smartphone_access"] == "No"
        and
        student["difficult_subject"] == "Maths"
    ):
        risk = "High"

    elif (
        student["internet_access"] == "No"
        or
        student["smartphone_access"] == "No"
    ):
        risk = "Medium"

    return render_template(
        "student_profile.html",
        student=student,
        recommendation=recommendations,
        risk=risk
    )

# =========================
# ANALYTICS
# =========================

@app.route('/analytics')
def analytics():

    cursor = db.cursor()

    cursor.execute(
        """
        SELECT career_goal,
        COUNT(*)
        FROM students
        GROUP BY career_goal
        """
    )

    careers = cursor.fetchall()

    cursor.execute(
        """
        SELECT class_name,
        COUNT(*)
        FROM students
        GROUP BY class_name
        """
    )

    classes = cursor.fetchall()

    return render_template(
        "analytics.html",
        careers=careers,
        classes=classes
    )

# =========================
# RUN APP
# =========================

if __name__ == "__main__":
    app.run(debug=True)