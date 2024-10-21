from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.throttling import UserRateThrottle

class CustomTokenObtainPairView(TokenObtainPairView):
    throttle_classes = [UserRateThrottle]

class CustomTokenRefreshView(TokenRefreshView):
    throttle_classes = [UserRateThrottle]
