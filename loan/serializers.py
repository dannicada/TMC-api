from rest_framework.serializers import ModelSerializer
from .models import Customer



class LoanSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        