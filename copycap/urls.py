from django.urls import path
from copycap.views import index, AccountCreateView

app_name = 'copycap'
urlpatterns = [
    path('', index, name='index'),
    path('create/', AccountCreateView.as_view(), name='create'),
]