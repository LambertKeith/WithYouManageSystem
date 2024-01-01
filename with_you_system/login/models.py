from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Teacher(models.Model):
    # 教师编号，假设是唯一的
    teacher_id = models.CharField(verbose_name='教师编号', max_length=10, unique=True)
    
    # 姓名
    name = models.CharField(verbose_name='教师姓名', max_length=100)

    # 负责教室
    classroom = models.CharField(verbose_name='负责教室', max_length=50)

    # 登录密码
    # 注意：实际中应使用Django内置的用户认证系统来处理密码
    password = models.CharField(verbose_name='登录密码', max_length=50, validators=[MinLengthValidator(8)])

    # 是否为管理员，布尔值，默认为False
    is_admin = models.BooleanField(verbose_name='是否为管理员', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'