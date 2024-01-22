from django.db import models
from django.contrib.auth import settings


class AirLine(models.Model):
    code = models.CharField(max_length=3, unique=True)


class Location(models.Model):
    from_airport = models.CharField(max_length=20)
    to_airport = models.CharField(max_length=20)
    from_city = models.CharField(max_length=10)
    to_city = models.CharField(max_length=10)


class Passenger(models.Model):

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    ticket = models.OneToOneField('Ticket', on_delete=models.CASCADE, related_name='passenger_tickets')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} {self.gender}'

    class Meta:
        ordering = ['first_name', 'last_name']


class Ticket(models.Model):

    CLASSES = [
        ('economy', 'Economy'),
        ('economy_plus', 'Economy Plus'),
        ('business', 'Business'),
        ('vip', 'VIP'),
    ]
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE, related_name='passenger_tickets', null=True)
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE)
    takeoff_date = models.DateTimeField(auto_now_add=True)
    ticket_price = models.DecimalField(max_digits=5, decimal_places=2)
    ticket_class = models.CharField(choices=CLASSES, max_length=15)
    seat_number = models.IntegerField()

    def __str__(self):
        return f'{self.flight} {self.takeoff_date} {self.ticket_class} {self.seat_number}'


class Flight(models.Model):
    passengers = models.ManyToManyField('Passenger', related_name='flights')
    tickets = models.ManyToManyField('Ticket', related_name='flights')
    location = models.ManyToManyField(Location)
    date = models.DateTimeField(auto_now_add=True)
    flight_num = models.CharField(max_length=10)
    departure_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    return_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    company = models.CharField(max_length=30, default=" ")
    seats = models.IntegerField()

    def __str__(self):
        return f'{self.location} {self.date}'


class Timetable(models.Model):
    from_airport = models.CharField(max_length=20)
    to_airport = models.CharField(max_length=20)
    departure_date = models.DateTimeField()
    return_date = models.DateTimeField()



