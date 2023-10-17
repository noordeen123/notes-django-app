from django.contrib.auth.models import User
from datetime import datetime
import pytest 


def test_home_view(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.context['time'] is not None
    assert response.context['time'].year == datetime.now().year
    assert 'SmartNotes!' in str(response.content)
    
#verifying that unauthorized user can access register page
def test_register_view(client):
    response = client.get('/register/')
    assert response.status_code == 200
    assert 'register.html' in response.template_name

#trying to access signup page when user is logged in
@pytest.mark.django_db
def test_register_view_authenticated(client):
    user = User.objects.create_user(username='testuser', password='12345')
    client.force_login(user)
    response = client.get('/register/', follow=True)
    assert response.status_code == 200
    print(response.template_name)


