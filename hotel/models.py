from django.db import models

# Create your models here.
class Room(models.Model):
    Room_types=(('one', 'single'),
                ('two', 'double'),
                ('multi','family'),
    )
    category = models.CharField(choices=Room_types, max_length=6)
    number = models.IntegerField()
    capacity = models.IntegerField()
    beds = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} people'

