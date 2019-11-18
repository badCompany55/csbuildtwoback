"""csback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.api import MapViewSet, TokenObtainPairPatchedView, UpdateStatsAPI, RunLootAPI, ChangeNameAPI

# from rest_framework_simplejwt import views

router = routers.DefaultRouter()
router.register("map", MapViewSet)
router.register("status", UpdateStatsAPI)
router.register("loot", RunLootAPI, basename="Loot")
router.register("namechange", ChangeNameAPI, basename="changename")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path("api/token/", TokenObtainPairPatchedView.as_view()),
]
