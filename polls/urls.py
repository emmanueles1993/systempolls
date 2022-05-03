from django.urls import URLPattern, path

from . import views
app_name = "polls"
urlpatterns = [
    #example /polls/
    path("", views.Indexview.as_view(), name="index"),
    #example /polls/5/
    path("<int:pk>/detail/estaeslamejorpagina", views.Detailview.as_view(), name="detail"),
    #ex: /polls/results
    path("<int:pk>/results/", views.Resultview.as_view(), name="results"),
    #ex /polls/5/vote
    path("<int:question_id>/vote", views.vote, name="vote"),

]