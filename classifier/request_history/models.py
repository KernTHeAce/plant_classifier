from django.db import models

from users.models import User
from classifier.dataset.models import PlantInfo, Label


class RequestHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/classifier/")
    info = models.ForeignKey(PlantInfo, on_delete=models.DO_NOTHING)
    label = models.ForeignKey(Label, on_delete=models.DO_NOTHING, null=True)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.info.name}:{self.label.value}"
