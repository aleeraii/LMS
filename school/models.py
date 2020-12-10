from django.db import models
from owner.models import OwnerModel
from principal.models import PrincipalModel


class FunctionModel(models.Model):
    role = models.CharField(max_length=300)

    def __str__(self):
        return self.role


class SchoolModel(models.Model):
    school_id = models.CharField(max_length=300, blank=True)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(OwnerModel, models.SET_NULL,
                              blank=True,
                              null=True,)
    principal = models.ForeignKey(
        PrincipalModel, models.SET_NULL,
        blank=True,
        null=True,)
    student_function = models.ManyToManyField(
        FunctionModel, related_name='+', blank=False)
    teacher_function = models.ManyToManyField(
        FunctionModel, related_name='+', blank=False)
    parent_function = models.ManyToManyField(
        FunctionModel, related_name='+', blank=False)
    principal_function = models.ManyToManyField(
        FunctionModel, related_name='+', blank=False)
    owner_function = models.ManyToManyField(
        FunctionModel, related_name='+', blank=False)
    admin_function = models.ManyToManyField(
        FunctionModel, related_name='+', blank=False)

    def __str__(self):
        return self.name
