from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.core import serializers

@ensure_csrf_cookie
def login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user is not None:
        data = serializers.serialize('json', [user,])
        return JsonResponse({'code': 200, 'result': data})

    return JsonResponse({'status': 'OK'})