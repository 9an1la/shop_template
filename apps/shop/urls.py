from django.urls import path

from apps.shop import views

urlpatterns = [
    path('', views.home, name='home'),
    path('promotions', views.promotions),
    path('catalog', views.catalog),
    path('about', views.about),
    path('catalog/<str:pk>', views.subcatalog_products, name='subcatalog_products')
    # ex: /polls/5/
    # path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]
