
from . import views
from django.urls import path


urlpatterns = [

    # path('',views.demo,name='demo'),
    # path('home/',views.home,name='home'),
    # path('about/',views.about,name="about"),
    # path('contact/',views.contact,name="contact"),
    # path('detail/',views.detail,name="detail"),
    # path('thanks/',views.thanks,name="thanks")

    # path('',views.form,name='form'),
    # path('operations/',views.operations,name='operations')
    path('',views.giants,name='giants'),
    #path('',views.langs,name='langs'),
    #path('',views.lbg,name='lbg'),
    path('register',views.register,name='register'),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout")
]