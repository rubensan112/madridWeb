from rest_framework import serializers
from backend.change_management.models import AffectedEntityORM

class AffectedEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AffectedEntityORM # Crea el serializador partiendo del modelo, permitiendo ahorrar codigo

        # Este campo nos permitia elegir cuales mostrar cuando se despliega la lista en formato api en el rest_framework
        fields = ('provider', 'reference_number', 'reference_type', 'administrative_number', 'change_request')