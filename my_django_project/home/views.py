from django.shortcuts import render,HttpResponse,redirect
from .models import Contact
from blogging.models import Post
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

def home(request):
    return render(request,'home/home.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request,'Please fill the form correctly')
        else:
            data=Contact(Name=name,Email=email,Phone_no=phone,Content=content)
            data.save()
            messages.success(request,'Your form has been successfully submitted')
    return render(request,'home/contact.html')

def about(request):    
    return render(request,'home/about.html')
    

def search(request):
    querry=request.GET['querry']
    if len(querry)>72:
        querry_post=Post.objects.none()
    else:
        querry_title=Post.objects.filter(Title__contains=querry)
        querry_content=Post.objects.filter(Content__icontains=querry)
        querry_author=Post.objects.filter(Author__contains=querry)
        querry_post=querry_title.union(querry_content,querry_author)
    if querry_post.count()==0:
        messages.warning(request,'No search results found. Please refine your query.')
    params={'querry_post':querry_post,'querry':querry}
    return render(request,'home/search.html',params)



def signup(request):
    if request.method=='POST':
        username=request.POST['Username']
        email = request.POST['Email']
        FirstName=request.POST['First_name']
        LastName=request.POST['Last_name']
        password1=request.POST['Password1']
        password2=request.POST['Password2']
        if len(username)<5:
            messages.error(request,'username must be above 5 character')
            return redirect('/')
        if not username.isalnum():
            messages.error(request,'Username should only contains letters and numbers')
            return redirect('/')
        if password1!=password2:
            messages.error(request,'Password didnot match,please input the right password')
            return redirect('/')
        my_user=User.objects.create_user(username,email,password1)
        my_user.first_name=FirstName
        my_user.last_name=LastName
        my_user.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('/')
    else:
        return HttpResponse('404 - Not found')

def user_login(request):
    if request.method=='POST':
        login_username=request.POST['Login_username']
        login_password=request.POST['Login_password']
        print(login_password,login_username)

        user=authenticate(username=login_username,password=login_password)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully Logged In')
            return redirect('/')
        else:
            messages.error(request,'Invalid credentials! Please try again')
            return redirect('/')

    return HttpResponse('404-Not found')

def user_logout(request):
    logout(request)
    messages.success(request,'Succesfully logged out')
    return redirect('/')