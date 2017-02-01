from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie

from customers.models import Customer, CustomerUser

@ensure_csrf_cookie
def create(request):
    if request.method == 'POST':
        """
        - Customer
        <QueryDict: {
            u'confirm_password': [u'@dune369'],
            u'company_name': [u'Incisia'],
            u'password': [u'@dune369'],
            u'email': [u'alwaysdeone@gmail.com'],
            u'name': [u'Dayo Osikoya']
        }>
        - Subscriber
        - Vendor
        """
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        company_name = request.POST.get('company_name', None)
        password = request.POST.get('password', None)
        
        # Create user.
        user = User.objects.create_user(email, email, password)
    
        # Save name if provided
        if name:
            first_name, last_name = name.split(' ')
            user.first_name = first_name
            user.last_name = last_name
            user.save()
    
        if company_name:
            # Create customer and customer user if user provided company name.
            customer = Customer.objects.create(name=company_name)
            customer_user = CustomerUser.objects.create(customer=customer, user=user)
    
            # Company users are always staff.
            user.is_staff = True
    
            # First company user is a superuser. Only superusers can create other users.
            company_user_count = CustomerUser.objects.filter(customer=customer).count()
            if company_user_count == 1:
                user.is_superuser = True
    
            user.save()
    
        data = serializers.serialize('json', [user,])
        return JsonResponse({'result': data})
    else:
        return JsonResponse({'status': 'OK'})

@ensure_csrf_cookie
def get(request):
    email = request.GET['email']

    try:
        User.objects.get(email=email)
    except User.DoesNotExist:
        return JsonResponse({}, status=404)
    else:
        return JsonResponse({}, status=200)