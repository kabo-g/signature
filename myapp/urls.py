from django.urls import path


from . views import SignatureView
from .views import myview
urlpatterns = [
    # path("", SignatureView.as_view(), name = "home"),
    path("", myview, name = "test"),
]
