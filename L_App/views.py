from django.shortcuts import render,HttpResponse,redirect
from.models import *


# Create your views here.
def demo(request):
    uname = request.session.get('uname', None)
    return render(request, 'base.html', {'uname': uname})


def signup(request):
    if request.method == 'POST':
        U_Name = request.POST['un']
        Email = request.POST['e']
        Password = request.POST['p']

        if not U_Name or not Email or not Password:
            error_message = 'All fields are required!'
            return render(request, 'signup.html', {'error': error_message})
        
        if UserId.objects.filter(U_Name=U_Name).exists():
            error_message1='Username already exists!'
            return render(request, 'signup.html', {'error1': error_message1})
        
        if UserId.objects.filter(Email=Email).exists():
            error_message2='Email already exists!'
            return render(request, 'signup.html', {'error2': error_message2})
        
        UserId.objects.create(U_Name=U_Name, Email=Email, Password=Password)
        return redirect('login') 
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['unm']
        password = request.POST['ps']
 


        if not username or not password:
            Error_message = 'All fields are required!'
            return render(request, 'login.html', {'ERROR': Error_message})
        try:
            user = UserId.objects.get(U_Name=username)
            if user.Password == password:
                request.session['user_id'] = user.id
                request.session['uname'] = user.U_Name
                return redirect('base') 
            else:
                return render(request, 'login.html', {'error': 'Incorrect password'})
        except UserId.DoesNotExist:
            return render(request, 'login.html', {'error': 'Username does not exist'})
    return render(request, 'login.html')
 