from django.urls import path
from . import views

app_name = "benchlist"

urlpatterns = [
    path('', views.home_view, name="home-view"),
    path('consultants/', views.consultants_view, name="consultants-view"),
    path('prospect_consultants/', views.prospect_consultants_view, name="prospect-consultants-view"),
    path('bench_consultants/', views.benchlist_view, name="benchlist-view"),
    path('submissions/', views.submission_view, name="submission-view"),
]
