"""URL paths for Organizer App"""
from django.urls import path

from .views import (
    StartupCreate,
    StartupDetail,
    StartupList,
    StartupUpdate,
    TagCreate,
    TagDelete,
    TagDetail,
    TagList,
    TagUpdate,
)

urlpatterns = [
    path(
        "startup/",
        StartupList.as_view(),
        name="startup_list",
    ),
    path(
        "startup/create/",
        StartupCreate.as_view(),
        name="startup_create",
    ),
    path(
        "startup/<str:slug>/",
        StartupDetail.as_view(),
        name="startup_detail",
    ),
    path(
        "startup/<str:slug>/update/",
        StartupUpdate.as_view(),
        name="startup_update",
    ),
    path("tag/", TagList.as_view(), name="tag_list"),
    path(
        "tag/create/",
        TagCreate.as_view(),
        name="tag_create",
    ),
    path(
        "tag/<str:slug>/",
        TagDetail.as_view(),
        name="tag_detail",
    ),
    path(
        "tag/<str:slug>/update/",
        TagUpdate.as_view(),
        name="tag_update",
    ),
    path(
        "tag/<str:slug>/delete/",
        TagDelete.as_view(),
        name="tag_delete",
    ),
]
