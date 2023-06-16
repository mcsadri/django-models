from django.db import models
from django.contrib.auth import get_user_model


# each class = a table in db
class Snack(models.Model):
    # class vars for each table col/field using Model Field Reference (field types + field options (keyword arguments))
    name = models.CharField(max_length=256)
    rating = models.IntegerField(default=0)
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
