from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns=[
    path("auth/", obtain_auth_token),
    path("", views.ProductListCreateAPIView.as_view()),
    path("<int:pk>/update/", views.ProductUpdateAPIView.as_view()),
    path("<int:pk>/delete/", views.ProductDestroyAPIView.as_view()),
    path("<int:pk>/", views.ProductDetailAPIView.as_view())
]