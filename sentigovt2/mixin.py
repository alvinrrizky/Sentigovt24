from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden

class RoleRequiredMixin(UserPassesTestMixin):
    required_roles = []

    def test_func(self):
        user = self.request.user
        return user.is_authenticated and user.role in self.required_roles

    def handle_no_permission(self):
        return HttpResponseForbidden("You don't have permission to access this page.")