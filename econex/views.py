from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# from .forms import NameForm

import json

# Create your views here.

# def send_e_mail(request):
#     if request.method == 'POST':
#         print(request.POST.get('user_name'))
#         print(request.POST.get('user_phone'))
#         print(request.POST.get('user_email'))
#         user_name  = request.POST['user_name']
#         user_phone = request.POST['user_phone']
#         user_email = request.POST['user_email']
#         send_mail('Contact Form',
#         user_name,
#         user_phone,
#         user_email,
#         settings.EMAIL_HOST_USER,
#         ['mail.martinaa@gmail.com'], 
# 		fail_silently=True)
#     return render(request, 'econex/index.html')

def contact(request):
    if request.method == 'POST':
        user_name  = request.POST['user_name']
        user_phone = request.POST['user_phone']
        user_email = request.POST['user_email']

        send_mail(
            user_name,
            user_phone,
            user_email,
            ['gcrasnodar@gmail.com']
            )

        return render(request, 'econex/contact.html',) 

        

def posts_list(request):
    return render(request, 'econex/index.html', context={'categores': Category.objects.order_by('order_num')})

def post_detail(request, slug = ''):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'econex/post_detail.html', context={'post': post, 'slug-post':{'slug':'piska'}})

def seria_detail(request, pk = None):
   
    seria = Seria.objects.get(pk = pk)
    
    return render(request, 'econex/seria_detail.html', context={'seria': seria})



def pull_db(request):
    with open('catalog.json', encoding='utf-8') as file:
        data = json.load(file)
        i = 1
        for p in data:
            cat = Category.objects.create(name = p['name'], order_num=i)
            cat.save()
            i += 1
            for seria in p['series']:
                ser = Seria.objects.create(
                    name=seria['name'],
                    types=seria['type'],
                    catogory_id=cat.pk
                )
                ser.save()
                for model in seria['models']:
                    OsveshModel.objects.create(
                        name=model['name'],
                        article=model["article"],
                        power=model["power"] ,
                        light=model["light"] ,
                        efficincy=model["efficincy"],
                        size=model["size"],
                        price = 1000,
                        seria_id=ser.pk
                    ).save
    return HttpResponse("qwe")

###############################################################################  Email  ####################################################

# from django.core.mail import send_mail

# if form.is_valid():
#     subject    = form.cleaned_data['subject']
#     message    = form.cleaned_data['message']
#     sender     = form.cleaned_data['sender']
#     cc_myself  = form.cleaned_data['cc_myself']

#     recipients = ['mail.mmartina@gmail.com']
#     if cc_myself:
#         recipients.append(sender)

#     send_mail(subject, message, sender, recipients)
    #return HttpResponseRedirect('/thanks/')