from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView

from food_ordering_system_app.models import CustomerDetails
# Create your views here.
class HomeInterfaceView(TemplateView):
    template_name = "home.html"

class MenuView(TemplateView):
    template_name = "food_ordering_system_app/menu.html"

class FoodMenuView(TemplateView):
    template_name = "food_ordering_system_app/food_menu.html"

class AboutusView(TemplateView):
    template_name = "food_ordering_system_app/aboutus.html"

class ContactsView(TemplateView):
    template_name = "food_ordering_system_app/Contacts.html"

class ReviewsView(TemplateView):
    template_name = "food_ordering_system_app/reviews.html"

class PhotoView(TemplateView):
    template_name = "food_ordering_system_app/photo.html"

class TablebookingView(TemplateView):
    template_name = "food_ordering_system_app/tablebooking.html"

class Food_DetailsView(TemplateView):
    template_name = "food_ordering_system_app/food_details.html"

class Shipping_DetailsView(CreateView):
    # form_class = Shipping_DetailsForm
    model = CustomerDetails
    fields = (
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "Address",
        "Quantity",
        
    )
    template_name = "food_ordering_system_app/shipping_details.html"
    # success_url = reverse_lazy("login")

    # To redirect to dashboard if user is already logged in
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("dashboard")
        return super().get(request, *args, **kwargs)
class PaymentView(TemplateView):
    template_name = "food_ordering_system_app/payment.html"

class Post_PaymentView(TemplateView):
    template_name = "food_ordering_system_app/post_payment.html"