from django.shortcuts import render
from .models import Student
from faker import Faker


def dummy(request):
    fake = Faker()
    
    for i in range(100):
        first_name = fake.first_name()
        last_name = fake.last_name()
        date_of_birth = fake.date()
        gender = 'Male'
        enrollment_date = fake.date()
        email = fake.email()
        phone_number = fake.msisdn()
        address = fake.address()
        Student.objects.create(first_name = first_name, last_name = last_name, date_of_birth = date_of_birth, gender = gender, enrollment_date = enrollment_date, email = email, phone_number = phone_number, address = address)
    
    return render(request,'response.html')
