from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from django.views.generic import TemplateView


urlpatterns = [

    path('bank/',views.BankdetailsViewSet.as_view({'get': 'list'})),
    path('bank/branches',views.BranchesdetailsViewSet.as_view({'get': 'list'})),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('', TemplateView.as_view(template_name="index.html"))
]


