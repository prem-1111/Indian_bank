from rest_framework import serializers
from .models import BankBranches


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('bank_id', 'bank_name')
        model = BankBranches


class BranchesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state', 'bank_name')
        model = BankBranches
