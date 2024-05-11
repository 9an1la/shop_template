from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.shop import views
from .views import Search
app_name = 'shop'


urlpatterns = [
    path('', views.home, name='home'),
    path('search/', Search.as_view(), name='search'),
    path('promotions', views.promotions),
    path('catalog', views.catalog, name='catalog'),
    path('about', views.about),
    path('catalog/<slug:subcategory_slug>', views.subcatalog_products, name='subcatalog_products'),
    path('<int:id>/<slug:slug>', views.product_detail, name='product_detail'),

    # ex: /polls/5/
    # path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)