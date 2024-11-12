from rest_framework import routers 
from django.urls import path,include
from user.views import ReactViewUserSet,MyTokenObtainPairView,ReactRegisterUserView,PasswordResetEmailVerifyAPIView,ReactViewUserDetails,PasswordChangeAPIView, LoginView
from django.conf import settings
from django.conf.urls.static import static
router = routers.DefaultRouter()
router.register(r'user', ReactViewUserSet, basename='user')

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("api/user/",  ReactViewUserSet.as_view({'get':'list'}), name="api", ),
    path("api/user/token/",MyTokenObtainPairView.as_view(),name="token"),
    path("api/user/token/refresh",TokenRefreshView.as_view(),name="refresh"),
    path("api/user/register",ReactRegisterUserView.as_view(),name="register"), 
    path("api/user/login",LoginView,name="login"),
    path("api/user-details/<email>/",ReactViewUserDetails.as_view(),name="userDetails"),  
    path("api/user/password-reset/<email>/",PasswordResetEmailVerifyAPIView.as_view(),name="passwordreset"),  
    path("api/user/password-change/",PasswordChangeAPIView.as_view(),name="passwordchange"), 

     


    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)