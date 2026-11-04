from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Mengizinkan akses baca (GET, HEAD, OPTIONS) untuk siapa saja
        if request.method in SAFE_METHODS:
            return True
        
        # Tolak semua akses ubah jika pengguna belum login
        if not request.user.is_authenticated:
            return False
            
        # Superuser diizinkan melakukan semua tindakan (POST, PUT, PATCH, DELETE)
        if request.user.is_superuser:
            return True
            
        # Editor hanya diizinkan melakukan ubah data (PUT, PATCH)
        return (
            request.method in ("PUT", "PATCH")
            and request.user.groups.filter(name="Editor").exists()
        )