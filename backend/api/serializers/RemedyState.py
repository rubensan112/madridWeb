from rest_framework import serializers
from backend.change_management.models import RemedyStateORM

class RemedyStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemedyStateORM # Crea el serializador partiendo del modelo, permitiendo ahorrar codigo

        # Este campo nos permitia elegir cuales mostrar cuando se despliega la lista en formato api en el rest_framework
        fields = ('state', 'url', 'id_ticket', 'creator_name','creator_departament','change_request')