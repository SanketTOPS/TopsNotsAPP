from django.shortcuts import render,redirect
from .forms import signupForm,updateForm,notesForm,contactForm
from .models import userSignup
from django.contrib.auth import logout
from django.core.mail import send_mail
from NotesApp import settings
import requests
import random

# Create your views here.

def index(request):
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("Signup Successfully!")
                
                #return redirect('notes')
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':

            unm=request.POST['username']
            pas=request.POST['password']

            uid=userSignup.objects.get(username=unm)
            print(uid.id)
            user=userSignup.objects.filter(username=unm,password=pas)
            if user:
                print("Login Successfully!")
                request.session['user']=unm
                request.session['userid']=uid.id

                #MSG Send
                otp=random.randint(111,999)
                url = "https://www.fast2sms.com/dev/bulkV2"
                querystring = {"authorization":"KEodGZf5czOn3eCxJPkWAFHQUYtS86Rbmrv1MyuViag4hs7N2DujvzKSw5MN9mRryb3LC4DsIHiWph78","variables_values":f"{otp}","route":"otp","numbers":"9328496808,9106761736,8849906669,8487886971"}
                headers = {
                    'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)

                #MAIL Send
                return redirect('notes')
            else:
                print("Error!Login fail....")
    return render(request,'index.html')

def notes(request):
    user=request.session.get('user')
    if request.method=='POST':
        newnotes=notesForm(request.POST,request.FILES)
        if newnotes.is_valid():
            newnotes.save()
            print("Notes Submitted!")
        else:
            print(newnotes.errors)
    return render(request,'notes.html',{'user':user})

def profile(request):
    user=request.session.get('user')
    uid=request.session.get('userid')
    cuser=userSignup.objects.get(id=uid)
    if request.method=='POST':
        updateProfile=updateForm(request.POST,instance=cuser)
        if updateProfile.is_valid():
            updateProfile.save()
            print("Your profile has been updated!")
        else:
            print(updateProfile.errors)
    return render(request,'profile.html',{'user':user,'uid':cuser})

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        newcontact=contactForm(request.POST)
        if newcontact.is_valid():
            newcontact.save()
            print("Your form has been submitted!")

            #send email
            sub="Thank you!"
            msg=f"Thank you for connecting with us!\nWe will assist you in near future.\n\nPlease contact us on \n+91 9724799469 | notesapp@support.com | Sanket Chauhan - Sr.Trainer | TOPS Tech"
            fromEmail=settings.EMAIL_HOST_USER
            toEmail=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=fromEmail,recipient_list=toEmail)
        else:
            print(newcontact.errors)
    return render(request,'contact.html')

def userlogout(request):
    logout(request)
    return redirect('/')
