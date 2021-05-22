from django.shortcuts import render
from . models import *
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from .models import *
from django.core.serializers import serialize
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request,"assignment/index.html")






def login_view(request):
	return render(request,"assignment/login_view.html")




def login_process(request):
	if request.method == "POST":
		username=request.POST["username"]
		password=request.POST["password"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse("assignment:dashboard_view"))
		else:
			return render(request, "assignment/login_view.html",{
				"msg": "Password or Username is not matched!!"
				})
	# return render(request,"Job/LR.html")



def signup_view(request):
    return render(request,"assignment/signup_view.html")



def signup_process(request):
	if request.method == "POST":
		username=request.POST["username"]
		password=request.POST["password"]
		email = request.POST["email"]
		rpassword = request.POST["rpassword"]
		name = request.POST['name']
		if password == rpassword:
			user = User.objects.create_user(username,email,password)
			user.first_name=name
			user.save()
			return render(request, "assignment/login_view.html")
		else:
			return render(request, "assignment/signup_view.html",{
				"msg":"Authenticate details is not correct, Please fill it correctly"
				})
	# return render(request, "Job/LR.html")


def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse("assignment:index"))
 

def dashboard_view(request):
	if request.method=='POST':
		pass
		# follower_min = int(request.POST["follower_min"])
		# follower_max = int(request.POST["follower_max"])
		# following_min = int(request.POST["following_min"])
		# following_max = int(request.POST["following_max"])
		# city = request.POST.getlist('city')
		# genre = request.POST["genre"]

		# get_acc=[]
		# token_acc=request.session['token']
		# for i in token_acc:
		# 	get_acc.append(Account.objects.get(pk=i))

		# filter_acc=[]
		# for i in get_acc:
		# 	# print(i)
		# 	if i.follower_count >= 10000*follower_min and i.follower_count <= 10000*follower_max and i.following_count >= 10000*following_min and i.following_count <= 10000*following_max:
		# 		if len(city)!=0:
		# 			if i.city in city:
		# 				filter_acc.append(i)
		# 		else:
		# 			filter_acc.append(i)

		# print(filter_acc)
		# get_token=[]
		# for i in filter_acc:
		# 	get_token.append(i.pk)
		# request.session['token']=get_token


		# page = request.GET.get('page', 1)

		# paginator = Paginator(filter_acc, 10)
		# try:
		# 	susers = paginator.page(page)
		# except PageNotAnInteger:
		# 	susers = paginator.page(1)
		# except EmptyPage:
		# 	susers = paginator.page(paginator.num_pages)
		

		# print(susers)
		# print(follower_min)
		# print(follower_max)
		# print(following_min)
		# print(following_max)
		# print(city)
		# print(genre)

		# return render(request,"assignment/dashboard_view.html",{
		# 	'users':filter_acc,
		# 	})

	else:
		accounts = Account.objects.all()
		session_acc=[]
		if session_acc:
			print("sjsjsjsjs")
		else:
			print("NOOOOOOOO")
		for i in accounts:
			session_acc.append(i.pk)
		request.session['token']=session_acc

		paginator = Paginator(accounts,10)

		try:
			page = int(request.GET.get('page',1))
		except:
			page=1

		try:
			posts = paginator.page(page)
		except(EmptyPage):
			posts = paginator.page(paginator,num_pages)

		# return render(request,'Job/home.html',{
		# 	'posts':posts,
		# 	})

		return render(request,"assignment/dashboard_view.html",{
			'posts':posts,
			})

		# page = request.GET.get('page', 1)

		# paginator = Paginator(accounts, 10)
		# try:
		# 	posts = paginator.page(page)
		# except PageNotAnInteger:
		# 	posts = paginator.page(1)
		# except EmptyPage:
		# 	posts = paginator.page(paginator.num_pages)
		# print(posts)
		# return render(request,"assignment/dashboard_view.html",{
		# 	'posts':posts,
		# 	})
	


def filtered_con(request):
	if request.method == 'POST':
		follower_min = int(request.POST.get('follower_min', False))
		follower_max = int(request.POST.get('follower_max', False))
		following_min = int(request.POST.get('following_min', False))
		following_max = int(request.POST.get('following_max', False))
		city = request.POST.getlist('city')
		genre = request.POST.get('genre', False)

		
			

		get_acc=[]
		token_acc=request.session['token']
		for i in token_acc:
			get_acc.append(Account.objects.get(pk=i))

		filter_acc=[]
		for i in get_acc:
			# print(i)
			if i.follower_count >= 10000*follower_min and i.follower_count <= 10000*follower_max and i.following_count >= 10000*following_min and i.following_count <= 10000*following_max:
				if str(genre)!="default":
					if i.genre==str(genre):
						if len(city)!=0:
							if i.city in city:
								filter_acc.append(i)
						else:
							filter_acc.append(i)
				else:
					if len(city)!=0:
						if i.city in city:
							filter_acc.append(i)
					else:
						filter_acc.append(i)

		print(filter_acc)
		get_token=[]
		for i in filter_acc:
			get_token.append(i.pk)
		request.session['token']=get_token

		page = request.GET.get('page', 1)

		paginator = Paginator(filter_acc, 10)
		try:
			susers = paginator.page(page)
		except PageNotAnInteger:
			susers = paginator.page(1)
		except EmptyPage:
			susers = paginator.page(paginator.num_pages)
		

		print(susers)
		print(request.session['token'])
		print(follower_min)
		print(follower_max)
		print(following_min)
		print(following_max)
		print(city)
		print(genre)
		return render(request,"assignment/filtered_con.html",{"posts":susers,})

	page = request.GET.get('page', 1)
	token_acc=request.session['token']
	original_acc=[]
	for i in token_acc:
		original_acc.append(Account.objects.get(pk=i))
	paginator = Paginator(original_acc, 10)
	try:
		susers = paginator.page(page)
	except PageNotAnInteger:
		susers = paginator.page(1)
	except EmptyPage:
		susers = paginator.page(paginator.num_pages)
	return render(request,"assignment/filtered_con.html",{
		"posts":susers,
		})


# def filter_it(request):
# 	# flag = request.GET['cnt']
# 	for i in rane(0,19):
# 		print("dhdvdeedwdhdwdhhqwehjqehj")
# 	return HttpResponse(request.POST['text'])
	# page = request.GET.get('page', 1)
	# token_acc=request.session['token']
	# original_acc=[]
	# for i in token_acc:
	# 	original_acc.append(Account.objects.get(pk=i))
	# paginator = Paginator(original_acc, 10)
	# try:
	# 	susers = paginator.page(page)
	# except PageNotAnInteger:
	# 	susers = paginator.page(1)
	# except EmptyPage:
	# 	susers = paginator.page(paginator.num_pages)
	# return render(request,"assignment/filtered_con.html",{
	# 	"posts":susers,
	# 	"flag":"0",
	# 	})
	# if request.method=='POST':
		# follower_min = int(request.POST["follower_min"])
		# follower_max = int(request.POST["follower_max"])
		# following_min = int(request.POST["following_min"])
		# following_max = int(request.POST["following_max"])
		# city = request.POST.getlist('city')
		# genre = request.POST["genre"]

		# get_acc=[]
		# token_acc=request.session['token']
		# for i in token_acc:
		# 	get_acc.append(Account.objects.get(pk=i))

		# filter_acc=[]
		# for i in get_acc:
		# 	# print(i)
		# 	if i.follower_count >= 10000*follower_min and i.follower_count <= 10000*follower_max and i.following_count >= 10000*following_min and i.following_count <= 10000*following_max:
		# 		if len(city)!=0:
		# 			if i.city in city:
		# 				filter_acc.append(i)
		# 		else:
		# 			filter_acc.append(i)

		# print(filter_acc)
		# get_token=[]
		# for i in filter_acc:
		# 	get_token.append(i.pk)
		# request.session['token']=get_token

		# sustain_acc=Account.objects.all()
		# page = request.GET.get('page', 1)

		# paginator = Paginator(sustain_acc, 10)
		# try:
		# 	susers = paginator.page(page)
		# except PageNotAnInteger:
		# 	susers = paginator.page(1)
		# except EmptyPage:
		# 	susers = paginator.page(paginator.num_pages)
		

		# print(susers)
		# print(follower_min)
		# print(follower_max)
		# print(following_min)
		# print(following_max)
		# print(city)
		# print(genre)
		
		# return render(request,"assignment/filtered_con.html",{
		# 	'posts':"",
		# 	})
	# return render(request,"assignment/signup_view.html")