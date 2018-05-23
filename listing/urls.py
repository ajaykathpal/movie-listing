from django.conf.urls import url
from .views import listing_index

urlpatterns = [

    url(r'', listing_index , name="listing_index"),
]
