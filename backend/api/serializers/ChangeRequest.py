from rest_framework import serializers
from backend.change_management.models import ChangeRequestORM, EmailORM, AffectedEntityORM, RemedyStateORM
from backend.api.serializers.AffectedEntity import AffectedEntitySerializer
from backend.api.serializers.Email import EmailSerializer
from backend.api.serializers.RemedyState import RemedyStateSerializer


class ChangeRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChangeRequestORM  # Crea el serializador partiendo del modelo, permitiendo ahorrar codigo

        # Este campo nos permitia elegir cuales mostrar cuando se despliega la lista en formato api en el rest_framework
        fields = ('start_date', 'end_date')

    def create(self, validated_data):
        '''
        email_data = validated_data.pop('email')
        serializer = EmailSerializer(data=email_data)
        serializer.is_valid()
        serializer.save()


        affected_entity = validated_data.pop('affected_entity')
        AffectedEntityORM.objects.create(**affected_entity)

        remedy_state = validated_data.pop('remedy_state')
        RemedyStateORM.objects.create(**remedy_state)
        '''
        change_request = ChangeRequestORM.objects.create(**validated_data)
        return change_request