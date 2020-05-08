from django.conf.urls import url
from appli import views
# SET THE NAMESPACE!
app_name = 'appli'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]