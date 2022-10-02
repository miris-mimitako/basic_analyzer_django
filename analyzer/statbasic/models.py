from enum import unique
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
    user_slug = models.SlugField(blank=True, null=True)

    def __str__(self) -> str:
        return self.user_name

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"slug": self.user_slug})

    def save(self, *args, **kwargs):
        if not self.user_slug:
            self.user_slug = slugify(self.user_name)
        return super().save(*args, **kwargs)

class CsvAnalyzer(models.Model):
    csv_file_name  = models.CharField(max_length=250, default="add_new_csv", unique=True)
    csv_comment = models.TextField(blank = True, null = True)
    csv_file_path = models.TextField(blank = True, null = True)
    csv_data_type = models.JSONField(blank = True, null = True)
    csv_analyze_selection = models.JSONField(blank = True, null = True)
    csv_analyze_record = models.JSONField(blank = True, null = True)
    csv_slug = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    revised_at = models.DateTimeField(auto_now_add = True)

    def get_absolute_url(self):
        return reverse("csv_detail", kwargs={"slug": self.csv_slug})

    def save(self, *args, **kwargs):
        if not self.csv_slug:
            self.csv_slug = slugify(self.csv_file_name)
        return super().save(*args, **kwargs)
