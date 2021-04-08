from django.db import models


class NewsCategory(models.Model):
    name = models.CharField('name', max_length=255, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'news category'
        verbose_name_plural = 'news category'


class News(models.Model):
    title = models.CharField('title', max_length=255, blank=False)
    content = models.TextField('content', max_length=1000, blank=False)
    category = models.ForeignKey(NewsCategory, related_name='category_news', on_delete=models.CASCADE)
    image = models.ImageField('image', upload_to='news/', default='no_image.jpg', help_text='Image resolution 750x375')
    created_at = models.DateTimeField('date', auto_now_add=True)
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'news'
        verbose_name_plural = 'news'


class About(models.Model):
    title = models.CharField('page name', max_length=255, blank=False)
    slug = models.SlugField('slug', max_length=255, blank=False, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'about'


class AboutItem(models.Model):
    page = models.ForeignKey(About, related_name='about_about_items', on_delete=models.CASCADE)
    title = models.CharField('title', max_length=255, blank=False)
    content = models.TextField('content', max_length=1000, blank=False)

    def __str__(self):
        return self.page.title


class Contact(models.Model):
    title = models.CharField('page name', max_length=255, blank=False)
    slug = models.SlugField('slug', max_length=255, blank=False, unique=True)
    address = models.CharField('address', max_length=255, blank=False)
    contact_phone = models.CharField('contact phone', max_length=16, blank=False)
    email = models.EmailField("email", max_length=100, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contact'
