from django.urls import path
from static_app import views
app_name="static_app"

urlpatterns = [
    path('motto/',views.motto,name="motto"),
    path('profile/',views.profile,name="profile"),
]
