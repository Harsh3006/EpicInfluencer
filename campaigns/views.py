from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.template import loader
from creators.models import User
from .models import Personal_Detail
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'campaigns/home.html')

@login_required
def personal(request):
    user = request.user
    if request.method == "POST":
        email = request.POST['email']
        dob = request.POST['dob']
        language = request.POST['language']
        gender = request.POST['gender']
        fname = request.POST['fname']
        lname = request.POST['lname']
        phoneNumber = request.POST['phoneNumber']
        address = request.POST['address']
        address2 = request.POST['address2']
        postalCode = request.POST['postalCode']
        city = request.POST['city']
        state = request.POST['state']
        department = request.POST['department']
        country = request.POST['country']
        if Personal_Detail.objects.filter(email=user).exists():
            user.email = email
            user.dob = dob
            user.country = country
            user.save()
            detail = Personal_Detail.objects.update(email=user, language=language, gender=gender, 
                                                fname=fname, lname=lname, phoneNumber=phoneNumber, 
                                                address=address, address2=address2, postalCode=postalCode, city=city,
                                                state=state, department=department)                                              
        else:                                                
            detail = Personal_Detail.objects.create(email=user, language=language, gender=gender, 
                                                    fname=fname, lname=lname, phoneNumber=phoneNumber, 
                                                    address=address, address2=address2, postalCode=postalCode, city=city,
                                                    state=state, department=department)
            detail.save()

        messages.success(request, 'Profile Updated')
        return redirect('personal')
    else:
        if Personal_Detail.objects.filter(email= user).exists():
            detail = Personal_Detail.objects.get(email=user)
            context = {
                'email': user.email,
                'dob': str(user.dob),
                'fname': detail.fname,
                'lname': detail.lname,
                'phoneNumber': detail.phoneNumber,
                'address': detail.address,
                'address2': detail.address2,
                'postalCode': detail.postalCode,
                'city': detail.city,
                'state': detail.state,
                'department': detail.department
            }
            return render(request, 'campaigns/personal.html', context)    
        else:
            context={
                'email': user.email,
                'dob': str(user.dob)
            }
            return render(request, 'campaigns/personal.html', context)                                        

@login_required
def accounts(request):
    return render(request, 'campaigns/accounts.html')

@login_required
def change_password(request):
    user = request.user
    if request.method == "POST":
        old_password = request.POST['password']
        if user.check_password(old_password):
            new_password = request.POST['password2']
            confirm_password = request.POST['confirmpassword']
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Your Password is changed')
                return redirect('change-password')
            else:
                messages.error(request, 'New Password and Confirmation Password not matching')
                return redirect('change-password')
        else:
            messages.error(request, 'Your current password is inavlid')
            return redirect('change-password')
    else:
        return render(request, 'campaigns/change-password.html')
