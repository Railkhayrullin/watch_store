from django.db import models
from django.urls import reverse_lazy


class Category(models.Model):
    title = models.CharField('category', max_length=255, blank=False)
    slug = models.SlugField('slug', max_length=255, blank=False, unique=True)
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_watch(self):
        return self.category_products.all()


class CaseMaterial(models.Model):
    title = models.CharField('case material', max_length=255, blank=False)
    slug = models.SlugField('slug', max_length=255, blank=False, unique=True)
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'case material'
        verbose_name_plural = 'case materials'


class Country(models.Model):
    title = models.CharField('country', max_length=255, blank=False)
    slug = models.SlugField('slug', max_length=255, blank=False, unique=True)
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'


class Brand(models.Model):
    title = models.CharField('brand', max_length=255, blank=False)
    slug = models.SlugField('slug', max_length=255, blank=False, unique=True)
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class Product(models.Model):
    title = models.CharField('watch', max_length=255, blank=False)
    slug = models.SlugField('slug', max_length=255, blank=False, unique=True)
    category = models.ForeignKey(Category, related_name='category_products', on_delete=models.CASCADE)
    case_material = models.ForeignKey(CaseMaterial, related_name='case_material_products', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name='country_products', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='brand_products', on_delete=models.CASCADE)
    image = models.ImageField("image", upload_to='images/', default='no_image.jpg',
                              help_text='Image resolution 380x361')
    with_discount = models.BooleanField('with discount', default=False)
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = 'watch'
        verbose_name_plural = 'watch'

    def get_absolute_url(self):
        return reverse_lazy('watch', kwargs={'slug': self.slug})

    def get_regular_price(self):
        if self.product_prices.filter(price_type__title='regular').exists():
            return self.product_prices.get(price_type__title='regular').price

    def get_discounted_price(self):
        if self.product_prices.filter(price_type__title='discounted').exists():
            return self.product_prices.get(price_type__title='discounted').price


class PriceType(models.Model):
    title = models.CharField('brand', max_length=255, blank=False)
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.title


class Price(models.Model):
    product = models.ForeignKey(Product, related_name='product_prices', on_delete=models.CASCADE)
    price_type = models.ForeignKey(PriceType, related_name='price_type_prices', on_delete=models.CASCADE)
    price = models.PositiveIntegerField('price', blank=False)
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.product.title

    class Meta:
        unique_together = 'product', 'price_type'
