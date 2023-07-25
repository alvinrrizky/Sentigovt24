from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse
from functools import wraps

def role_required(allowed_roles):
    def decorator(view_func):

        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            # Check if user is authenticated
            if not request.user.is_authenticated:
                return redirect('account:login')
            
            # Retrieve the user's role from your custom user model or user profile
            user_role = request.user.role

            # Check if the user's role is allowed to access the view
            if user_role not in allowed_roles:
                # Redirect the user to a custom page or return a forbidden response
                return HttpResponseRedirect(reverse('account:login'))
            return view_func(request, *args, **kwargs)
        return wrapped_view
    return decorator