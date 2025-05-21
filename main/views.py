from django.views.generic import TemplateView



class IndexView(TemplateView):
    template_name = "main/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pagename"] = "BankrotСпец - Главная"
        context["content"] = "Имущество с Торгов"
        return context

class AboutView(TemplateView):
    template_name = "main/about.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pagename"] = "BankrotСпец - О нас"
        context["content"] = "О нас"
        context["text_about_us"] = "Тестовый текст , информация о ресурсе"
        return context