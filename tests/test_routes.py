import pytest
from app import create_app
from app.routes import students

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False # If using WTForms
    
    with app.test_client() as client:
        # Clear students before each test
        students.clear()
        import app.routes
        app.routes.next_id = 1
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Student Portal' in response.data

def test_student_list_empty(client):
    response = client.get('/students')
    assert response.status_code == 200
    assert b'No students registered yet' in response.data

def test_student_registration(client):
    response = client.post('/register', data={
        'name': 'John Doe',
        'email': 'john@example.com',
        'course': 'Computer Science'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Student registered successfully!' in response.data
    assert b'John Doe' in response.data

def test_student_detail(client):
    # Register first
    client.post('/register', data={
        'name': 'Jane Doe',
        'email': 'jane@example.com',
        'course': 'Math'
    })
    
    response = client.get('/students/1')
    assert response.status_code == 200
    assert b'Jane Doe' in response.data
    assert b'Math' in response.data
