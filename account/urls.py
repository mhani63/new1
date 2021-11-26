from django.contrib.auth import logout, views
from django.urls import path
from django.urls.resolvers import URLPattern
from. views import LoginView , logout_view , Profile , activate , signup,PasswordChange

app_name='account'
urlpatterns=[
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',logout_view,name='logout'),
    path('profile/',Profile.as_view(),name='profile'),
    path('password_change/',PasswordChange.as_view(),name='password_change_view'),
    path('password_change/done/',views.PasswordChangeDoneView.as_view(),name='password_change_done'),


]


urlpatterns +=[
    path('signup/', signup, name='signup'),
    path('activate/<uidb64>/<token>/', activate,name='activate'),


]