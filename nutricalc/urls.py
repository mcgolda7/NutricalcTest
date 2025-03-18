from django.contrib import admin
from django.urls import path
from nutricalc import views
from nutricalc.forms import UserLoginForm, UserSignupForm


urlpatterns = [
    # 🔹 Home Section
    path('', views.index, name='index'),  # Home page
    path('bmi/', views.bmi_calculator, name='bmi'),

    # 🔹 Authentication
    path('register/', views.UserSignupView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm)),
    path('logout/', views.logout_user, name="logout"),

    # 🔹 Energy Calculations
    path('eer/', views.eer_calculator, name='eer_calculator'),
    path('penn_state/', views.penn_state_calculator, name='penn_state_calculator'),
    path('modified_penn_state/', views.modified_penn_state_calculator, name='modified_penn_state_calculator'),

    # 🔹 Protein Calculations
    path('protein_req/', views.protein_req, name='protein_req'),

    # 🔹 Nutrition Tracking
    path('nutrition-received/', views.nutrition_received, name='nutrition_received'),

    # 🔹 Patient & Consult Tracking
    path('productivity-tracker/', views.productivity_tracker, name='productivity_tracker'),

    # 🔹 Feed Calculation
    path('feed-calculator/', views.feed_calculator, name='feed_calculator'),
]