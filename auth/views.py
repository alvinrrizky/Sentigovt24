from django.shortcuts import render
from django.http import HttpResponse
# from .register_forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# def register(request):
#     context = {}
#     form = UserCreationForm(request.POST or None)
#     context['registered'] = False
#     if request.method == "POST":
#         if form.is_valid():
#             user = form.save()
#             return render(request, 'success-register.html')
#         else:
#             print(form.errors.as_data())
#     context['form'] = form
#     return render(request, 'register.html',context)
# # Create your views here.

# def regsuccess(request):
#     return render(request, 'success-register.html')

# @login_required
# def loginsuccess(request):
#     return render(request, 'success-login.html')

# class webLoginView(LoginView):
#     template_name = "login.html"
#     # redirect_authenticated_user = True

#     def form_invalid(self, form):
#         messages.error(self.request,'Invalid username or password')
#         return self.render_to_response(self.get_context_data(form=form))