from django.urls import path
from . import views
urlpatterns = [

    #CRUD Profile
    path("profile/add", views.add_profile, name="add_profile"),
    path("profile/all", views.list_profile, name="list_profile"),
    path("profile/delete/<profile_id>", views.delete_profile, name="delete_profile"),
    path("profile/update/<profile_id>", views.update_profile, name="update_profile"),
    path("prfile/get/<Profile_id>", views.get_profile, name="get_profile"),
    path("profile/", views.my_profile, name="my_profile"),
    # CRUD Comment
    path("comment/add", views.add_comment, name="add_comment"),
    path("comment/delete/<comment_id>", views.delete_comment, name="delete_comment"),
    path("comment/all", views.list_comment, name="list_comment"),
    path("comment/update/<comment_id>", views.update_comment, name="update_comment"),
    # CRUD Animal
    path("animal/add", views.add_Animal, name="add_Animal"),
    path("animal/delete/<Animal_id>", views.delete_Animal, name="delete_animal"),
    path("animal/all", views.list_Animal, name="list_animal"),
    path("animal/update/<Animal_id>", views.update_Animal, name="update_animal"),
    path("animal/get/<Animal_id>", views.get_animal, name="get_animal"),
    path("animal/", views.my_animals, name="get_animal"),#####################
    # CRUD Order
    path("order/add", views.add_Order, name="add_Order"),
    path("order/delete/<Order_id>", views.delete_Order, name="delete_Order"),
    path("order/all", views.list_Order, name="list_Order"),
    path("order/update/<Order_id>", views.update_Order, name="update_Order"),


]