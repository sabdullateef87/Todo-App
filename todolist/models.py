from django.db import models

# Create your models here.
from django.utils import timezone

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    name = models.TextField(max_length=100)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name

class TodoList(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    class Meta:
        ordering = ["-created"]
    def __str__(self):
        return self.title
