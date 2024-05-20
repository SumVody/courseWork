from datetime import timezone, datetime
from django.contrib.auth.models import User
from django.db import models

class BodyType(models.Model):
    title = models.CharField("Тип кузова", max_length=255)

    def __str__(self):
        return self.title

class Car(models.Model):
    name = models.TextField("Назва авто")
    year = models.IntegerField("Рік випуску")
    volume = models.FloatField("Об'єм двигуна")
    power = models.IntegerField("Потужність(к.с)")
    sing_of_car = models.CharField("Номер авто", max_length=255)
    body_type = models.ForeignKey(BodyType, verbose_name="Тип кузова", on_delete=models.CASCADE)
    is_fixing = models.BooleanField("В ремонті:", default=False)
    is_used = models.BooleanField("Використовується:", default=False)

    def __str__(self):
        return f"{self.name}"

class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=datetime.now(timezone.utc))
    end_date = models.DateTimeField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.car.name}"

    def calculate_price(self):
        if self.end_date:
            duration = self.end_date - self.start_date
            hours = duration.total_seconds() / 3600
            self.price = hours * 25
            self.save()