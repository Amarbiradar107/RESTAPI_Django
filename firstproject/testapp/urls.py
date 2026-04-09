
from django.urls import path
from .views import todo_list, todo_detail

urlpatterns = [
    path('todo_view/', todo_list),
    path('todo_details/<str:id>/',todo_detail),
]