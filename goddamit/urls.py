from django.urls import path
from goddamit.views import products

app_name = 'goddamit'
urlpatterns = [
    path('', products, name='products'),
    path('detail/', products, name='detail')
                ]

