from django.db import models
from django.contrib.auth.models import AbstractUser

class Teacher(AbstractUser):
    # 添加额外的字段
    classroom = models.CharField(verbose_name='负责教室', max_length=50)
    
    class Meta:
        # 多数名词
        verbose_name_plural = '老师'

    def __str__(self):
        if self.classroom != '':
            return f"{self.username}:教室{self.classroom}"
        else :
            return f"{self.username}"

    
