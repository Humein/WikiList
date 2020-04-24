import datetime
from django.utils import timezone
from django.db import models
# Create your models here.

class WiKi(models.Model):
    title_text = models.CharField(max_length=200)
    url_text = models.CharField(max_length=200)
    author_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self): # 管理后台显示
        return self.title_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)