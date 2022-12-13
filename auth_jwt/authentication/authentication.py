from rest_framework import permissions

class AuthIsPOST(permissions.BasePermission):
    """ permite hacer post sin estar logueado """
    def has_permission(self, request, view):
        if (not request.user.username) & (request.method == "POST"):
            return True
        else:
            return bool(request.user and request.user.is_authenticated)