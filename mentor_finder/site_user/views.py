from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import LoginForm, RegisterForm
from mentor_finder.site_user.models import SiteUser, Personality
from mentor_finder.industry.models import Industry

def login_view(request, *args, **kwargs):
    if request.method == 'GET':
        if request.user.is_anonymous:
            page = 'form.html'
            end_point = 'login'
            button_label = 'Login'
            form = LoginForm()
            user = None
            
            return render(request, page, {'user': user,'form': form, 'button_label': button_label})
        else:
            return HttpResponseRedirect(reverse('login'))
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = authenticate(
                username=data['username'], password=data['password'])
            if u is not None:
                login(request, u)
            else:
                page = 'form.html'
                error_message = 'Username or password is incorrect.'
                end_point='login'
                form = LoginForm()
                return render(request, page, {'form': form, 'end_point': end_point, 'error_message': error_message})

            destination = request.GET.get('next')
            if destination:
                return HttpResponseRedirect(destination)
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        return HttpResponseRedirect(reverse('homepage'))


def register_view(request, *args, **kwargs):
    if request.method == 'GET':
        if request.user.is_anonymous:
            page = 'form.html'
            end_point = 'register'
            button_label = 'Submit'
            form = RegisterForm()
            not_logged_in = True

            return render(request, page, {'form': form, 'button_label': button_label})
        else:
            return HttpResponseRedirect(reverse('homepage'))

    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = User.objects.create_user(
                username=data['username'],
                password=data['password'],
                email=data['email']
            )

            personality = Personality.objects.get(title=data['personality'])
            industry = Industry.objects.get(title=data['industry'])
            site_user = SiteUser.objects.create(
                user=u,
                personality=personality,
                industry=industry,
                is_mentor=data['is_mentor']
            )

            return HttpResponseRedirect(reverse('login'))