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