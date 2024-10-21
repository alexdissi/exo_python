from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.throttling import UserRateThrottle

class CustomTokenObtainPairView(TokenObtainPairView):
    throttle_classes = [UserRateThrottle]  # Appliquer le throttling ici

class CustomTokenRefreshView(TokenRefreshView):
    throttle_classes = [UserRateThrottle]  # Appliquer le throttling ici
