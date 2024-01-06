from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from e_auth.views.user_views import UserViewSet, Login, Logout

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login/', Login.as_view(), name='login'),
    path('api/logout/', Logout.as_view(), name='logout'),
    path('api/', include('e_products.urls')),
]
