from django.shortcuts import render
from ..login_reg.models import User
# Create your views here.
def index(request, user_id):
	context = {
		'user' : User.userManager.getOne(user_id)
	}
	return render(request, 'wall/index.html', context)