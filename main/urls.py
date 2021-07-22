from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home_view'),
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update_view'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete_view'),
    path(
        'cross_off/<int:pk>/',
        views.CrossOffView.as_view(),
        name='cross_off'
    ),
    path('uncross/<int:pk>/', views.UncrossView.as_view(), name='uncross'),
]
