from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('bank/<ifsc>', views.BankdetailsViewSet.as_view({'get': 'list'})),
    path('bank/<bank_name>/<city>', views.BranchesdetailsViewSet.as_view({'get': 'list'})),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
