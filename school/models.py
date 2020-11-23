from django.db import models
from owner.models import OwnerModel
from principal.models import PrincipalModel
# Create your models here.


class SchoolModel(models.Model):
    school_id = models.CharField(max_length=300, null=False)
    name = models.CharField(max_length=500, null=False)
    address = models.CharField(max_length=500, null=False)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(OwnerModel, on_delete=models.CASCADE)
    principal = models.ForeignKey(PrincipalModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
