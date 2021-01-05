from django.db import models
# Create your models here.


class Application(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=60, unique=True)
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=240, blank=True, null=True)
    url = models.URLField(max_length=255)
    isActive = models.BooleanField(default=True)
    icon = models.ImageField(upload_to="static/images", blank=True, null=True)


class Service(models.Model):
    id = models.IntegerField(primary_key=True)
    applicationId = models.ForeignKey(Application)
    code = models.CharField(max_length=60, unique=True)
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=240, blank=True, null=True)
    serviceType = models.CharField(max_length=30, default="GET")
    url = models.URLField(max_length=255)
    isActive = models.BooleanField(default=True)
    icon = models.ImageField(upload_to="static/images", blank=True, null=True)


class Entity(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=60, unique=True)
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=240, blank=True, null=True)
    isActive = models.BooleanField(default=True)


class EntityApplication(models.Model):
    id = models.IntegerField(primary_key=True)
    entityId = models.ForeignKey(Entity)
    applicationId = models.ForeignKey(Application)
    description = models.CharField(max_length=240, blank=True, null=True)
    isActive = models.BooleanField(default=True)


class ElementType(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=60, unique=True)
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=240, blank=True, null=True)
    isActive = models.BooleanField(default=True)


class EntityElement(models.Model):
    id = models.IntegerField(primary_key=True)
    entityId = models.ForeignKey(Entity)
    elementId = models.IntegerField()
    description = models.CharField(max_length=240, blank=True, null=True)
    isActive = models.BooleanField(default=True)
    calculationMethod = models.CharField(max_length=30, default="service")
    fixedAmount = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    serviceId = models.ForeignKey(ElementType, blank=True, null=True)
    isActive = models.BooleanField(default=True)


class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=60, unique=True)
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=240, blank=True, null=True)
    isActive = models.BooleanField(default=True)


class RoleLine(models.Model):
    id = models.IntegerField(primary_key=True)
    roleId = models.ForeignKey(Role)
    periodUom = models.CharField(max_length=30)
    period = models.IntegerField()
    percentage = models.IntegerField()
    maxYears = models.IntegerField(blank=True, null=True)


class ClaimType(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=60, unique=True)
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=240, blank=True, null=True)
    isActive = models.BooleanField(default=True)


class ClaimTypeElement(models.Model):
    id = models.IntegerField(primary_key=True)
    claimTypeId = models.ForeignKey(ClaimType)
    elementTypeId = models.ForeignKey(ElementType)
    isActive = models.BooleanField(default=True)


class Decision(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=60, unique=True)
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=240, blank=True, null=True)
    claimTypeId = models.ForeignKey(ClaimType)
    roleId = models.ForeignKey(Role)
    startDate = models.DateField()
    endDate = models.DateField(blank=True, null=True)
    isActive = models.BooleanField(default=True)


class DecisionElementType(models.Model):
    id = models.IntegerField(primary_key=True)
    decisionId = models.ForeignKey(Decision)
    elementTypeId = models.ForeignKey(ElementType)
    roleId = models.ForeignKey(Role)



















