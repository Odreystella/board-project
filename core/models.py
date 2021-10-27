from django.db import models

class AbstractTimeStamped(models.Model):

    """Time Stamped Model"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # 데이터베이스에 등록 안됨
