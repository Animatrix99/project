from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    '''Post'''
    title = models.CharField('Sarlavha', max_length=200)
    tixt = models.TextField('Matni')
    author = models.CharField('Avtor', max_length=50)
    date = models.DateField('Vaqti')
    img = models.ImageField('Rasm', upload_to='image/', blank=True)

    def __str__(self):
        return f'{self.title} | {self.author}'
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Postlar'
    


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField('Ism', max_length=50)
    email = models.EmailField()
    text_comment = models.TextField('Izoy')

    def __str__(self):
        return f'{self.post} | {self.name}'

    class Meta:
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'