from django.urls import path
from .views import DeviceView

urlpatterns = [
    path(
        f"device/",
        DeviceView.as_view(),
        name="device"),
    path(
        f"device/<int:pk>/",
        DeviceView.as_view(),
        name="device-get-retrieve"),
]
