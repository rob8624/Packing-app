from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    boxed = models.ForeignKey('Box', on_delete=models.CASCADE, related_name='items', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = slug = models.SlugField(unique_for_date='created')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Box(models.Model):
    number = models.PositiveSmallIntegerField(unique=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    additional = models.CharField(max_length=200, null=True, blank=True)

    boxes = models.Manager()

    def get_items(self):
        boxed = self.items.name
        print(boxed)
        return boxed

    def __str__(self):
        return (f"Box number {self.number}")


