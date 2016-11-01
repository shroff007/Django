from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import Person
from .forms import PersonForm, LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    people = Person.objects.all()
    form = PersonForm()
    return render(request,'index.html',{'people': people, 'form': form})

def post_person(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        person = form.save(commit = False)
        person.user = request.user
        person.save()
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse('<h1>The account has been disabled!</h1>')
            else:
                return HttpResponse("<h1>The username and password are incorrect.</h1>")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

#class Person:
    #"""docstring for ."""
    #def __init__(self, name, userType):
        #self.name = name
        #self.userType = userType

#people = [
    #Person('Tom Wells','Rentee'),
    #Person('Dick Ericson','Renter')
#]
