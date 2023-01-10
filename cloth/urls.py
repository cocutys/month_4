from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("cloth/", views.ClothListView.as_view(), name="cloth_list"),
    path("cloth/retro/", views.ClothListViewRetro.as_view(), name="retro_cloth_list"),
    path("cloth/unisex/", views.ClothListViewUnisex.as_view(), name="unisex_cloth_list"),
    path("cloth/male/", views.ClothListViewMale.as_view(), name="male_cloth_list"),
    path("cloth/female/", views.ClothListViewFemale.as_view(), name="female_cloth_list"),
    path("create_order/", views.OrderCreateView.as_view(), name="add-order"),
]