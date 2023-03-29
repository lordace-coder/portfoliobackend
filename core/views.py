from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Users_messages
from django.contrib.auth.decorators import login_required
from . import urls
# my own model
from blocker.security import spot_mal_and_act,set_home_page





# Create your views here.
def index(request):
    if request.user.is_authenticated and request.method == 'POST':
        msg = request.POST['message']
        if msg =='' or len(msg) <= 10:
            messages.info(request,'Message cant be less than 10 characters')
            return redirect('index')
        else:
            message = Users_messages.objects.create(senders_name=request.user,msg_txt=msg)
            message.save()
            messages.info(request,'message sent,Reply will be sent via email')
            return redirect('index')

    else:
        context = {}
        return render(request,'index.html',context)

set_home_page('index')



def user_login(request):

    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=name,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Credentials invalid')
            return redirect('login')
    return render(request,'login.html')






def user_signup(request):

    if request.method == 'POST':
        username= request.POST['username']
        email_address = request.POST['contact']
        password = request.POST['password1']
        confirm_password = request.POST['password2']

        if User.objects.filter(username=username):
            messages.info(request,'Sorry Username already exits')
            context = {}
            return redirect('signup')

        if password is None:
            messages.info(request,'insert valid password')
        elif username in password:
            messages.info(
                request,'password not strong enough'
            )
        
        elif len(password) <= 8:
            messages.info(request,'password has to be more than 8 characters')

        elif password == confirm_password :
            user = User.objects.create_user(
                username = username,
                password=confirm_password,
                email=email_address,
                )
            user.save()
            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.info(request,'Credentials invalid')
                return redirect('login')
            return redirect('index')
        else:
            messages.info(request,'Passwords dont match')
        
    context = {}
    return render(request,'signup.html',context)



def logout_user(request):
    logout(request)
    return redirect('login')





@login_required(login_url='login')
def get_admin_page(request):

    if request.user.is_superuser:
        users=User.objects.all()
        total_msg_count=0

        senders_names = {} 
        for msg in Users_messages.objects.all():
            total_msg_count+=1

            if msg.senders_name not in senders_names:
                senders_names[msg.senders_name]=1
            else:
                senders_names[msg.senders_name]+=1
        context = {
            'no_of_pages':len(urls.urlpatterns),
            'messages':total_msg_count,
            'senders_names':senders_names,
            'no_of_users':len(users)
        }
        return render(request,'admin_page.html',context)
    else:
        return spot_mal_and_act(request.user)
        



@login_required(login_url='login')
def users_messages(request,user_id):
    if request.user.is_superuser:
        user=User.objects.get(id=user_id)

        msg = Users_messages.objects.filter(senders_name = user)
        context = {
            'user':user,
            'messages':msg
        }
        return render(request,'messages.html',context)
    else:
        return spot_mal_and_act(request.user)
        # return HttpResponse('Not Allowed to view this page')


@login_required(login_url='login')
def delete_msg(request,id =None):
    if id == None:
        ...
    else:
        msg = Users_messages.objects.get(id=id)
        temp = msg
        msg.delete()
        id_for_url = temp.senders_name.id
    return redirect('messages' ,user_id=id_for_url)




@login_required(login_url='login')
def delete_all_messages(request,id =None):
    user = User.objects.get(id=id)

    if id == None:
        ...
    else:
        msg = Users_messages.objects.filter(senders_name = user)
        for i in msg:
            i.delete()
    return redirect('../../')





def projects(request):
    return render(request,'coming_soon.html')