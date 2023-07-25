from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Bacapres
from .forms import BacapresForm
from django.contrib import messages
from sentigovt2.decorators import role_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from sentigovt2.mixin import RoleRequiredMixin
from django.views import View

class BacapresView(RoleRequiredMixin, View):
    required_roles = ['ADMIN', 'SUPERADMIN']
    context = {}
    context['active_page'] = 'bacapres management'

    def get(self, request):
        query = self.request.GET.get('search')
        if query:
            bacapres = Bacapres.objects.filter(name__icontains=query).order_by('id')
        else: 
            bacapres = Bacapres.objects.all().order_by('id')
        # pagination
        paginator = Paginator(bacapres, 10)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        data_items = []
        for item in page_obj:
            data_item = {
                'id': item.id,
                'name': item.name,
                'avatar': item.avatar.url,
            }
            data_items.append(data_item)

        self.context['total_pages'] = paginator.num_pages
        self.context['results'] = data_items
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse(self.context, safe=False)
        else:
            return render(request, 'bacapres/bacapresManagement.html', self.context)

    def post(self, request):
        form = BacapresForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ('Bacapres was succesfully added!'))
            return redirect(reverse_lazy('bacapres:bacapres_list'))
        else:
            messages.error(request, 'Error saving form')
            print(form.errors.as_data())
        self.context['form'] = form
        return render(request, 'bacapres/createBacapres.html', self.context)

    def delete(self, request, id):
        try:
            bacapres = get_object_or_404(Bacapres, id=id)
            bacapres.delete()
            return JsonResponse({'message': 'Data deleted successfully'})
        except Bacapres.DoesNotExist:
            return JsonResponse({'message': 'Invalid request method'})
    
class BacapresDetailView(RoleRequiredMixin, View):
    required_roles = ['ADMIN', 'SUPERADMIN']
    context = {}
    context['active_page'] = 'bacapres management'
    template_name = 'bacapres/editBacapres.html'

    def get(self, request,id):
        bacapres = get_object_or_404(Bacapres,id=id)
        form = BacapresForm(instance=bacapres)
        self.context['form'] = form
        self.context['object'] = bacapres
        return render(request, self.template_name, self.context)
    
    def post(self, request, id):
        bacapres = get_object_or_404(Bacapres,id=id)
        form = BacapresForm(request.POST,request.FILES, instance=bacapres)
        if form.is_valid():
            new_img = form.cleaned_data['avatar']
            if new_img:
                form.cleaned_data['avatar'] = Bacapres.objects.get(id=id).avatar
            form.save()
            return redirect(reverse_lazy('bacapres:bacapres_list'))
        else:
            print(form.errors.as_data())
            self.context['form'] = form
            self.context['object'] = bacapres
            return render(request, self.template_name, self.context)

class BacapresCreateView(RoleRequiredMixin, View):
    required_roles = ['ADMIN', 'SUPERADMIN']
    context = {}
    context['active_page'] = 'bacapres management'

    def get(self, request):
        form = BacapresForm()
        self.context['form'] = form
        return render(request,'bacapres/createBacapres.html', self.context)
    
    def post(self, request):
        form = BacapresForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ('Bacapres was succesfully added!'))
            return JsonResponse({"success": True}, status=200)
        else:
            errors = form.errors.get_json_data()
            print(errors)
            messages.error(request, 'Please correct the error below.')
            return JsonResponse(errors,status=400,safe=False)