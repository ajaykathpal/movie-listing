from django.conf.urls import url, include
from api.views import *


urlpatterns = [
 url(r'^movies/$',  MoviesListAPIView.as_view() )

]
