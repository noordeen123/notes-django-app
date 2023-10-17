import pytest
from django.contrib.auth.models import User
from notes.models import notes



@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='12345')
@pytest.fixture
def user2():
    return User.objects.create_user(username='testuser2', password='12345')

#verifying that when user creates a note its visible in his notes and database
@pytest.mark.django_db
def test_list(client):
    user = User.objects.create_user(username='testuser', password='12345')
    client.force_login(user)
    note = notes.objects.create(title='test title', text='test', user=user)
    note2 = notes.objects.create(title='test title2', text='test2', user=user)
    response = client.get('/smart/notes/')
    assert response.status_code == 200
    con = str(response.content)
    assert 'test title' in con
    assert 'test title2' in con
    assert 2 == con.count('<h3>')
    
#verifying that one user can see only his notes
#verifying that another user note is not appearing in logged in user's notes
@pytest.mark.django_db
def test_list_view(client, user, user2):
    note = notes.objects.create(title='test title', text='test', user=user)
    note2 = notes.objects.create(title='test title2', text='test2', user=user2)
    client.force_login(user)
    response = client.get('/smart/notes/')
    assert response.status_code == 200
    con = str(response.content)
    assert 'test title' in con
    assert 'test title2' not in con

    




