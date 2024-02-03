from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page, name="landing_page"),  # Landing page
    path("limo/customer", views.customer_page, name="customer_page"),  # Customer page
    path("limo/driver", views.driver_page, name="driver_page"),  # DRiver page
]