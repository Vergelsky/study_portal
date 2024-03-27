from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderators').exists():
            return True

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        owner = view.get_object().owner
        return request.user == owner

