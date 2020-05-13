from django.shortcuts import render
from  user_form2.forms import UserForm,UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
 # Create your views here.
def index(request):
     return render(request,'user_form2/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    
@login_required
def special(request):
    return Httpresponse("you are logged in...")


def register(request):
        registered=False

        if request.method=="POST":
            users_form=UserForm(data=request.POST)
            profile_form=UserProfileInfoForm(data=request.POST)
           
            if users_form.is_valid() and profile_form.is_valid():

                user=users_form.save()
                user.set_password(user.password)
                user.save()

                profile=profile_form.save(commit=False)
                profile.user=user

                if 'profile_pics' in request.FILES:
                    profile.profile_pics = request.FILES['profile_pics']


                profile.save()

                registered=True
            else:
                print(users_form.errors,profile_form.errors)

        else:
            users_form=UserForm()
            profile_form=UserProfileInfoForm()
        
        return render(request,'user_form2/register.html',{'users_form':users_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method=="POST":
         username=request.POST.get('username')
         password=request.POST.get('password')
         user=authenticate(username=username,password=password)
         if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse(index))
            else:
                return HttpResponse("Account not active")
         
         else:
            print("someone try to login and failed")
            print("username:{} and password:{}".format(username,password))
            return HttpResponse("invalid login details")


    else:
        return render(request,'user_form2/login.html',{})

