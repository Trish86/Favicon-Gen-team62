from xml.etree.ElementInclude import include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path

from Favitude import views

router = DefaultRouter
router.register(" ", views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('api-auth/', include('rest_framework.urls'))

]


urlpatterns += router.urls

