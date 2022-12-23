from django.db import models
from django.conf import settings

# Create your models here.
class Room(models.Model):
    ROOM_CATEGORIES = (
            ('single', 'one'),
            ('double', 'two'),
            ('family','multi'),
    )
    category = models.CharField(choices=ROOM_CATEGORIES, max_length=6)
    number = models.IntegerField()
    capacity = models.IntegerField()
    beds = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} people'

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_out = models.DateTimeField()
    check_in = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked  {self.room} from {self.check_in} to {self.check_out}'

