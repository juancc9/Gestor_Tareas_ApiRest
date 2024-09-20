from .views import TareaViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'tareas',TareaViewSet)

urlpatterns =[
    path('',include(router.urls))
]