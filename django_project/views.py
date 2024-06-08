import requests
from requests.exceptions import RequestException

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def home(request):
    # Using API for healthcare
    try:
        
        response=requests.get('https://healthcare.googleapis.com/$discovery/rest?version=v1beta1')
        response.raise_for_status()  # Check for HTTP request errors
        data = response.json()
        # Adjust the key extraction according to the actual structure of the response
        result = data.get("items", [{}])[0].get("repo", "No repo found")
    except (RequestException, ValueError, KeyError) as e:
        result = f"Error fetching data: {e}"

    return render(request, 'templates/index.html', {'result': result})

def submit_question(request):
    if request.method == 'POST':
        question = request.POST.get('question', '')
        if question:
            # Process the question here (e.g., save to database)
            return JsonResponse({'message': 'Question submitted successfully!'})
        else:
            return JsonResponse({'message': 'No question submitted.'}, status=400)
    return JsonResponse({'message': 'Invalid request'}, status=400)

# views.py
from django.shortcuts import render, redirect
from .forms import MyRegistrationForm

def register(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = MyRegistrationForm()
    return render(request, 'register.html', {'form': form})



# views.py
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Redirect to a success page.
            return redirect('dashboard')  # Redirect to the dashboard or any other page
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

# Community

def community(request):
    return render(request, 'community.html')


from django.shortcuts import render

def products(request):
    products = [
        {
            'name': 'Metformin',
            'price': '$29.99',
            'image': 'metformin.jpg',
        },
        {
            'name': 'Insulin Glargine',
            'price': '$39.99',
            'image': 'insulin_glargine.jpg',
        },
        {
            'name': 'Sitagliptin',
            'price': '$49.99',
            'image': 'sitagliptin.jpg',
        },
        {
            'name': 'Aspirin',
            'price': '$19.99',
            'image': 'aspirin.jpg',
        },
        {
            'name': 'Ibuprofen',
            'price': '$24.99',
            'image': 'ibuprofen.jpg',
        },
        {
            'name': 'Diclofenac',
            'price': '$34.99',
            'image': 'diclofenac.jpg',
        },
        {
            'name': 'Atorvastatin',
            'price': '$59.99',
            'image': 'atorvastatin.jpg',
        },
        {
            'name': 'Losartan',
            'price': '$54.99',
            'image': 'losartan.jpg',
        },
        {
            'name': 'Warfarin',
            'price': '$44.99',
            'image': 'warfarin.jpg',
        },
    ]
    return render(request, 'products.html', {'products': products})

#ABOUT_US Codes
def about_us(request):
    return render(request, 'about_us.html')

# DOCTOR_NURSE Codes ON VIEWS.PY

from django.shortcuts import render

# Define the view for the Doctors/Nurses page
def doctors_nurses(request):
    return render(request, 'doctors_nurses.html')

# VACANCIES CODES IN VIEWS
from django.shortcuts import render

def vacancies(request):
    return render(request, 'vacancies.html')

from django.shortcuts import render

def diabetes_guide(request):
    return render(request, 'diabetes_guide.html')

def heart_disease_guide(request):
    return render(request, 'heart_disease_guide.html')

def arthritis_guide(request):
    return render(request, 'arthritis_guide.html')

# EXPLORE GUIDE views.py
from django.shortcuts import render

def explore_guide(request):
    return render(request, 'explore_guide.html')
# Guides viwes.py
from django.shortcuts import render

def guides(request):
    return render(request, 'guides.html')

# Nutritional_guide viwes.py
from django.shortcuts import render

def nutrition_guide(request):
    return render(request, 'nutrition_guide.html')
# Exercises viwes.py
from django.shortcuts import render

def exercise_guide(request):
    return render(request, 'exercise_guide.html')

# Stress_management viwes.py
from django.shortcuts import render

def stress_management_guide(request):
    return render(request, 'stress_management_guide.html')




