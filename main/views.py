from django.shortcuts import render, redirect
from .forms import DriverForm, CustomerForm
from django.contrib import messages


# Homepage
def landing_page(request):
    return render(request, 'main/landing_page.html')

# Customer Page
def customer_page(request):
    # Handle Form Submission
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data saved successfully")
            return redirect("landing_page")
    else:
        form = CustomerForm()

    context = {
        "form": form,
    }
    return render(request, 'main/customer_page.html', context)

# Driver Page
def driver_page(request):
    # Handle Form Submission
    if request.method == "POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data saved successfully")
            return redirect("landing_page")
    else:
        form = DriverForm()

    context = {
        "form": form,
    }
    return render(request, 'main/driver_page.html', context)