from django.shortcuts import render, redirect
from nutricalc.forms import UserLoginForm, UserSignupForm
from .models import *
from .forms import *
from django.views.generic import CreateView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
import json
from datetime import datetime


def index(request):
        user = request.user
        if user.is_anonymous: 
            #if user isn't logged in  
            return render(request, 'index.html')
        
        elif user.is_member:
                # user is member
            return render(request, 'index.html')
       
        else:
            # not logged in at all 
            # either show generic landing page 
            # or redirect to login 
            return render(request, 'index.html')


class UserSignupView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'user_signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')
    


class UserLoginView(LoginView):
    template_name='login.html'


def logout_user(request):
    logout(request)
    return redirect("/")

# BMI Calculator view to calculate BMI
@login_required
def bmi_calculator(request):

    if request.method == "POST":

        weight = request.POST.get("weight")  # Get the weight from the POST data
        height = request.POST.get("height")  # Get the height from the POST data

        if weight and height:
            weight = float(weight)
            height = float(height) / 100  # Convert height to meters

            bmi = weight / (height ** 2)  # Calculate BMI

            # Determine BMI category
            if bmi < 18.5:
                bmi_category = "Underweight"
            elif 18.5 <= bmi < 24.9:
                bmi_category = "Healthy weight"
            elif 25 <= bmi < 29.9:
                bmi_category = "Overweight"
            else:
                bmi_category = "Obesity"

            # Calculate Ideal Body Weight (IBW) for BMI 20, 22.5, and 25
            ibw_20 = round(20 * (height ** 2), 1)
            ibw_22_5 = round(22.5 * (height ** 2), 1)
            ibw_25 = round(25 * (height ** 2), 1)

            context = {
                'bmi': round(bmi, 1),  # Rounded BMI
                'bmi_category': bmi_category,
                'weight': weight,
                'height': height * 100,  # Convert height back to centimeters for display
                'ibw_20': ibw_20,  # IBW for BMI 20
                'ibw_22_5': ibw_22_5,  # IBW for BMI 22.5
                'ibw_25': ibw_25  # IBW for BMI 25
            }
            return render(request, 'bmi.html', context)  # Render the template with context

    return render(request, 'bmi.html')  # Render the BMI template without calculations initially


# 🔹 Energy Calculations
def eer_calculator(request):
    return render(request, 'eer_calculator.html')

def penn_state_calculator(request):
    return render(request, 'penn_state_calculator.html')

def modified_penn_state_calculator(request):
    return render(request, 'modified_penn_state_calculator.html')

# 🔹 Protein Requirements
def protein_req(request):
    return render(request, 'protein_req.html')

# 🔹 Nutrition Tracking
def nutrition_received(request):
    return render(request, 'nutrition_received.html')

# 🔹 Patient & Consultation Tracking
def productivity_tracker(request):
    if request.method == 'POST':
        # Get form data from the request
        patient_name = request.POST['patient_name']
        mrn = request.POST['mrn']
        consult_type = request.POST['consult_type']
        start_time = datetime.fromisoformat(request.POST['start_time'])
        end_time = datetime.fromisoformat(request.POST['end_time'])

        # Calculate consultation duration in minutes
        duration = (end_time - start_time).total_seconds() / 60

        # Save consultation in database
        Consultation.objects.create(
            patient_name=patient_name,
            mrn=mrn,
            consult_type=consult_type,
            start_time=start_time,
            end_time=end_time,
            duration=int(duration)
        )

        return redirect('productivity_tracker')  # Refresh page after submission

    # Retrieve all logged consultations
    consultations = Consultation.objects.all().order_by('-start_time')

    return render(request, 'productivity_tracker.html', {'consultations': consultations})

# 🔹 Feed Calculation
def feed_calculator(request):
    return render(request, 'feed_calculator.html')