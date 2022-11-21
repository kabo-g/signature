from django.db import models
from jsignature.fields import JSignatureField

# Create your models here.

class ServerRoom(models.Model):

    first_name = models.CharField(max_length = 200, blank = True, null = True)
    last_name = models.CharField(max_length = 200, blank = True, null = True)
    phone_no = models.CharField(max_length = 8, blank = True, null = True)
    company = models.CharField(max_length = 200, blank = True, null = True)
    date = models.DateField(null=True, blank = True)
    time_in = models.TimeField(null = True, blank = True)
    time_out = models.TimeField(null = True, blank = True)
    signature = JSignatureField(null = True, blank = True)


    def __str__(self):

        return self.first_name

    class Meta:
        pass
