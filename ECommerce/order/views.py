from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from accounts.models import UserDetail


@login_required
def details(request):
    user = request.user
    user_details = UserDetail.objects.filter(user__username=user)
    # print(user_detail)
    if len(user_details)!=0:
        context = { 'user_details': user_details }
    else:
        context = {}
    print(context)
    return render(request, 'userdetails.html', context=context)

@login_required
def order(request):
    if request.method=='POST':
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        exists = request.POST.get('existed_value')
        print(exists)
        if exists=='False':
            user = request.user
            userdetails = UserDetail.objects.create(user=user, address=address, phone=phone)
            userdetails.save()
    return HttpResponse('hello there')