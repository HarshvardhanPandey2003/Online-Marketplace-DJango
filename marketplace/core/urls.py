from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'core' 
# We are assigning the name 'core' to the app 

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('about/',views.about, name='about'),
    path('logout/', views.logout_view, name='logout'),  
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
]

"""
1.) URL Pattern: 'login/'
This is the URL route for the login page. When a user visits /login/, Django will use this path configuration.

2.) View: auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm)
auth_views.LoginView: This is Django's built-in class-based view for handling user login.
.as_view(): This method converts the class-based view into a function-based view which Django can use to handle HTTP requests.

3.)Arguments to LoginView:
template_name='core/login.html': Specifies the template to render for the login page. In this case, it's pointing to login.html 
inside the core directory authentication_form=LoginForm: 
Specifies the custom form class to use for authentication. Here, LoginForm is your customized form that extends AuthenticationForm.
"""