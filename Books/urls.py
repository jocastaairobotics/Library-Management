from django.urls import path
from .views import AuthorListView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView

urlpatterns = [
    path("authorlist", AuthorListView.as_view(), name="AuthorListView"),
    path("create", AuthorCreateView.as_view(), name="AuthorCreateView"),
    path("<pk>/update", AuthorUpdateView.as_view(), name="AuthorUpdateView"),
    path("<pk>/delete", AuthorDeleteView.as_view(), name="AuthorDeleteView"),
]