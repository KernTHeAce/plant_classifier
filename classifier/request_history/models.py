from django.db import models

from users.models import User
from classifier.dataset.models import Plant


class RequestHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/classifier/")
    response = models.ForeignKey(Plant, on_delete=models.DO_NOTHING)
