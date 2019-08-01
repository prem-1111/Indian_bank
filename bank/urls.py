from django.urls import path
from . import views


urlpatterns = [
    path('bank/<ifsc>', views.BankdetailsViewSet.as_view({'get': 'list'})),
    path('bank/<bank_name>/<city>', views.BranchesdetailsViewSet.as_view({'get': 'list'})),

]
