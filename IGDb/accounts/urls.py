from django.urls import path
from . import views


urlpatterns = [
    path("register", views.register_user, name="register_user"),
    path("login", views.login_user, name="login_user"),
    path("update/information",views.edit_personal_info, name="update_information"),
    path("information",views.personal_info, name="personal_info"),
]