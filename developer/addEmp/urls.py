from django.urls import path
from . import views
app_name = 'addEmp'
urlpatterns = [
    path('data/', views.EmpData, name='DevloperData'),
    path('edit/<int:id>', views.edit_view, name='DevloperData'),
]
