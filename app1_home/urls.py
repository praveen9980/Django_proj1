
from django.urls import path, re_path
from app1_home import views

urlpatterns = [
    re_path(r'^$',views.wellcome,name="wellcome"),

]