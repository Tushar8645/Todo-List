from django.db import models


class List(models.Model):
    item = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item

    class Meta:
        verbose_name = "List"
        verbose_name_plural = "Lists"
