from django.contrib import admin
from django.urls import path,include
from studentdata import views
urlpatterns = [
    
    path('std',views.std),
    path('show',views.show),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/int:id>',views.destroy),


]