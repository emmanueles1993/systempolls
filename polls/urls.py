from django.urls import URLPattern, path

from . import views
app_name = "polls"
urlpatterns = [
    #example /polls/
    path("", views.index, name="index"),
    #example /polls/5/
    path("<int:question_id>/detail/estaeslamejorpagina", views.detail, name="detail"),
    #ex: /polls/results
    path("<int:question_id>/results/", views.results, name="results"),
    #ex /polls/5/vote
    path("<int:question_id>/vote", views.vote, name="vote"),

]