from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login

from .models import Author


def registerView(request):
    """ثبت‌نام کاربر جدید در سیستم."""

    if request.method == "POST":
        username = request.POST.get("reg_username")
        password1 = request.POST.get("reg_password1")
        password2 = request.POST.get("reg_password2")

        if password1 != password2:
            messages.error(request, "پسوردها باید مطابقت داشته باشند")

        elif Author.objects.filter(username=username).exists():
            messages.error(request, "کاربر از قبل وجود دارد")
            return redirect("register")

        elif username and password1 and password1 == password2:
            user = Author.objects.create_user(
                username=username,
                password=password1,
            )
            login(request, user)
            return redirect("home")

    return render(request, template_name="account/register.html")
