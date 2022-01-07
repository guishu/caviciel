import datetime

from django.db import models
from django.db.models import Q
from django.core.validators import MinValueValidator, MaxValueValidator

from phonenumber_field.modelfields import PhoneNumberField


class Region(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Classification(models.Model):
    TYPE_CHOICES = [
        ("AOC", "AOC"),
        ("AOP", "AOP"),
        ("IGP", "IGP"),
        ("VDP", "Vin de Pays"),
        ("Autre", "Autre")
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default="AOC")
    name = models.CharField(max_length=150)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="classifications")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=("type", "name"), name="unique_type_name")
        ]

    def __str__(self):
        if self.type == "Autre":
            return self.name
        else:
            return f"{self.get_type_display()} {self.name}"


class Color(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Producer(models.Model):
    name = models.CharField(null=True, blank=True, max_length=255)
    domain = models.CharField(null=True, blank=True, max_length=255)
    address = models.CharField(null=True, blank=True, max_length=2048)
    phone = PhoneNumberField(null=True, blank=True)
    mobile = PhoneNumberField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'domain'], name='unique_name_domain'),
            models.CheckConstraint(check=Q(name__isnull=False) | Q(domain__isnull=False), name='not_both_null')
        ]

    def __str__(self):
        return " - ".join(filter(None, [self.domain, self.name]))


class Wine(models.Model):
    name = models.CharField(null=True, blank=True, max_length=255)
    vintage = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(datetime.date.today().year)])
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name="wines")
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name="wines")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True, related_name="wines")
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, null=True, blank=True, related_name="wines")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['producer', 'name'], name='unique_name_producer'),
        ]

    def __str__(self):
        return " - ".join(filter(None, [str(self.producer), self.name, str(self.color), str(self.vintage)]))
