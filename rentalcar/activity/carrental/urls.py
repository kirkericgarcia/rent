from django.urls import path
from carrental.views import RentListView, RentDetailView, RentCreateView, RentUpdateView, RentDeleteView

urlpatterns = [
    path('', RentListView.as_view(), name='list-view-rent'),
    path('<int:pk>/', RentDetailView.as_view(), name='detail-view-rent'),
    path('create/', RentCreateView.as_view(), name='rent-create-view'),
    path('update/<int:pk>/', RentUpdateView.as_view(), name='rent-update-view'),
    path('delete/<int:pk>/', RentDeleteView.as_view(), name='rent-delete-view')
]
