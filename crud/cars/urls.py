from django.urls import path
from .views import Car_form, Car_list, Car_delete

urlpatterns = [

    path('', Car_form.as_view(), name='insert'),
    path('<int:id>/', Car_form.as_view(), name='update'),
    path('list/', Car_list.as_view(), name='list'),
    path('delete/<int:id>/', Car_delete.as_view(), name='delete')
]
