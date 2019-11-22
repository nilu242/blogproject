from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list_view),
    path('detail/<int:pk>',views.BlogDetailView.as_view()),
    path('dashboard/',views.dashboard_view),
    path('dashboard/<int:pk>/update',views.update_view),
    path('dashboard/<int:pk>/delete',views.delete_view),
    path('create/',views.createview),
]
