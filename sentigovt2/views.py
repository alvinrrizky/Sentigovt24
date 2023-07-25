from django.shortcuts import render
from django.http import HttpResponse
from sentiment.models import Bacapres
import uuid
from accounts.models import Session
from django.views import View


def home(request):
    
    return render(request, 'home.html')

class DashboardView(View):
    context = {}
    template_name = "dashboard.html"
    context['title'] = 'Dashboard'
    context['active_page'] = 'dashboard'

    def get(self, request):
        # set session for guest
        rendered_html = render(request, self.template_name, self.context)
        session_guest = request.COOKIES.get('session_guest')
        if session_guest:
            response = HttpResponse(rendered_html)
        else:
            response = HttpResponse(rendered_html)
            
            unique_id = str(uuid.uuid4())
            session_age = 3600 * 24 * 90 # 3 months
            response.set_cookie('session_guest', unique_id, max_age=session_age)
            Session.objects.create(id=unique_id)

        # clear all session from other view
        if 'selected_start_date' in request.session:
            del request.session['selected_start_date']
    
        if 'selected_end_date' in request.session:
            del request.session['selected_end_date']
            
        if 'selected_options' in request.session:
            del request.session['selected_options']
        
        if 'history_id' in request.session:
            del request.session['history_id']
        
        request.session.modified = True

        return response