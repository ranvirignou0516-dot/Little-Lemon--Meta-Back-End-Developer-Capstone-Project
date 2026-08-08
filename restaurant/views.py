from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsManager

from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.shortcuts import render
def home(request):
    return render(request, 'index.html')


def menu_page(request):
    menu_items = Menu.objects.all()
    return render(request, 'menu.html', {
        'menu_items': menu_items
    })


def booking_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        no_of_guests = request.POST.get('no_of_guests')
        booking_date = request.POST.get('booking_date')

        if name and no_of_guests and booking_date:
            Booking.objects.create(
                name=name,
                no_of_guests=no_of_guests,
                booking_date=booking_date
            )

            return render(request, 'booking.html', {
                'success': 'Your table has been booked successfully!'
            })

        return render(request, 'booking.html', {
            'error': 'Please fill in all fields.'
        })

    return render(request, 'booking.html')
# Menu List (GET, POST)
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsManager()]
        return []


# Single Menu Item (GET, PUT, DELETE)
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAuthenticated(), IsManager()]
        return []


# Booking API
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

# Logout API
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    Token.objects.filter(user=request.user).delete()
    return Response({"message": "Logged out successfully"})

