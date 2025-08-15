from rest_framework import generics, permissions
from rest_framework.response import Response
from django.db.models import Sum
from .models import Activity, Profile
from .serializers import (
    RegisterSerializer,
    ProfileSerializer,
    ActivitySerializer,
    ActivityMetricsSerializer
)


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


class ActivityListCreateView(generics.ListCreateAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ActivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)


class ActivityHistoryView(generics.ListAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Activity.objects.filter(user=self.request.user)
        activity_type = self.request.query_params.get('activity_type')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if activity_type:
            queryset = queryset.filter(activity_type__iexact=activity_type)
        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        return queryset


class ActivityMetricsView(generics.GenericAPIView):
    serializer_class = ActivityMetricsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        activities = Activity.objects.filter(user=request.user)

        if start_date and end_date:
            activities = activities.filter(date__range=[start_date, end_date])

        metrics = activities.aggregate(
            total_duration=Sum('duration'),
            total_distance=Sum('distance'),
            total_calories=Sum('calories_burned')
        )

        data = {
            'total_duration': metrics['total_duration'] or 0,
            'total_distance': metrics['total_distance'] or 0,
            'total_calories': metrics['total_calories'] or 0,
            'start_date': start_date,
            'end_date': end_date
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
