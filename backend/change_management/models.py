from django.db import models

# Create your models here.
from django.db import models
from backend.shared.infrastructure.mappers import EntityMapper

#temporal
REFERENCE_TYPES = (
    ('type1', 'Freshman'),
    ('type2', 'Sophomore'),
    ('type3', 'Junior'),
    ('type4', 'Senior'),
)

STATES = (
    (0,'CRQ created'),
    (1, 'CRQ in progress'),
    (2, 'CRQ closed')
)

#Opciones de clase derivada models.Model
#o from backend.shared.infrastructure.mappers import EntityMapper

class ChangeRequestORM(EntityMapper):
    start_date = models.DateTimeField('Date and time when the change implementation is started',null=True)
    end_date = models.DateTimeField('Date and time when the change implementation is finished',null=True)
    #email = models.ForeignKey(EmailORM, on_delete=models.CASCADE, null=True)
    #affected_entity = models.ForeignKey(AffectedEntityORM, on_delete=models.CASCADE,null=True)
    #remedy_state = models.ForeignKey(RemedyStateORM, on_delete=models.CASCADE,null=True)

    def __unicode__(self):
        return '%s' % (self.start_date)


class EmailORM(EntityMapper):
    sender = models.CharField(max_length=100, blank=False)
    receiver = models.CharField(max_length=100, blank=False)
    subject = models.TextField(max_length=1000, blank=False)
    body = models.TextField(max_length=5000, blank=False)
    received_date = models.DateTimeField('Date and time when the email was received', blank=False)
    change_request = models.ForeignKey(ChangeRequestORM, related_name='email', on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return '%s' % (self.sender)

class AffectedEntityORM(EntityMapper):
    provider = models.CharField(max_length=100, blank=False)
    reference_number = models.CharField(max_length=300, blank=False)
    reference_type = models.CharField(max_length=100, blank=False, choices=REFERENCE_TYPES)
    administrative_number = models.CharField(max_length=300, blank=False)
    change_request = models.ForeignKey(ChangeRequestORM, related_name='affected_entity', on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return '%s' % (self.administrative_number)


class RemedyStateORM(EntityMapper):
    state = models.IntegerField(blank=False, choices=STATES)
    url = models.URLField(blank=False)
    id_ticket = models.CharField(max_length=100, blank=False)
    creator_name = models.CharField(max_length=100, blank=False)
    creator_departament = models.CharField(max_length=100, blank=False)
    change_request = models.ForeignKey(ChangeRequestORM, related_name='remedy_state', on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return '%s' % (self.id_ticket)
