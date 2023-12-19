from django.shortcuts import get_object_or_404, render
from .models import Publicacion


# Create your views here.
def posts(request):
    publicaciones = Publicacion.objects.all()
    return render(request, "posts.html", {"publicaciones": publicaciones})


def post_detail(request, post_id):
    publicacion = get_object_or_404(Publicacion, pk=post_id)
    return render(request, "post_detail.html", {"publicacion": publicacion})
