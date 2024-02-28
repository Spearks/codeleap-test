from accounts.views import DecoratedTokenObtainPairView, SignUpUserView
from django.urls import path, include

urlpatterns = [
    path('auth/token/', DecoratedTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/signup/', SignUpUserView.as_view({'post': 'create'}), name='signup_user'),
]
