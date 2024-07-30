from django.db import models

# Create your models here.


class Categories(models.Model):

    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=150, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        # имя для бд
        db_table = "Category"
        # имя для админки
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class BiddingCateories(models.Model):
    format_bidding = models.CharField(
        max_length=80, blank=False, null=False, verbose_name="Формат аукциона"
    )
    slug = models.SlugField(
        max_length=150, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "BiddingCategory"
        verbose_name = "Формат Аукциона"

    def __str__(self):
        return self.format_bidding


class Lots(models.Model):

    name = models.CharField(
        max_length=150, blank=False, null=False, verbose_name="Наименование"
    )
    slug = models.SlugField(
        max_length=150, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(
        max_length=600, blank=True, null=True, verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="lots_images", blank=True, null=True, verbose_name="Изображение"
    )
    price = models.DecimalField(
        default=0.00, max_digits=20, decimal_places=2, verbose_name="Цена"
    )
    application_date = models.DateField(
        blank=False, null=False, verbose_name="Заявки принимаются до:"
    )
    bidding_date = models.DateField(
        blank=False, null=False, verbose_name="Дата проведения торгов"
    )
    url_etp = models.URLField(blank=False, null=False, verbose_name="Ссылка на торги")
    format_bidding = models.ForeignKey(
        to=BiddingCateories,
        on_delete=models.PROTECT,
        verbose_name="Формат проведения торгов",
    )
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Категория лота"
    )
    place = models.CharField(max_length=150,blank=False,null=False,default='Уточняется',verbose_name='Местоположение')

    class Meta:

        db_table = "goods_lots"

        verbose_name = "Лот"
        verbose_name_plural = "Лоты"

    def __str__(self):
        return self.name
