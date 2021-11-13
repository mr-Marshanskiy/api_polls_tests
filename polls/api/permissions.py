from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET']:
            return True
        else:
            return (request.user.is_staff)
