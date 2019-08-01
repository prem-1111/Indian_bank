# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BankSerializer, BranchesSerializer
from .models import BankBranches
# Create your views here.


class BankdetailsViewSet(viewsets.ModelViewSet):

    serializer_class = BankSerializer

    def get_queryset(self):
        ifsc = self.kwargs['ifsc']
        queryset = BankBranches.objects.filter(ifsc=ifsc)
        print(queryset)
        return queryset


class BranchesdetailsViewSet(viewsets.ModelViewSet):

    serializer_class = BranchesSerializer

    def get_queryset(self):
        bank_name = self.kwargs['bank_name']
        city = self.kwargs['city']
        queryset = BankBranches.objects.filter(bank_name=bank_name, city=city)
        print(queryset)
        return queryset

