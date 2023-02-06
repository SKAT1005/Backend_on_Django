from django.urls import path

from .views import register_view, LoginView, Logout_View, UserEditFormView, HistoryList, HistoryDetail, CartView, \
    OrderView, PaymentForm, PaymentSomeoneForm, UserView, PasswordRecoveryStepOne, PasswordRecoveryStepTwo, \
    ChangingThePassword, AboutView, RepeatOrderView

urlpatterns = [
    path('', AboutView.as_view(), name='about'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', Logout_View.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('password_recovery', PasswordRecoveryStepOne.as_view(), name='password_recovery_step_one'),
    path('recovery_password/<str:pk>', PasswordRecoveryStepTwo.as_view(), name='password_recovery_step_two'),
    path('profile/', UserView.as_view(), name='user_detail'),
    path('profile/change_password', ChangingThePassword.as_view(), name='change_password'),
    path('profile/edit', UserEditFormView.as_view(), name='user_edit'),
    path('profile/history', HistoryList.as_view(), name='history_list'),
    path('profile/history/<int:pk>', HistoryDetail.as_view(), name='history_detail'),
    path('profile/cart', CartView.as_view(), name='cart'),
    path('profile/order', OrderView.as_view(), name='order'),
    path('profile/order/<int:pk>', RepeatOrderView.as_view(), name='order'),
    path('profile/payment/<int:pk>', PaymentForm.as_view(), name='payment_form'),
    path('profile/payment_someone/<int:pk>', PaymentSomeoneForm.as_view(), name='payment_someone_form'),

]
