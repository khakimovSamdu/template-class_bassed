from django.urls import path
from .views import SmartphoneViews
urlpatterns = [
    path('', SmartphoneViews.as_view())
]