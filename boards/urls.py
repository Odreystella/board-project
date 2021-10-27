from django.urls import path
from .views import BoardCreateView

app_name = "boards"

urlpatterns = [
  path("create/", BoardCreateView.as_view(), name="create" )
]