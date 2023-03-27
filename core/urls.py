from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.user_login,name="login"),
    path('logout',views.logout_user,name="logout"),
    path('signup',views.user_signup,name="signup"),
    path('admin_local/',views.get_admin_page,name="admin"),
    path('admin_local/messages/<int:user_id>',views.users_messages ,name="messages"),
    path('admin_local/messages/delete_msg/<int:id>',views.delete_msg,name='delete_msg'),
    path('admin_local/messages/delete_msg/',views.delete_msg),
    path("admin_local/messages/clear_all/<int:id>",views.delete_all_messages,name="clear_all"),
    path('projects',views.projects,name="projects")
]
