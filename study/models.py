from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    create_time = models.DateTimeField(verbose_name="创建时间", default=timezone.now)
    update_time = models.DateTimeField(verbose_name="修改时间", default=timezone.now)
    delete_time = models.DateTimeField(verbose_name="删除时间", default=timezone.now)
    enable = models.BooleanField(verbose_name="有效", default=1)

    class Meta:
        abstract = True


class User(BaseModel):
    user_id = models.CharField(verbose_name="用户uid", max_length=50)
    user_name = models.CharField(verbose_name="用户名称", max_length=50)
    user_pwd = models.CharField(verbose_name="用户密码", max_length=18)
    user_phone = models.CharField(verbose_name="用户手机", max_length=11)
    user_email = models.CharField(verbose_name="用户邮箱", max_length=20)
    real_name = models.CharField(verbose_name="真实姓名", max_length=20)
    user_sex = models.IntegerField(verbose_name="性别", choices=((0, "男"), (1, "女")), default=1)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"
        db_table = "user"

