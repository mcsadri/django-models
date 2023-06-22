from django.urls import path
from .views import SnackListView, SnackDetailView, SnackAboutView


urlpatterns = [
    path('', SnackListView.as_view(), name='snack_list'),
    path('<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),
    path('about', SnackAboutView.as_view(), name='snack_about'),
]
