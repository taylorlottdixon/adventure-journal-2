import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Campaign, Monster, Item, PlayerCharacter, NPC, Encounter, System

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def campaigns_index(request):
    my_campaigns = Campaign.objects.filter(user=request.user)
    player_campaigns = Campaign.objects.filter(player=request.user)
    return render(request, 'campaigns/index.html', {
        'my_campaigns': my_campaigns,
        'player_campaigns': player_campaigns,
    })

def campaigns_detail(request, campaign_id):
    campaign = Campaign.objects.get(id=campaign_id)
    return render(request, 'campaigns/detail.html', {
        'campaign': campaign,
    })

class CampaignCreate(LoginRequiredMixin, CreateView):
    model = Campaign

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CampaignUpdate(LoginRequiredMixin, CreateView):
    model = Campaign

class CampaignDelete(LoginRequiredMixin, CreateView):
    model = Campaign

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
        # This will add the user to the database
            user = form.save()
        # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)