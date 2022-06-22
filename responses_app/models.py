from django.db import models

# Create your models here.
class Areas(models.Model):
#  """Тема, которую изучает пользователь"""
    area = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
#  """Возвращает строковое представление модели."""
        return self.area

class Places(models.Model):
#  """Информация, изученная пользователем по теме"""
    area = models.ForeignKey(Areas, on_delete=models.CASCADE)
    text = models.TextField()
    
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'places'

    def __str__(self):
#  """Возвращает строковое представление модели."""
        return f"{self.text[:50]}..."


class Comments(models.Model):
#  """Информация, изученная пользователем по теме"""
    place = models.ForeignKey(Places, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='files/',null=True)


    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
#  """Возвращает строковое представление модели."""
        return f"{self.text[:50]}..."
