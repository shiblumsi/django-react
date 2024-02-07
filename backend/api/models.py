from django.db import models
from autoslug import AutoSlugField
import uuid


class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    # slug = AutoSlugField(populate_from='title', unique=True, max_length=50, separator='_', always_update=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Person(BaseModel):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=255, choices=GENDER)
    is_married = models.BooleanField(default=False)
    address = models.TextField()
    photo = models.ImageField(upload_to="person", null=True, blank=True)

    def __str__(self):
        return self.name

