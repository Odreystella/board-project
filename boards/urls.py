from django.urls import path
from .views import BoardCreateView, BoardDetailView, BoardUpdateView

app_name = "boards"

urlpatterns = [
    path("create/", BoardCreateView.as_view(), name="create" ),
    path("detail/<int:pk>/", BoardDetailView.as_view(), name="detail" ),
    path("edit/<int:pk>/", BoardUpdateView.as_view(), name="edit" ),
]