from django.conf.urls import url
from user_form2 import views

app_name="user_form2"

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    
]