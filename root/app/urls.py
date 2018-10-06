from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls import url

router=routers.DefaultRouter()

router.register('all_endpoint',views.InsuranceView,'all_endpoint')
router.register('Automobiles_endpoint',views.InsuranceAutomobilesView,'Automobiles_endpoint')
router.register('TradingCards_endpoint',views.InsuranceTradingCardsView,'TradingCards_endpoint')

urlpatterns = [
        path('',include(router.urls)),
        url(r'^form/$',views.InsuranceFormView,name='createForm'),
        url(r'^main/$',views.InsuranceView.homeview,name='main')
]