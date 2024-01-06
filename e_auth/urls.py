# # from django.urls import path, include
# # from rest_framework import routers
# # from e_auth.views.user_views import UserViewSet, Login
# #
# # # ModelViewSet router
# # ecommerce_router = routers.DefaultRouter()
# #
# # # Register UserViewSet with the router
# # ecommerce_router.register('users', UserViewSet)
# #
# # # Include router's URLs along with the custom login URL
# # urlpatterns = [
# #     # Include the router's URLs under the 'api/' path
# #     path('api/', include(ecommerce_router.urls)),
# #     path('api/login/', Login.as_view(), name='login'),
# # ]
#
#
# # from django.urls import path
# # from e_auth.views.user_views import UserViewSet, Login
# #
# # urlpatterns = [
# #     path('login/', Login.as_view(), name='login'),  # Use a relative path for login
# #     path('users/', UserViewSet.as_view(), name='user-list'),
# #
# # ]
# # project/urls.py
# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from e_auth.views.user_views import UserViewSet, Login
#
# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
#     path('login/', Login.as_view(), name='login'),
# ]
