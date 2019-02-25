from rest_framework import serializers
from backend.change_management.models import EmailORM

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailORM # Crea el serializador partiendo del modelo, permitiendo ahorrar codigo

        # Este campo nos permitia elegir cuales mostrar cuando se despliega la lista en formato api en el rest_framework
        fields = ('sender', 'receiver', 'subject', 'body','received_date','change_request')

