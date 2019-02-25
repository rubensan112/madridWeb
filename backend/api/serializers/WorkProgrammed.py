
from rest_framework import serializers
from backend.work_management.models import WorkProgrammedORM

class WorkProgrammedSerializer(serializers.ModelSerializer):


    class Meta:
        model = WorkProgrammedORM #Crea el serializador partiendo del modelo, permitiendo ahorrar codigo

        #Este campo nos permitia elegir cuales mostrar cuando se despliega la lista en formato api en el rest_framework
        fields = ('name', 'creationDate','ownerOfNet', 'description','actualStartTime','actualEndTime')