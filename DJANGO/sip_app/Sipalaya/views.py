from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout


# Create your views here.
def home(request):
    data = EmployeeInfo.objects.all()
    
    return render(request,'web/dashboard.html',{'data': data})

def products(request):
    return render(request,'web/products.html')

def contact(request):
    return render(request,'web/contact.html')

def about(request):
    return render(request,'web/about.html')

def dashboard(request):
    return render(request,'web/dashboard.html')

def submit_form(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        # Create a new instance of the model
        my_model = EmployeeInfo(
            first_name=first_name,
            last_name=last_name,
            Phone=phone,
            Address=address)
        my_model.save()
        return redirect('home')
    
def DeleteData(request,id):
    data=EmployeeInfo.objects.get(id=id)
    data.delete()
    return redirect('Dashboard')

def EditData(request,id):
    data=EmployeeInfo.objects.get(id=id)
    if request.method == 'POST':
        data.first_name = request.POST.get('fname')
        data.last_name = request.POST.get('lname')
        data.Phone = request.POST.get('phone')
        data.Address = request.POST.get('address')
        data.save()
    
        return redirect('Dashboard')
    return render(request,'web/update.html', {'data':data})

def SearchData(request):
    if request.method=="GET":
        query=request.GET['query']
        searchdata1=EmployeeInfo.objects.filter(first_name__icontains=query)
        searchdata2=EmployeeInfo.objects.filter(Address__icontains=query)
        searchdata3=EmployeeInfo.objects.filter(Phone__icontains=query)
        searchdata4=EmployeeInfo.objects.filter(last_name__icontains=query)
        searchdata=searchdata1.union(searchdata2,searchdata3,searchdata4)
        
        
    return render(request,'web/search.html',{'searchdata':searchdata})
def Eyeglass(request):
    query = request.GET.get('query', '')
    # Perform the search logic using the query

    context = {
        'query': query,
        # Add other variables you want to pass to the template
    }

    return render(request, 'web/eyeglass.html', context)

def Image_Handler(request):
    if request.method=="POST":
        for file in request.FILES.getlist('image'):
            img=ImageHandler(image=file)
            img.save()
    data=ImageHandler.objects.all()
    return render(request,'web/products.html',{'data':data})

def User_Reg(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('uname')
        password = request.POST.get('pass1')
        confirm_password=request.POST.get('pass2')
        user=User.objects.create_user(username=username,password=password)
        user.first_name=first_name
        user.last_name=last_name
        user.save()


    
    return render(request,'web/reg.html')

def LogIn(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass1')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Dashboard')  # Redirect to the home page or any other desired page upon successful login
    
    return render(request, 'web/login.html')

def HandleLogout(request):
    logout(request)
    return redirect('login')