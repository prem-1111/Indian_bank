# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BankSerializer, BranchesSerializer
from .models import BankBranches
# Create your views here.
from rest_framework.permissions import IsAuthenticated


class BankdetailsViewSet(viewsets.ModelViewSet):

    serializer_class = BankSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        ifsc = self.request.GET.get('ifsc')
        queryset = BankBranches.objects.filter(ifsc=ifsc)
        print(queryset)
        return queryset


class BranchesdetailsViewSet(viewsets.ModelViewSet):

    serializer_class = BranchesSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        bank_name = self.request.GET.get('bank_name')
        city = self.request.GET.get('city')
        queryset = BankBranches.objects.filter(bank_name=bank_name, city=city)
        print(queryset)
        return queryset

