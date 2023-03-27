from django.contrib.auth.models import User
from django.http import Http404
from .models import Malicious_count
from django.shortcuts import redirect
# get user object
# check if user tried to access the admin panel 
# block the user from the website for a limited ammount of time

home_path:str = ''





# create a default homepage in your app
# think of it as a url destination for 
# users that hv been kicked out of your website
def set_home_page(home:str):
    home_path = home

def get_home_page():
    return home_path




"""
    This function  is used to delete users that hv
      performed illegal activities or users that hv the ability to
    access pages that they r not supposed to...you can return this 
    function in your views.py instead of returning a HttpResponse or render as this
    function will handle the rest
"""
def spot_mal_and_act(user_obj : User) :
    try:
        get_mal_count = Malicious_count.objects.get(user=user_obj)

        if get_mal_count.mal_count >=3 :
            user_obj.delete()
            return redirect('logout')
        else:
            get_mal_count.mal_user_spotted()
            return redirect('index')
    except Malicious_count.DoesNotExist:
        # create a new object
        new_mal_user = Malicious_count.objects.create(user=user_obj)
        new_mal_user.save()
        get_mal_count = Malicious_count.objects.get(user=user_obj)

        if get_mal_count.mal_count >=3 :
            user_obj.delete()
            return redirect('logout')
        else:
            get_mal_count.mal_user_spotted()
            return redirect('index')
        
        return redirect(get_home_page())
