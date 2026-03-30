from flask import Blueprint, render_template, request, redirect, url_for, flash
import re

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
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        course = request.form.get('course', '').strip()
        
        if not name or not email:
            flash('Name and Email are required!')
            return redirect(url_for('main.register'))
            
        if len(name) < 2:
            flash('Name must be at least 2 characters long!')
            return redirect(url_for('main.register'))
            
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash('Invalid email address!')
            return redirect(url_for('main.register'))
            
        if any(s['email'] == email for s in students.values()):
            flash('Email already registered!')
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
