from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False

class IsGETORPOSTOrPUT(BasePermission):
    def has_permission(self, request, view):
        allowed_methods = ['GET','PUT','POST',]
        if request.method in allowed_methods:
            return True
        else:
            return False


class RolePermission(BasePermission):
    def has_permission(self, request, view):
        staff_status = request.user.is_staff
        if staff_status == True:
            allowed_methods = ['GET','POST', 'PUT', 'DELETE']
            if request.method in allowed_methods:
                return True
            return False
        else:
            allowed_methods = ['GET',]
            if request.method in allowed_methods:
                return True
            return False
            