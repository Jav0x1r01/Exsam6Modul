from django.db.models import Model, CharField,ImageField, ForeignKey, CASCADE
from django_resized import ResizedImageField


class UserModel(Model):
    name=CharField(max_length=255)
    position=ForeignKey('apps.Position', CASCADE, 'position')
    image = ImageField()
    facebook=CharField(max_length=255,default='#')
    twitter=CharField(max_length=255,default='#')
    linkedin=CharField(max_length=255,default='#')

    def __str__(self):
        return self.name

class Position(Model):
    name=CharField(max_length=255)

    def __str__(self):
        return self.name