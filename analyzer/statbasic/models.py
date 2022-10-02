from django.db import models

# Create your models here.
from django.urls import reverse
from django.template.defaultfilters import slugify  


# Register your models here.
class User(models.Model):
    user_name = models.CharField(max_length=250, default="noname_user")
    user_email = models.EmailField(max_length=250)
    user_profiel = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    revised_at = models.DateTimeField(auto_now_add=True)
    post_user_slug = models.SlugField(blank=True, null=True)

    def __str__(self) -> str:
        return self.user_name

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"slug": self.post_user_slug})

    def save(self, *args, **kwargs):
        if not self.post_user_slug:
            self.post_user_slug = slugify(self.user_name)
        return super().save(*args, **kwargs)
