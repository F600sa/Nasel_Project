from django.urls import path
from . import views
urlpatterns = [

    path("profile/add", views.add_profile, name="add_profile"),
    path("profile/all", views.list_profile, name="list_profile"),
    path("profile/delete/<profile_id>", views.delete_profile, name="delete_profile"),
    path("profile/update/<profile_id>", views.update_profile, name="update_profile"),
    # CRUD Comment
    path("add/comment", views.add_comment, name="add_comment"),
    path("comment/delete/<comment_id>", views.delete_comment, name="delete_comment"),
    path("comment/all", views.list_comment, name="list_comment"),
    path("comment/all", views.list_comment, name="list_comment")]