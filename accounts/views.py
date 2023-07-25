from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import logout
from .forms import SignUpForm, UpdateProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import User
from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator
from django.http import JsonResponse
from sentigovt2.mixin import RoleRequiredMixin

# Create your views here.

class AccountListView(RoleRequiredMixin,View):
    required_roles = ['ADMIN', 'SUPERADMIN']
    context = {}
    template_name = 'accounts/userManagement.html'
    context['active_page'] = 'user management'

    def get(self, request):
        # get user
        query = self.request.GET.get('search')
        if query:
            user = User.objects.filter(is_active=True,first_name__icontains=query).order_by('id')
            print(user)
        else:
            user = User.objects.all().filter(is_active=True).order_by('id')

        # pagination
        paginator = Paginator(user, 10)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        data_items = []
        for item in page_obj:
            data_item = {
                'id': item.id,
                'name': item.first_name,
                'role': item.role,
            }
            data_items.append(data_item)
        context = {
            'total_pages':paginator.num_pages,
            'results': data_items,
        }

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse(context, safe=False)
        else:
            return render(request, self.template_name, context)
        
    def post(self, request, id):
        try:
            user = User.objects.get(id=id)
            if user.is_active:
                user.is_active = False
            user.save()
            print(user.save())
            return redirect(reverse_lazy('account:userManagement'))
        except User.DoesNotExist:
            print("Object not found")
            return redirect(reverse_lazy('account:userManagement'))
        
class AccountDetailView(RoleRequiredMixin,View):
    required_roles = ['ADMIN', 'SUPERADMIN']
    context = {}
    template_name = 'accounts/editUser.html'
    context['active_page'] = 'user management'

    def get(self, request, id):
        user = get_object_or_404(User,id=id)
        self.context['user'] = user
        return render(request, self.template_name, self.context)
    
    def post(self, request, id):
        role = request.POST.get('selected_role')
        user = get_object_or_404(User,id=id)
        user.role = role
        user.save()
        return JsonResponse({"success": True}, status=200)
    
class UserProfileView(RoleRequiredMixin,View):
    required_roles = ['MEMBER','ADMIN', 'SUPERADMIN']
    context = {}
    template_name = 'accounts/profile.html'

    def get(self, request):
        auth_user = request.user
        user = get_object_or_404(User,id=auth_user.id)
        form = UpdateProfileForm(instance=user)
        self.context['form'] = form
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        auth_user = request.user
        user = get_object_or_404(User,id=auth_user.id)
        form = UpdateProfileForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.avatar = form.cleaned_data['avatar']
            if not user.avatar:
                user.avatar = User.objects.get(id=auth_user.id).avatar
            user.save()
            return JsonResponse({"success": True}, status=200)
        else:
            errors = form.errors.get_json_data()
            print(errors)
            return JsonResponse(errors,status=400,safe=False)

class RegisterView(View):
    context = {}
    template_name = 'accounts/register.html'

    def get(self, request):
        form = SignUpForm()
        self.context['form'] = form
        return render(request, self.template_name,self.context)
    
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect(reverse_lazy('dashboard'))
        else:
            print(form.errors.as_data())
            self.context['form'] = form
            return render(request, 'accounts/register.html',self.context)

class LoginView(View):
    context = {}
    template_name = 'accounts/login.html'

    def get(self, request):
        self.context['verified'] = True
        return render(request, self.template_name, self.context)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  
        else:
            self.context['verified'] = False
            return render(request, self.template_name, self.context)
        
class ChangePasswordView(View):
    context = {}
    template_name = 'accounts/profile.html'

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return JsonResponse({'message': 'Form submitted successfully'})
        else :
            errors = form.errors.get_json_data()
            print(errors)
            messages.error(request, 'Please correct the error below.')
            return JsonResponse(errors,status=400,safe=False)
# FBV #

def logoutRequest(request):
    logout(request)
    print("berhasil logout")
    return redirect(reverse_lazy('home'))

