from django.urls import path
from . import views
urlpatterns=[

    path('signup/',views.sign_up,name="signup"),
    path('login_page/',views.login_page,name="login_page"),
    path('view/',views.view,name='view')
]