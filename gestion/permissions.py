from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Admin').exists()

class IsEditorUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Editor').exists()

class ObjectPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('change_livre', obj)  # '