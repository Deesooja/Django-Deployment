from django.urls import path
from App.views import CrudApiView

urlpatterns = [
    path("api",CrudApiView.as_view()),
    path("api/<int:pk>",CrudApiView.as_view()),
]