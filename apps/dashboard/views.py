from django.shortcuts import render,redirect

from ..login_reg.models import User

# Create your views here.
def index(request):
	context = {
		'users' : User.userManager.getAll()
	}
	return render(request, 'dashboard/index.html', context)

def logout(request):
	request.session.clear()
	return redirect('/')

def new(request):
	return render(request, 'dashboard/new.html')

def add_new(request):
	if request.method == "POST":
		user_tuple = User.userManager.register(request.POST['first_name'],request.POST['last_name'],request.POST['email'],request.POST['password'],request.POST['conf_password'])
		if user_tuple[0] == False:
			context = {
				'errors' : user_tuple[1].values()
			}
			return render(request, 'dashboard/new.html', context)
		else:
			return redirect('../../dashboard')

def my_profile(request, user_id):
	return render(request, 'dashboard/profile.html')
