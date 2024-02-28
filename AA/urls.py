from django.urls import path
from .views import Talk,all_prof,profile,delete_prof,update

urlpatterns = [
    path('',Talk, name='Talk'),
    path('all_prof/',all_prof, name='all_prof'),
    path('profile/', profile, name='profile'),
    path('delete_prof/<int:id>/', delete_prof, name='delete_prof'),
    path('update/<int:id>/', update, name='update'),

]
