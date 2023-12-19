from django.db.models import Model
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.


class Proyecto(Model):
    titulo = CharField(max_length=100)
    descripcion = CharField(max_length=250)
    imagen = ImageField(upload_to="porfolio/images/")
    url = URLField(blank=True)
