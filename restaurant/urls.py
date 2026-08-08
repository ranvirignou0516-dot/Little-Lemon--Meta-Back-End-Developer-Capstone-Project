from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.BookingViewSet, basename='booking')

urlpatterns = [

    path('', views.home, name='home'),
    path('menu-page/', views.menu_page, name='menu-page'),
    path('book/', views.booking_page, name='booking-page'),
    
    path('menu/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),

    path('booking/', include(router.urls)),
    
    path('logout/', views.logout_view, name='logout'),
]