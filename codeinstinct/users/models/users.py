from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=12, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    username = models.CharField(max_length=100, unique=True, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
