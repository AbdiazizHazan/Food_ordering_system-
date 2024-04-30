from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeInterfaceView.as_view(), name="home"),
    path("menu/", views.MenuView.as_view(), name="menu"),
    path("food_menu/", views.FoodMenuView.as_view(), name="food_menu"),
    path("aboutus/", views.AboutusView.as_view(), name="aboutus"),
    path("Contacts/", views.ContactsView.as_view(), name="Contacts"),
    path("reviews/", views.ReviewsView.as_view(), name="reviews"),
    path("photo/", views.PhotoView.as_view(), name="photo"),
    path("tablebooking/", views.TablebookingView.as_view(), name="tablebooking"),
    path("food_details/", views.Food_DetailsView.as_view(), name="food_details"),
    path("shipping_details/", views.Shipping_DetailsView.as_view(), name="shipping_details"),
    path("payment/", views.PaymentView.as_view(), name="payment"),
    path("post_payment/", views.Post_PaymentView.as_view(), name="post_payment"),


]