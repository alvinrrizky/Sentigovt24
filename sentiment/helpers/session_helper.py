from accounts.models import Session

def isGuestLimitAccess(request):
    session_guest = request.COOKIES['session_guest']

    session = Session.objects.get(id=session_guest)
    print("isGuestLimitAccess",session)
    print(session)

    if session and not request.user.is_authenticated:
        if session.quota == 0:
            print(session.quota)
            return True
        else:
            session.quota = session.quota - 1
            session.save()
    print(session.quota)
    return False