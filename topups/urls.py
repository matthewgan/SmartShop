# Stdlib imports
# Core Django imports
from django.conf.urls import url
# Third-party app imports
# Imports from your apps
from .views import TopupCreateView, TopUpSuccessView, PointToBalanceView

urlpatterns = [
    url(r'^$', TopupCreateView.as_view()),
    # url(r'^$', TopUpView.as_view()),
    url(r'^success/$', TopUpSuccessView.as_view()),
    url(r'^p2b/$', PointToBalanceView.as_view()),
]
