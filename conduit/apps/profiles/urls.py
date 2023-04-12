
from django.urls import include, path
from .views import ProfileRetrieveAPIView, ProfileFollowAPIView

urlpatterns = [
    path('profiles/<str:username>/', ProfileRetrieveAPIView.as_view()),
    path('profiles/<str:username>/follow/', ProfileFollowAPIView.as_view()),
]

