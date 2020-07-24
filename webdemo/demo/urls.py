from django.urls import path
from . import views, emp_views

urlpatterns = [
    path("index/", views.index),
    path("countries/", views.list_countries),
    path("country/", views.get_country_info),
    path("addemployee/", emp_views.add_employee),
    path("addemployee2/", emp_views.add_employee_with_form),
    path("employees/", emp_views.list_employees),
]
