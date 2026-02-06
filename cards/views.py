from datetime import datetime, date, time as dt_time
from django.shortcuts import render

RECIPIENT = "Nandita"
RECIPIENT_NICK = "My Heart"
SENDER = "Forever Yours"
SENDER_NICK = "Your Love"
MEMORY = "the day we first met"
FUTURE = "a lifetime of laughter and adventures"
START_DATE = date(2024, 11, 29)


def format_ordinal_day(day_value: int) -> str:
    if 11 <= day_value <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(day_value % 10, "th")
    return f"{day_value}{suffix}"


def build_context() -> dict:
    now = datetime.now()
    start_dt = datetime.combine(START_DATE, dt_time.min)
    delta = now - start_dt
    if delta.total_seconds() < 0:
        delta = delta.__class__(0)

    start_label = f"{format_ordinal_day(START_DATE.day)} {START_DATE.strftime('%B')}, {START_DATE.year}"
    story_days = delta.days
    love_counter = f"{story_days} days · {delta.seconds // 3600} hrs · {(delta.seconds % 3600) // 60} mins"

    recipient_display = RECIPIENT
    if RECIPIENT_NICK.lower() != RECIPIENT.lower():
        recipient_display = f"{RECIPIENT} ({RECIPIENT_NICK})"

    return {
        "recipient": RECIPIENT,
        "recipient_nick": RECIPIENT_NICK,
        "recipient_display": recipient_display,
        "sender": SENDER,
        "sender_nick": SENDER_NICK,
        "memory": MEMORY,
        "future": FUTURE,
        "start_label": start_label,
        "story_days": story_days,
        "love_counter": love_counter,
        "love_level": 1000,
        "today_label": now.strftime("%B %d, %Y"),
        "valentine_year": now.year,
    }


def romantic_letter(request):
    return render(request, "cards/romantic_letter.html", build_context())

def home(request):
    return render(request, "cards/home.html", build_context())


def love_declaration(request):
    return render(request, "cards/love_declaration.html", build_context())


def heartfelt_poem(request):
    return render(request, "cards/heartfelt_poem.html", build_context())


def reasons_i_love_you(request):
    return render(request, "cards/reasons_i_love_you.html", build_context())


def promise_ring(request):
    return render(request, "cards/promise_ring.html", build_context())


def starlit_vows(request):
    return render(request, "cards/starlit_vows.html", build_context())


def our_love_story(request):
    return render(request, "cards/our_love_story.html", build_context())
