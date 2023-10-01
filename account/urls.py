from django.urls import path
from .views import *
from . import views



urlpatterns=[
    path('reg',RegView.as_view(),name='reg'),
    path('cust',CustHome.as_view(),name='h'),
    path('about',AboutHome.as_view(),name='about'),
    path('ser',ServiceHome.as_view(),name='ser'),
    path('contact',PersonaldataView.as_view(),name='cont'),
    path('ship/<int:id>',ShipHome.as_view(),name='ship'),
    path('storev',StoreView.as_view(),name='Store'),
    path('pay/<int:id>/',PaymentHome.as_view(),name='pay'),
    path("lgout",LgOutView.as_view(),name='lgout'),
    path('calculate_price/<int:id>/',calculate_price,name='calculate_price'),
    path('book',BookingView.as_view(),name='book'),
    
]

     
    
