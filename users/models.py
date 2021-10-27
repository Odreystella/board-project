from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """ User model """

    email = models.EmailField(max_length=25, unique=True, verbose_name="email")
    name = models.CharField(max_length=10, verbose_name="닉네임")
    bio = models.TextField(verbose_name="소개글")

    USERNAME_FIELD = "email"  # 고유 식별자로 email 설정
    REQUIRED_FIELDS = ("username",)  # createsuperuser 커맨드 실행했을 때 입력받을 필드 설정, USERNAME_FIELD or PASSWORD는 포함되면 안됨

    def __str__(self):
        return self.name