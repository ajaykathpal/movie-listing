from django.shortcuts import render,get_object_or_404
from .models import Movies

# Create your views here.
def listing_index(request):
    return render(request,'listing/listing_index.html',{'movies':get_object_or_404(Movies,pk=1)})
