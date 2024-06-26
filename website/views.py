from django.shortcuts import render
from django.core.mail import send_mail


def home_page(request):
    return render(request, "website/home_page.html")


def about(request):
    return render(request, "website/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        # Send an Email
        send_mail(
            name,
            message,
            email,
            ["ace12351235@gmail.com", ],
        )

        return render(request, "website/contact.html", {"message": name})
    else:
        return render(request, "website/contact.html")


def appointment(request):
    return render(request, "website/appointment.html")


def book_appointment(request):
    if request.method == "POST":
        service = request.POST["service"]
        doctor = request.POST["doctor"]
        name = request.POST["name"]
        email = request.POST["email"]
        date = request.POST["date"]
        time = request.POST["time"]
        # Send an Email
        send_mail(
            f"{name}({doctor})",
            f"{date}-{time}",
            email,
            ["ace12351235@gmail.com", ],
        )
        return render(request, "website/book_appointment.html", {"name": name})
    else:
        return render(request, "website/home_page.html")
