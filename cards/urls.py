from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("romantic-letter/", views.romantic_letter, name="romantic_letter"),
    path("love-declaration/", views.love_declaration, name="love_declaration"),
    path("heartfelt-poem/", views.heartfelt_poem, name="heartfelt_poem"),
    path("reasons-i-love-you/", views.reasons_i_love_you, name="reasons_i_love_you"),
    path("promise-ring/", views.promise_ring, name="promise_ring"),
    path("starlit-vows/", views.starlit_vows, name="starlit_vows"),
    path("our-love-story/", views.our_love_story, name="our_love_story"),
]
