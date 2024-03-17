from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login , logout , authenticate
from random import *
from django.core.mail import send_mail
from .models import StudentModel
from .forms import StudentForm

# Create your views here.


def uhome(request) :
	if request.user.is_authenticated : 
		return render(request , "home.html")
	else :
		return redirect("ulogin")

def ulogin(request) :
	if request.user.is_authenticated : 
		return redirect("uhome")
	elif request.method == "POST" :
		un = request.POST.get("un")
		pw = request.POST.get("pw1")
		usr = authenticate(username = un , password = pw)
		if usr is None :
			return render(request , "login.html" , {"msg" : "Invalid Login"})
		else :
			login(request , usr)
			return redirect("uhome")
		
	else :
		return render(request , "login.html")

def usignup(request) :
	if request.user.is_authenticated :
		return redirect("uhome")
	elif request.method == "POST" :
		un = request.POST.get("un")
		try :
			usr = User.objects.get(username = un)
			return render(request , "signup.html" , {"msg" : "email already exists"})
		except User.DoesNotExist :
			text = "0123456789"
			pw = ""
			for i in range(4) :
				r = randrange(len(text))
				pw = pw + text[r]
			subject = "Password From Vinit To Validate in Student Management System"
			text = "Your Password is "  + str(pw)
			from_email = "gurupalekar143@gmail.com"
			to_email = [str(un)]
			send_mail(subject , text , from_email , to_email)
			usr = User.objects.create_user(username = un , password = pw)
			usr.save()
			return redirect("ulogin")
	else :
		return render(request , "signup.html")


def usnp(request) :
	if request.user.is_authenticated : 
		return redirect("uhome")
	elif request.method == "POST" :
		un = request.POST.get("un")
		try :
			usr = User.objects.get(username = un)
			text = "0123456789"
			pw = ""
			for i in range(4) :
				r = randrange(len(text))
				pw = pw + text[r]
			subject = "Password From Vinit To Validate in Student Management System"
			text = "Your Password is "  + str(pw)
			from_email = "gurupalekar143@gmail.com"
			to_email = [str(un)]
			send_mail(subject , text , from_email , to_email)
			usr = User.objects.get(username = un)
			usr.set_password(pw)
			usr.save()
			return redirect("ulogin")
		except User.DoesNotExist :
			return render(request , "snp.html" , {"msg" : "Email Not Registered"})
	else :
		return render(request, "snp.html")

def ulogout(request) :
	logout(request)
	return redirect("ulogin")

def create(request) :
	if request.method == "POST" :
		data = StudentForm(request.POST , request.FILES)
		if data.is_valid() :
			data.save()
			msg = "Data uploaded"
			fm = StudentForm()
			return render(request , "create.html" , {"fm" : fm , "msg" : msg})
		else :
			msg = "Check errors"
			return render(request , "create.html" , {"fm" : data , "msg" : msg})
	else :
		fm = StudentForm()
		return render(request , "create.html" , {"fm" : fm })

def view(request) :
	data = StudentModel.objects.all()
	return render(request , "view.html" , {"data" : data})



def remove(request , id) :
	st = StudentModel.objects.get(roll_no = id)
	st.delete()
	return redirect("view")


	
