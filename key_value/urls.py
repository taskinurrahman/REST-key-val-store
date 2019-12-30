

from django.urls import path
from key_value import views
urlpatterns = [
    path('values/',views.values,name='values'),
]
