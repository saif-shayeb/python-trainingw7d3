from flask import Blueprint, render_template, request, redirect, url_for, flash

main = Blueprint('main', __name__)

# In-memory storage for students
students = {}
next_id = 1

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    global next_id
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        course = request.form.get('course')
        
        if not name or not email:
            flash('Name and Email are required!')
            return redirect(url_for('main.register'))
            
        student_id = next_id
        students[student_id] = {
            'id': student_id,
            'name': name,
            'email': email,
            'course': course
        }
        next_id += 1
        
        flash('Student registered successfully!')
        return redirect(url_for('main.student_list'))
        
    return render_template('register.html')

@main.route('/students', methods=['GET'])
def student_list():
    return render_template('list.html', students=students.values())

@main.route('/students/<int:student_id>', methods=['GET'])
def student_detail(student_id):
    student = students.get(student_id)
    if not student:
        flash('Student not found!')
        return redirect(url_for('main.student_list'))
    return render_template('detail.html', student=student)
