from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Application(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=60, unique=True)
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=240, blank=True, null=True)
    base_url = models.URLField(max_length=255)
    username = models.CharField(max_length=60, blank=True, null=True)
    password = models.CharField(max_length=60, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    icon = models.ImageField(upload_to="static/images", blank=True, null=True)
    created_by = models.ForeignKey(
        User, related_name="create_applications", on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated_by = models.ForeignKey(
        User, related_name="update_applications", on_delete=models.DO_NOTHING)
    last_update_date = models.DateTimeField(auto_now=True)


# class Service(models.Model):
#     id = models.IntegerField(primary_key=True)
#     application = models.ForeignKey(
#         Application, on_delete=models.deletion.CASCADE)
#     code = models.CharField(max_length=60, unique=True)
#     name = models.CharField(max_length=60, unique=True)
#     description = models.CharField(max_length=240, blank=True, null=True)
#     serviceType = models.CharField(max_length=30, default="GET")
#     url = models.URLField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     icon = models.ImageField(upload_to="static/images", blank=True, null=True)


# class Parameter(models.Model):
#     id = models.IntegerField(primary_key=True)
#     service = models.ForeignKey()


# class Entity(models.Model):
#     id = models.IntegerField(primary_key=True)
#     code = models.CharField(max_length=60, unique=True)
#     name = models.CharField(max_length=60, unique=True)
#     description = models.CharField(max_length=240, blank=True, null=True)
#     isActive = models.BooleanField(default=True)


# class EntityApplication(models.Model):
#     id = models.IntegerField(primary_key=True)
#     entityId = models.ForeignKey(Entity, models.deletion.CASCADE)
#     applicationId = models.ForeignKey(Application,  models.deletion.CASCADE)
#     description = models.CharField(max_length=240, blank=True, null=True)
#     isActive = models.BooleanField(default=True)


# class ElementType(models.Model):
#     id = models.IntegerField(primary_key=True)
#     code = models.CharField(max_length=60, unique=True)
#     name = models.CharField(max_length=60, unique=True)
#     description = models.CharField(max_length=240, blank=True, null=True)
#     isActive = models.BooleanField(default=True)


# class EntityElementType(models.Model):
#     id = models.IntegerField(primary_key=True)
#     entityId = models.ForeignKey(Entity, on_delete=models.deletion.CASCADE)
#     elementId = models.IntegerField()
#     description = models.CharField(max_length=240, blank=True, null=True)
#     isActive = models.BooleanField(default=True)
#     calculationMethod = models.CharField(max_length=30, default="service")
#     fixedAmount = models.DecimalField(
#         max_digits=11, decimal_places=2, blank=True, null=True)
#     serviceId = models.ForeignKey(
#         ElementType, blank=True, null=True, on_delete=models.deletion.CASCADE)
#     isActive = models.BooleanField(default=True)


# class Role(models.Model):
#     id = models.IntegerField(primary_key=True)
#     code = models.CharField(max_length=60, unique=True)
#     name = models.CharField(max_length=60, unique=True)
#     description = models.CharField(max_length=240, blank=True, null=True)
#     isActive = models.BooleanField(default=True)


# class RoleLine(models.Model):
#     id = models.IntegerField(primary_key=True)
#     roleId = models.ForeignKey(Role, on_delete=models.deletion.CASCADE)
#     periodUom = models.CharField(max_length=30)
#     period = models.IntegerField()
#     percentage = models.IntegerField()
#     maxYears = models.IntegerField(blank=True, null=True)


# class ClaimType(models.Model):
#     id = models.IntegerField(primary_key=True)
#     code = models.CharField(max_length=60, unique=True)
#     name = models.CharField(max_length=60, unique=True)
#     description = models.CharField(max_length=240, blank=True, null=True)
#     isActive = models.BooleanField(default=True)


# class ClaimTypeElement(models.Model):
#     id = models.IntegerField(primary_key=True)
#     claimTypeId = models.ForeignKey(
#         ClaimType, on_delete=models.deletion.CASCADE)
#     elementTypeId = models.ForeignKey(
#         ElementType, on_delete=models.deletion.CASCADE)
#     isActive = models.BooleanField(default=True)


# class Decision(models.Model):
#     id = models.IntegerField(primary_key=True)
#     code = models.CharField(max_length=60, unique=True)
#     name = models.CharField(max_length=60, unique=True)
#     description = models.CharField(max_length=240, blank=True, null=True)
#     claimTypeId = models.ForeignKey(
#         ClaimType, on_delete=models.deletion.CASCADE)
#     roleId = models.ForeignKey(Role, on_delete=models.deletion.CASCADE)
#     startDate = models.DateField()
#     endDate = models.DateField(blank=True, null=True)
#     isActive = models.BooleanField(default=True)


# class DecisionElementType(models.Model):
#     id = models.IntegerField(primary_key=True)
#     decisionId = models.ForeignKey(Decision, on_delete=models.deletion.CASCADE)
#     elementTypeId = models.ForeignKey(
#         ElementType, on_delete=models.deletion.CASCADE)
#     roleId = models.ForeignKey(Role, on_delete=models.deletion.CASCADE)
