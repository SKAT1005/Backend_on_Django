import random

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from app_shop.models import Category
from .forms import RegisterForm, UserEditForm, OrderForm, EmailForm, PasswordForm
from .models import Profile, History, Delivery

ERROR_LIST = [
    'Неверные реквизиты карты',
    'Ваша карта заблокирована',
    'Недостаточно средств',
    'Оплата картой вашего банка недоступна на территории РФ',
]


class AboutView(View):
    def get(self, request):
        category = Category.objects.all
        return render(request, 'registration/about.html', context={'category': category})


class Login_View(LoginView):
    """Представления логина"""
    template_name = 'registration/login.html'


class Logout_View(LogoutView):
    """Представление выхода"""
    next_page = '/'


class PasswordRecoveryStepOne(View):
    error = ''

    def get(self, request):
        form = EmailForm
        return render(request, 'registration/e-mail.html', context={'form': form,
                                                                    'error': self.error})

    def post(self, request):
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.get(username=email):
                return HttpResponseRedirect(f'http://127.0.0.1:8000/recovery_password/{email}')
            self.error = 'Данного пользователя не существует'
        return render(request, 'registration/e-mail.html', context={'form': form,
                                                                    'error': self.error})


class PasswordRecoveryStepTwo(View):
    def get(self, request, pk):
        form = PasswordForm
        return render(request, 'registration/password.html', context={'form': form})

    def post(self, request, pk):
        form = EmailForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            user = User.object.get(user=pk)
            user.password = password
            user.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/')
        return render(request, 'registration/password.html', context={'form': form})


class ChangingThePassword(View):
    def get(self, request):
        form = PasswordForm
        return render(request, 'registration/password.html', context={'form': form})

    def post(self, request):
        form = EmailForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            user = User.object.get(user=request.user.id)
            user.password = password
            user.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/profile')
        return render(request, 'registration/password.html', context={'form': form})


def register_view(request):
    form = RegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        else:
            form = RegisterForm()
    return render(request, 'registration/registr.html', {'form': form})


class UserView(View):
    def get(self, request):
        category = Category.objects.all()
        profile = Profile.objects.get(id=request.user.id)
        try:
            history = profile.history.latest('id')
        except Exception:
            history = False
        return render(request, 'registration/account.html', context={'profile': profile,
                                                                     'history': history,
                                                                     'category': category})


class UserEditFormView(View):
    def get(self, request):
        profile = Profile.objects.get(id=request.user.id)
        category = Category.objects.all()
        form = UserEditForm(instance=profile, initial={'username': request.user.username,
                                                       'first_name': request.user.first_name,
                                                       'phone_number': profile.phone_number})
        return render(request, 'registration/profile.html',
                      context={'form': form, 'category': category, 'profile': profile})

    def post(self, request):
        category = Category.objects.all()
        profile = Profile.objects.get(id=request.user.id)
        form = UserEditForm(request.POST, request.FILES)
        if form.is_valid():
            profile.phone_number = form.cleaned_data.get('phone_number')
            if not form.cleaned_data.get('file') == None:
                profile.avatar = form.cleaned_data.get('file')
            else:
                pass
            profile.save()
            request.user.username = form.cleaned_data.get('username')
            request.user.first_name = form.cleaned_data.get('first_name')
            request.user.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/profile/')
        return render(request, 'registration/profile.html',
                      context={'form': form, 'category': category, 'profile': profile})


class HistoryList(View):
    def get(self, request):
        try:
            history_list = History.objects.all()
        except Exception:
            history_list = False
        category = Category.objects.all()
        return render(request, 'registration/historyorder.html',
                      context={'history_list': history_list,
                               'category': category})


class HistoryDetail(View):
    def get(self, request, pk):
        history = History.objects.get(id=pk)
        category = Category.objects.all()
        return render(request, 'registration/oneorder.html',
                      context={'history': history,
                               'category': category})


class CartView(View):
    def get(self, request):
        profile = Profile.objects.get(id=request.user.id)
        cart = profile.cart.all()
        category = Category.objects.all()
        return render(request, 'registration/cart.html',
                      context={'cart': cart,
                               'profile': profile,
                               'category': category})


class OrderView(View):
    def get(self, request):
        profile = Profile.objects.get(id=request.user.id)
        cart = profile.cart.all()
        category = Category.objects.all()
        form = OrderForm(initial={'phone_number': request.user.users.phone_number,
                                  'city': request.user.users.city,
                                  'address': request.user.users.address,
                                  'first_name': request.user.first_name})
        return render(request, 'registration/order.html',
                      context={'form': form,
                               'category': category,
                               'cart': cart})

    def post(self, request):
        form = OrderForm(request.POST)
        category = Category.objects.all()
        profile = Profile.objects.get(id=request.user.id)
        cart = profile.cart.all()
        delivery = Delivery.objects.get(id=1)
        if request.method == 'POST':
            if form.is_valid():
                profile = Profile.objects.get(id=request.user.id)
                profile.phone_number = form.cleaned_data.get('phone_number')
                profile.city = form.cleaned_data.get('city')
                profile.user.users.first_name = form.cleaned_data.get('first_name')
                profile.save()
                history = History.objects.create(
                    user=profile,
                    type_of_delivery=request.POST.get('delivery'),
                    type_of_pay=request.POST.get('pay'),
                    total_price=profile.total_price,
                    status='Не оплачено', )
                profile.history.add(history)
                history.prods.set = cart
                profile.cart.clear()
                profile.save()
                if history.type_of_delivery == 'Обычная доставка':
                    if history.total_price >= delivery.min_cart:
                        pass
                    else:
                        history.total_price += delivery.delivery
                else:
                    if history.total_price >= delivery.min_cart:
                        history.total_price += delivery.express_delivery
                    else:
                        history.total_price += delivery.delivery + delivery.express_delivery
                if history.type_of_pay == 'Онлайн картой':
                    return HttpResponseRedirect('http://127.0.0.1:8000/profile/trans_pay/1')
                else:
                    return HttpResponseRedirect('http://127.0.0.1:8000/profile/trans_pay/2')
        return render(request, 'registration/order.html',
                      context={'form': form,
                               'category': category,
                               'cart': cart})


class RepeatOrderView(View):
    def get(self, request, pk):
        last_history = History.objects.get(id=pk)
        cart = last_history.prods.all()
        category = Category.objects.all()
        form = OrderForm(initial={'phone_number': request.user.users.phone_number,
                                  'city': request.user.users.city,
                                  'address': request.user.users.address,
                                  'first_name': request.user.first_name})
        return render(request, 'registration/order.html',
                      context={'form': form,
                               'category': category,
                               'cart': cart})

    def post(self, request, pk):
        form = OrderForm(request.POST)
        category = Category.objects.all()
        last_history = History.objects.get(id=pk)
        cart = last_history.prods.all()
        delivery = Delivery.objects.get(id=1)
        if request.method == 'POST':
            if form.is_valid():
                profile = Profile.objects.get(id=request.user.id)
                profile.phone_number = form.cleaned_data.get('phone_number')
                profile.city = form.cleaned_data.get('city')
                request.user.first_name = form.cleaned_data.get('first_name')
                request.user.save()
                profile.save()
                history = History.objects.create(
                    user=profile,
                    type_of_delivery=request.POST.get('delivery'),
                    type_of_pay=request.POST.get('pay'),
                    total_price=profile.total_price,
                    status='Не оплачено', )
                profile.history.add(history)
                history.prods.set(cart)
                profile.save()
                if history.type_of_delivery == 'Обычная доставка':
                    if history.total_price >= delivery.min_cart:
                        pass
                    else:
                        history.total_price += delivery.delivery
                else:
                    if history.total_price >= delivery.min_cart:
                        history.total_price += delivery.express_delivery
                    else:
                        history.total_price += delivery.delivery + delivery.express_delivery
                if history.type_of_pay == 'Онлайн картой':
                    return HttpResponseRedirect('http://127.0.0.1:8000/profile/trans_pay/1')
                else:
                    return HttpResponseRedirect('http://127.0.0.1:8000/profile/trans_pay/2')
        return render(request, 'registration/order.html',
                      context={'form': form,
                               'category': category,
                               'cart': cart})


def trans_pay(request, pk):
    if pk == 1:
        return HttpResponseRedirect('http://127.0.0.1:8000/profile/payment')
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/profile/payment_someone')


class PaymentForm(View):
    def get(self, request):
        category = Category.objects.all()
        return render(request, 'registration/payment.html',
                      context={'category': category})

    def post(self, request):
        category = Category.objects.all()
        profile = Profile.objects.get(id=request.user.id)
        history = History.objects.filter(user=profile).latest('pub_date')
        if int(request.POST.get('numero1')) <= 100000000 and int(request.POST.get('numero1')) % 10 != 0 and int(
                request.POST.get('numero1')) % 2 == 0:
            history.status = 'Оплачен'
            history.save()
            return render(request, 'registration/progressPayment.html', context={'category': category})
        else:
            history.status = 'Ошибка'
            history.error = 'Неверные реквизиты карты'
            history.save()
            return render(request, 'registration/progressPayment.html', context={'category': category})


class PaymentSomeoneForm(View):
    def get(self, request):
        category = Category.objects.all()
        return render(request, 'registration/paymentsomeone.html',
                      context={'category': category})

    def post(self, request):
        category = Category.objects.all()
        profile = Profile.objects.get(id=request.user.id)
        history = History.objects.filter(user=profile).latest('pub_date')
        cart_number = int(request.POST.get('numero1').replace(' ', ''))
        if cart_number <= 100000000 and cart_number % 10 != 0 and cart_number % 2 == 0:
            history.status = 'Оплачен'
        else:
            history.status = 'Ошибка'
            history.error = 'Неверные реквизиты карты'

        return render(request, 'registration/progressPayment.html', context={'category': category})
