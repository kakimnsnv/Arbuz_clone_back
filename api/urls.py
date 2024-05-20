# from django.urls import path
# from .views import ProductListCreateView, ProductDetailView, CartDetailView, SignUpView, LoginView

# urlpatterns = [
#     path('products/', ProductListCreateView.as_view(), name='product-list-create'),
#     path('products/<str:pk>/', ProductDetailView.as_view(), name='product-detail'),
#     path('cart/', CartDetailView.as_view(), name='cart-detail'),
#     path('signup/', SignUpView.as_view(), name='signup'),
#     path('login/', LoginView.as_view(), name='login'),
# ]

# ! fsdfsdf 

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import CollectionViewSet, ProductViewSet, CartViewSet, UserCreateView
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# router = DefaultRouter()
# router.register(r'products', ProductViewSet)
# router.register(r'carts', CartViewSet, basename='cart')
# router.register(r'collections', CollectionViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('signup/', UserCreateView.as_view(), name='signup'),
#     path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]

# ! sfsdfds


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CollectionViewSet, ProductViewSet, CartViewSet, UserCreateView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet, basename='cart')
router.register(r'collections', CollectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
