from django.urls import path
from app.views import register,waste_collection_point,waste_collection_record,wallet,signin,saved_address,update_profile,smspin
from app.views import get_user
from .utils.TokenObtainPairView import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('getalluser/',get_user.GetUserALL),
    # path('user/',get_user.GetUser.as_view()),
    # path('userwastecollector/',get_user.GetWasteCollector.as_view()),
    # path('userdistrictwastecollector/',get_user.GetDistrictWasteCollector.as_view()),
    path('registerUser/',register.RegisterAPI.as_view()),
    path('update_profile/',update_profile.UpdateProfileAPI.as_view()),
    path('waste_collection_point/', waste_collection_point.WasteCollectionPointAPI.as_view()),
    path('waste_collection_point/<slug:collection_point_id>/', waste_collection_point.WasteCollectionPointSlugAPI.as_view(), name='login'),
    path('waste_collection_record/',waste_collection_record.WasteCollectionRecordAPI.as_view()),
    path('wallet/',wallet.CreditAPI.as_view()),
    path('wallet/',wallet.DebitAPI.as_view()),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', signin.LoginAPI.as_view(), name='login'),
    path('address/', saved_address.SavedAddressAPI.as_view(), name='login'),
    path('address/<slug:saved_address_id>/', saved_address.SavedAddressSlugAPI.as_view(), name='login'),
    path('pin_verify/', smspin.SmsPinAPI.as_view()),


]

