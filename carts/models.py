from django.db import models
from goods.models import Lots
from users.models import User



class CartQueryset(models.QuerySet):
    
    def total_price(self):
        return sum(cart.lots_price() for cart in self)
    
    def total_count(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE,blank=True, null=True, verbose_name="Пользователь"
    )
    lot = models.ForeignKey(to=Lots, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Лот")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Количество")
    session_key = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        db_table = 'cart'
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"
        
    objects = CartQueryset.as_manager()


    def lots_price(self):
        return round(self.lot.price * self.quantity, 2)

    # def __str__(self):
    #     return f" Корзина {self.user.username} | Лот {self.lot.name} | Количество {self.quantity}"
    
    
