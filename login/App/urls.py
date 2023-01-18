from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views
from .views import RegisterView, CustomerRegisterView, LogOutAPIView, ChangePasswordView, vendortypeView, \
    vendorinfoView, vendoraboutView, CarView, addpic, venueservices, cateringservices, venuecateringservices, dropimage, djservices, dholservices, portpolioservices,allweddingservices,weddingservices,engegementservices, preweddingservices,allweddingmakeupservices,weddingmakeupservices,engegementmakeupservices, preweddingmakeupservices, foodplateservices, foodwithoutservices, foodwithservices

# from .views  import RegisterAPIView, CustomerRegisterAPIView, vendoraboutView, dropimage

urlpatterns = [
    path('', views.messages_page),
    path('api/vendorregister/', RegisterView.as_view()),
    path('api/vendorlogin/', TokenObtainPairView.as_view(), name='login_view'),

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),
    path('api/logout/', LogOutAPIView.as_view(), name='logout_view'),

    path('api/customerregister/', CustomerRegisterView.as_view()),
    path('api/customerlogin/', TokenObtainPairView.as_view(), name='login_view'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('vendortype/', vendortypeView.as_view()),
    path('vendorinfo/', vendorinfoView.as_view()),
    path('about/', vendoraboutView.as_view()),

    path('car/', CarView.as_view()),
    path('addpics/', addpic.as_view()),
    path('venueservices/', venueservices.as_view()),
    path('cateringservices/', cateringservices.as_view()),
    path('venuecateringservices/', venuecateringservices.as_view()),
    path('dropimage/', dropimage.as_view()),
    path('dj/', djservices.as_view()),
    path('dhol/', dholservices.as_view()),
    path('portpolio/', portpolioservices.as_view()),
    path('engement/', engegementservices.as_view()),
    path('prewedding/', preweddingservices.as_view()),
    path('weddind/', weddingservices.as_view()),
    path('allwedding/', allweddingservices.as_view()),
    path('engementmakeup/', engegementmakeupservices.as_view()),
    path('preweddingmakeup/', preweddingmakeupservices.as_view()),
    path('weddingmakeup/', weddingmakeupservices.as_view()),
    path('allweddingmakeup/', allweddingmakeupservices.as_view()),
    path('foodplate/', foodplateservices.as_view()),
    path('foodwithoutmaterial/', foodwithoutservices.as_view()),
    path('foodwithmaterial/', foodwithservices.as_view())







]