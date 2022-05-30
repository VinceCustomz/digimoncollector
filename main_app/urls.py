from django.urls import path
from . import views

urlpatterns = [
    # General Routes
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Digimon Routes
    path('digimons/', views.digimons_index, name='index'),
    path('digimons/create/', views.DigimonCreate.as_view(), name='digimons_create'),
    path('digimons/<int:digimon_id>', views.digimons_details, name="detail"),
    path('digimons/<int:pk>/update', views.DigimonUpdate.as_view(), name='digimons_update'),
    path('digimons/<int:pk>/delete', views.DigimonDelete.as_view(), name='digimons_delete'),
    path('digimons/<int:digimon_id>/add_playtime', views.add_playtime, name='add_playtime'),
    
    # Associate pet with digimon
    path('digimons/<int:digimon_id>/assoc_pet/<int:pet_id>/', views.assoc_pet, name='assoc_pet'),

    # Unassociate pet with digimon
    path('digimons/<int:digimon_id>/unassoc_toy/<int:pet_id>/', views.unassoc_pet, name='unassoc_pet'),

    # Pets Routes
    path('pets/', views.PetList.as_view(), name='pets_index'),
    path('pets/<int:pk>/', views.PetDetail.as_view(), name='pets_detail'),
    path('pets/create/', views.PetCreate.as_view(), name='pets_create'),
    path('pets/<int:pk>/update/', views.PetUpdate.as_view(), name='pets_update'),
    path('pets/<int:pk>/delete/', views.PetDelete.as_view(), name='pets_delete'),

    # Authentication
    path('accounts/signup/', views.signup, name="signup")
]