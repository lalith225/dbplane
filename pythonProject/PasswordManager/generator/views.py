from django.shortcuts import render
import random
import string


def home(request):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    all_chars = lowercase + uppercase + digits + special
    password_list = random.choices(all_chars, k=12)
    random.shuffle(password_list)
    final_password = ''.join(password_list)

    if request.method == 'POST':
        password_list = random.choices(all_chars, k=12)
        random.shuffle(password_list)
        final_password = ''.join(password_list)

    return render(request, "generator/home.html", {'password_generated': final_password})


def about(request):
    return render(request, "generator/about.html", {})
