from django.urls import path

from . import views

urlpatterns=[
    path("", views.ProductMixinView.as_view()),
    path("<int:pk>/update/", views.ProductMixinView.as_view()),
    path("<int:pk>/delete/", views.ProductDestroyAPIView.as_view()),
    path("<int:pk>/", views.ProductDetailAPIView.as_view())
]