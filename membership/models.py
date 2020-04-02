from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from library.models import BookInstance
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    staff = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("member-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.user.last_name}, {self.user.first_name}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Loan(models.Model):
    # make sure each book can be loaned ONCE at a time
    book = models.ForeignKey(BookInstance, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_loan = models.DateField(default=datetime.date.today())
    date_of_return = models.DateField(
        default=(datetime.date.today() + datetime.timedelta(weeks=3)))
    returned = models.BooleanField(default=False)
    @property
    def is_overdue(self):
        if self.date_of_return and datetime.date.today() > self.date_of_return:
            return True
        return False

    def __str__(self):
        return f'{self.book}, {self.user.username}'
