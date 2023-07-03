from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Python 4 fours a day",
    "april": "Do 100 push-ups every day!",
    "may": "Make online lessons!",
    "june": "Read self-development books",
    "july": "Make money!",
    "august": "Go to Tashkent!",
    "september": "Work and Study at the same time!",
    "october": "Run every day!",
    "november": "Do not drink fizzy drinks",
    "december": None,
}

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenge_text, "month_name": month},
        )
    except:
        raise Http404()
