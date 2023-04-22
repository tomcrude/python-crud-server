from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('userReviews/<str:id>/<str:user>/', views.UserReviews.as_view(), name="userReviews"),
    path('reviews/', views.AllReviews.as_view(), name="allReviews"),
    path('review/<str:id>/', views.Review.as_view(), name="review")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)