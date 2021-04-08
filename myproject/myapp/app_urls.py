from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('add/<int:a>/<int:b>',views.add,name="add"),
    path('intro/<str:name>/<int:age>',views.intro,name="intro"),
    path('example',views.example,name="example"),
    path('third',views.third,name="third"),
    path('imagepage',views.imagepage,name="imagepage"),
    path('imagepage2',views.imagepage2,name="imagepage2"),
    path('passcolor/<str:color>',views.passcolor,name="passcolor"),
]