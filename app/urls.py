from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.Index,name="home"),
    path('blogpost/', views.BlogPostListCreate.as_view()),  # Add parentheses here
]
