from django.db import models
from django.contrib.auth.models import User

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.CharField(max_length = 256, blank=True)
    site = models.URLField(blank=True)
    picture = models.ImageField(upload_to='picture', blank=True)

    def __str__(self):
        return f'{self.user.last_name}, {self.user.first_name}'


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
