from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from slugify import slugify


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Чорновик'),
        ('published', 'Опублікований')
    )
    title = models.CharField('Заголовок', max_length=256)
    slug = models.SlugField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='content_posts', verbose_name='Автор')
    body = models.TextField('Тіло тексту')
    photo = models.ImageField('Фото', upload_to='posts/%Y/%m/%d/', blank=True)
    created = models.DateTimeField('Створено', auto_now_add=True)
    updated = models.DateTimeField('Оновлено', auto_now=True)
    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)

