from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """اجازه فقط برای نویسنده در متدهای ویرایش/حذف."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class IsSuperUserOrReadOnly(permissions.BasePermission):
    """اجازه کامل فقط برای سوپر یوزرها."""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser
