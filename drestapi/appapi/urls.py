from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('shows/<email>', views.show, name='show'),
    path('show/<id>', views.show_id, name='show_id'),
    path('person/', views.createperson, name='createperson'),
    path('uperson/<id>', views.updateperson, name='updateperson'),
    path('dperson/<id>', views.deleteperson, name='deleteperson'),

]