def authenticated_user(request):
    user = request.user if request.user.is_authenticated else None
    return {
        'auth_user': user,
    }