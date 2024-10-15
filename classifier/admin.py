from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Label, PlantInfo, PlantImage, Plant, Dataset

admin.site.register(Label)


class PromoImageInline(admin.StackedInline):
    model = PlantImage
    min_num = 1
    max_num = 3


class PlantInline(admin.StackedInline):
    model = Plant
    min_num = 2


@admin.register(PlantInfo)
class PlantInfoAdmin(admin.ModelAdmin):
    inlines = (PromoImageInline, )

    list_display = ("preview", "name", "full_name")

    def preview(self, obj):
        if obj.images.exists():
            first_image = obj.images.all()[0]
            try:
                return mark_safe(f'<img src="{first_image.image.url}" height="80">')
            except ValueError:
                first_image.delete()
                return "[no image]"
        else:
            return "[no image]"


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    inlines = (PlantInline, )
    list_display = ("name", 'get_num_classes', "is_active",)

    def get_num_classes(self, obj):
        return len(obj.plants.all())

    get_num_classes.short_description = 'Number of classes'
