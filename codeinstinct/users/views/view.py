from django.views import View
from django.shortcuts import render
from users.models.users import User

class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'user_list.html', {'users': users})
