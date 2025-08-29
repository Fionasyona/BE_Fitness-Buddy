from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # User management
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

    # Activity CRUD
    path('activities/', views.ActivityListCreateView.as_view(), name='activity-list-create'),
    path('activities/<int:pk>/', views.ActivityDetailView.as_view(), name='activity-detail'),

    # Activity history with filters
    path('activities/history/', views.ActivityHistoryView.as_view(), name='activity-history'),

    # Metrics
    path('activities/metrics/', views.ActivityMetricsView.as_view(), name='activity-metrics'),

     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
