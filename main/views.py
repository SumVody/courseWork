from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Car, Rental
from .forms import RegisterForm
from datetime import timezone, datetime

class sites:

    def index(request):
        return render(request, 'main/index.html', {'title': 'Головна'})

    def about(request):
        return render(request, 'main/about.html', {'title': 'Про нас'})

    def cars(request):
        cars = Car.objects.all()
        return render(request, 'main/cars.html', {'cars': cars})


    def register(request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()

            else:
                return render(request, 'main/register.html', {'form': form})

    @login_required
    def profile(request):
        rentals = Rental.objects.filter(user=request.user)
        return render(request, 'main/profile.html', {'rentals': rentals})

    @login_required
    def rent_car(request, id):
        car = get_object_or_404(Car, id=id)
        if not car.is_used:
            car.is_used = True
            car.save()
            Rental.objects.create(user=request.user, car=car)
        return redirect('main:cars')


    @login_required
    def end_rental(request, rental_id):
        rental = get_object_or_404(Rental, id=rental_id)
        if rental.user == request.user and not rental.end_date:
            rental.end_date = datetime.now(timezone.utc)
            rental.calculate_price()
            rental.save()
            rental.car.is_used = False
            rental.car.save()
            return render(request, 'main/end_rental.html', {'rental': rental})
        return redirect('main:profile')

    @login_required
    def pay_rental(request, rental_id):
        rental = get_object_or_404(Rental, id=rental_id)
        if rental.user == request.user and rental.end_date and rental.price is not None:
            rental.delete()
            return render(request, 'main/pay_rental.html')
        return redirect('main:end_rental', rental_id=rental.id)