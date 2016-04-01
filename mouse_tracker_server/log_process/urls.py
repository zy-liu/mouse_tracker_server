from django.conf.urls import url
from .views import doPost
urlpatterns = [
    url(r'^$', doPost),
]