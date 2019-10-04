from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.models import User

from mentor_finder.site_user.models import SiteUser
from mentor_finder.goal.models import Goal

class dashboard(TemplateView):
    def get(self, request, *args, **kwargs):
        u = User.objects.get(username=request.user)
        user = SiteUser.objects.get(user=u)
        goals = Goal.objects.filter(assigned_to=user)
        for goal in goals:
            print(goal.tasks)
        page = 'dashboard.html'

        return render(request, page, {'goals': goals})
