from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mail_id = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    date_of_birth = models.DateField()
    mailing_address = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.first_name + " " + self.last_name