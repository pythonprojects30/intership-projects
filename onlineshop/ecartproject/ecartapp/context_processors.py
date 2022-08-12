from .models import Category
def menulinks(request):
     link=Category.objects.all()
     return dict(link=link)