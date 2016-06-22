from django.shortcuts import render,redirect
from ..login_reg.models import User
from models import Message
# Create your views here.
def index(request, user_id):

	context = {
		'user' : User.userManager.getOne(user_id),
		'messages' : Message.messageManager.getAll(user_id)
	}
	return render(request, 'wall/index.html', context)

def add_msg(request, wall_id):
	# user = User.userManager.getOne(request.session['id'])
	if request.method == "POST":
		user_tuple = Message.messageManager.addMessage(wall_id, request.POST['message'], request.session['id'])
		if user_tuple[0] == False:
			print user_tuple[1].values()
			return redirect('/../../user/'+wall_id)
		else:
			return redirect('/../../user/'+wall_id)
 
