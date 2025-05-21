from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView,TemplateView
from django.shortcuts import redirect, render
from django.db.models import Prefetch
from carts.models import Cart

from orders.models import Order, OrderItem
from users.form import UserLoginForm, UserRegistrationForm, ProfileForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    
    def get_success_url(self):
        redirect_page = self.request.POST.get('next', None)
        if redirect_page and redirect_page !=  reverse('users:logout'):
            return redirect_page
        return reverse_lazy("main:index")
    
    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.get_user()
        
        if user:
            auth.login(self.request, user)
            forgot_carts = Cart.objects.filter(user=user)
            if forgot_carts.exists():
                forgot_carts.delete()
            Cart.objects.filter(session_key=session_key).update(user=user)
            
            messages.success(self.request, f"Вы успешно авторизовались.")
            return  HttpResponseRedirect(self.get_success_url())
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["pagename"] = "BakrotWeb - Авторизация"
        return context
    

class UserRegistrationView(CreateView):
    template_name = "users/registration.html"
    form_class = UserRegistrationForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pagename"] = "BakrotWeb - Регистрация"
        return context
    
    def get_success_url(self):
        return reverse_lazy("users:profile")
    
    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.instance
        
        if user:
            form.save()
            auth.login(self.request, user)
            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
            messages.success(self.request, f" {user.username}, вы успешно зарегестрировались и авторизовались.")
            return HttpResponseRedirect(self.get_success_url())
        
    
class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = "users/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("users:profile")
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, " Профиль успешно обновлен.")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pagename"] = "BakrotWeb - Профиль"
        context["orders"] = Order.objects.filter(user=self.request.user).prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("product"),
                )
            ).order_by("-id")
        return context
    
class UserCartView(TemplateView):
    template_name = "users/users-cart.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pagename"] = "BakrotWeb - Корзина"
        return context  
    
@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, вы успешно вышли из аккаунта.")
    auth.logout(request)
    return redirect(reverse('main:index'))


