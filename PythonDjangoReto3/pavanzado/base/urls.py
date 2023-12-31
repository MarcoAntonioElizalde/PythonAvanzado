from django.urls import path
from . import views

urlpatterns = [
    path('', views.getMenu),
    path('users/', views.UserList.as_view()),
    path('users/<str:username>', views.UserDetail.as_view()),
    path('accounts/', views.AccountList.as_view()),
    path('accounts/<str:id>', views.AccountDetail.as_view()),
    path('cards/', views.CardList.as_view()),
    path('cards/<str:id>', views.CardDetail.as_view()),
    path('charges/', views.ChargeList.as_view()),
    path('charges/<str:id>', views.ChargeDetail.as_view()),
    path('payments/', views.PaymentList.as_view()),
    path('payments/<str:id>', views.PaymentDetail.as_view()),

]