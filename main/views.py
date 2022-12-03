from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, CreateView, UpdateView, ListView,DetailView
from main.forms import LoginForm, UserRegisterForm
from django.views.generic import ListView, DetailView, FormView


from main.forms import UserRegisterForm, UserUpdateForm

from .models import CollectionPlaces, Members, Partners, MaterialType

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import is_valid_path, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views import View

from .models import User


def index(request):
    return render(request, 'main.html')



def about(request):
    return render(request, 'about.html')




class UserCollectionPlacesView(LoginRequiredMixin, ListView):
    template_name = 'places.html'
    model = CollectionPlaces
    
    def get_queryset(self):
        queryset = self.model.objects.filter(user=self.request.user)
        return queryset



class CollectionPlacesView(ListView):
    template_name = 'places.html'
    model = CollectionPlaces

    def get_queryset(self):
        queryset = super().get_queryset()
        search_word = self.request.GET.get('search_word','')
        if search_word:
            queryset = CollectionPlaces.objects.filter(
                material_type__name__contains=search_word
            ).distinct().order_by('working_from')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_text"] = self.request.GET.get("query")
        return context



class CollectionPlacesDetailView(DetailView):
    template_name = 'place_detail.html'
    model = CollectionPlaces

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
        



class LatestEventsView(View):
    def get(self, request):
        return render(request, 'events.html')




class VolunteersView(View):
    def get(self, request):
        return render(request, 'volunteer.html')
    



class ContactsView(View):
    def get(self, request):
        return render(request, 'contacts.html')

    def post(self, request):
        fullname = request.POST.get('fullname')
        Members.objects.create(
            full_name=fullname
        )
        return render(request, 'contacts.html')





class UserLoginFormView(View):
    def get(self, request):
        return render(request, 'login.html', {'login':True})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff == True:
                login(request, user)
                response = redirect('index')
                return response
            login(request, user)
            response = redirect('index')
            return response
        else:
            response = redirect('login')
            return response

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("index")




class UserRegisterFormView(CreateView):

    def get(self, request):
        return render(request, 'login.html', {'register':True})
    
    def post(self, request):
        new_user = User.objects.create(
            username=request.POST.get('username', ''),
            first_name=request.POST.get('first_name', ''),
            last_name=request.POST.get('last_name', ''),
            email=request.POST.get('email', ''),
            phone=request.POST.get('tel', ''),
            address=request.POST.get('address', '')
        )
        password = request.POST.get('password', '')
        password1 = request.POST.get('password1', '')

        if password == password1:
            new_user.set_password(password)
            new_user.save()

        else:
            raise ValueError
        user = authenticate(username=new_user.username, password=password)
        
        if user is not None:
            login(request, user)
            response = redirect('index')
            return response
        else:
            return redirect('login')



class PartnersView(ListView):
    template_name = 'partners.html'
    model = Partners

    def get_queryset(self):
        return super().get_queryset()




class UserProfileView(DetailView):

    template_name = 'user_profile.html'
    model = User
    def get_object(self):
        return get_object_or_404(User, pk = self.request.user.id)




class PostCreate(CreateView):
    
    def get(self, request):
        return render(request, 'places.html')

    def post(self, request):
        new_post = CollectionPlaces.objects.create(
            author=request.POST.get('username', ''),
            image=request.POST.get('photo', ''),
            name=request.POST.get('name', ''),
            address=request.POST.get('address',''),
            phone=request.POST.get('tel', ''),
            working_from=request.POST.get('working_from', ''),
            working_to=request.POST.get('working_to', ''),
            material_type=request.POST.get('material_type', ''))



