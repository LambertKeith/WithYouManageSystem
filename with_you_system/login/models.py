from django.db import models
from django.contrib.auth.models import AbstractUser

class Teacher(AbstractUser):
    # 添加额外的字段
    teacher_id = models.CharField(verbose_name='教师编号', max_length=10, unique=True)
    classroom = models.CharField(verbose_name='负责教室', max_length=50)
    is_admin = models.BooleanField(verbose_name='是否为管理员', default=False)

    def __str__(self):
        return self.username

    
