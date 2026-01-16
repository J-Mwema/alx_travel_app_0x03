from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .tasks import send_booking_confirmation_email

# Dummy Booking model for demonstration (replace with your actual model)
from django.contrib.auth.models import User as Booking

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = None  # Replace with your BookingSerializer

    def create(self, request, *args, **kwargs):
        # Simulate booking creation (replace with actual logic)
        booking = Booking.objects.first()  # Dummy booking
        email = request.data.get('email', 'test@example.com')
        subject = 'Booking Confirmation'
        message = 'Your booking was successful!'
        # Trigger Celery email task
        send_booking_confirmation_email.delay(email, subject, message)
        return Response({'status': 'Booking created, confirmation email sent.'}, status=status.HTTP_201_CREATED)
