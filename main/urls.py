from django.urls import path
# from main.views import LoginView, UserRegisterView, UpdateUserView, UserProfileView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about_us'),
    path('collection_places/', views.CollectionPlacesView.as_view(), name='places'),
    path('latest_events/', views.LatestEventsView.as_view(), name='events'),
    path('volunteers/', views.VolunteersView.as_view(), name='volunteers'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('collection_places/<int:pk>/', views.CollectionPlacesDetailView.as_view(), name='place_detail'),
    path('sign_in/',views.UserLoginFormView.as_view(), name = 'login'),
    path('registration/',views.UserRegisterFormView.as_view(), name = 'registration'),
    path('logout/', views.logout_user, name = "logout"),
    path('partners/',views.PartnersView.as_view(), name = 'partners'),
    path('my_profile/', views.UserProfileView.as_view(), name = 'user_profile'),
    path('my_places', views.UserCollectionPlacesView.as_view(), name = 'my_places'),
    path('post/', views.PostCreateView.as_view(), name = 'post'),
    # path('collection_places/post/', views.PostCreateView.as_view(), name='post'),
]