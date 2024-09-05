from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.


monthly_challenges = {
    "january": "Play Football!",
    "february": "Go Walking!",
    "march": "Drink More Water!",
    "april": "Do Nothing! HaHa april fools Go Study!",
    "may": "Play Video Games!",
    "june": "Eat fresh fruits every day",
    "july": "Learn foreign languages",
    "august": "Follow a bedtime routine",
    "september": "Walk 10,000 steps every day",
    "october": "Brush your teeth twice a day",
    "november": "Meditate",
    "december": "It's Your Birthday!! :) ",
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request,"challenges/index.html",{
        "months":months
    })


def monthly_challenge_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("monthly-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html",{
            "text": challenge_text,
            "month_name": month
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)