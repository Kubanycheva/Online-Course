from rest_framework import permissions

class CheckStatus(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'администратор' 'преподаватель':
            return True
        return False