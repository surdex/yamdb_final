from rest_framework import permissions


class IsAuthAdmModerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user == obj.author
            or request.user.is_moderator
            or request.user.is_admin
            or request.user.is_superuser
        )


class AdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and (
            request.user.is_superuser or request.user.is_admin
        ):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and (
            request.user.is_superuser or request.user.is_admin
        ):
            return True
        return False


class IsUserIsAdmin(permissions.BasePermission):
    message = 'The user must have the admin status!'

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and (request.user.is_superuser or request.user.is_admin)
        )
