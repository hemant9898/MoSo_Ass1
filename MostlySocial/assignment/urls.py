from django.contrib import admin
from django.urls import include,path
from . import views

app_name ="assignment"

urlpatterns = [
    path("",views.index,name="index"),
    path("login_view",views.login_view,name="login_view"),
    path("signup_view",views.signup_view,name="signup_view"),
    path("dashboard_view/",views.dashboard_view,name="dashboard_view"),
    # path("filter_it",views.filter_it,name="filter_it"),
    # path('my-ajax-test/', views.filter_it),
    # path('my-ajax-test/', views.filter_it, name='ajax-test-view'),
    path("filtered_con", views.filtered_con,name="filtered_con"),
    path("login_process",views.login_process,name="login_process"),
    path("signup_process",views.signup_process,name="signup_process"),
    path("logout_view",views.logout_view,name="logout_view"),

]