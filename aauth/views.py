from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie

@login_required
def index(request):
    pass

@ensure_csrf_cookie
def login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user is not None:
        data = serializers.serialize('json', [user,])
        return JsonResponse({'code': 200, 'result': data})

    return JsonResponse({'status': 'OK'})