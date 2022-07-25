from django.urls import path
from . import views
urlpatterns = [

    #CRUD Profile
    path("profile/add", views.add_profile, name="add_profile"),
    path("profile/all", views.list_profile, name="list_profile"),
    path("profile/delete/<profile_id>", views.delete_profile, name="delete_profile"),
    path("profile/update/<profile_id>", views.update_profile, name="update_profile"),
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
    # CRUD Order
    path("order/add", views.add_Order, name="add_Order"),
    path("order/delete/<Order_id>", views.delete_Order, name="delete_Order"),
    path("order/all", views.list_Order, name="list_Order"),
    path("order/update/<Order_id>", views.update_Order, name="update_Order"),
    #Test CRUD

<<<<<<< HEAD
=======
    # path("profilee/update/<slug>",views.update_profilee,name="update_profilee"),
    # path("profilee/delete/<slug>",views.test_delete_profile,name="test_delete_profile"),
    # path('profile-details/<user_id>',views.profile_details,name='profile-details'),


    # path("profilee/update/<slug>",views.update_profilee,name="update_profilee"),
    # path("profilee/delete/<slug>",views.test_delete_profile,name="test_delete_profile")

>>>>>>> 3e190d4c73d2c70f5adbf1f7ddbcd39f58b418d5



]