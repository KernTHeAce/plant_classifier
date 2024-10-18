from django.db import models
from django.db.models import Q


class Label(models.Model):
    value = models.SmallIntegerField(unique=True)

    def __str__(self):
        return str(self.value)


class PlantInfo(models.Model):
    name = models.CharField(max_length=70)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class PlantImage(models.Model):
    promo = models.ForeignKey(PlantInfo, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="media/classifier/")

    def __str__(self):
        return self.promo.name


class Dataset(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if kwargs.get("is_active"):
            Dataset.objects.all().update({"is_active": False})
        super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        if self.is_active:
            Dataset.objects.filter(~Q(id=self.id)).update(is_active=False)


class Plant(models.Model):
    label = models.ForeignKey(Label, on_delete=models.DO_NOTHING)
    info = models.ForeignKey(PlantInfo, on_delete=models.DO_NOTHING)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name="plants", null=True, blank=True)

    class Meta:
        unique_together = (("label", "dataset"), )
