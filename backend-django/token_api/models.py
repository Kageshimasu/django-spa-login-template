import hashlib

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TokenRDB(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=40)
    access_datetime = models.DateTimeField()

    def __str__(self):
        dt = timezone.localtime(self.access_datetime).strftime("%Y/%m/%d %H:%M:%S")
        return self.user.email + '(' + dt + ') - ' + self.token

    @staticmethod
    def create(user: User):
        if TokenRDB.objects.filter(user=user).exists():
            TokenRDB.objects.get(user=user).delete()

        dt = timezone.now()
        str = user.email + user.password + dt.strftime('%Y%m%d%H%M%S%f')
        hash = hashlib.sha1(str.encode('utf-8')).hexdigest()

        token = TokenRDB.objects.create(
            user=user,
            token=hash,
            access_datetime=dt)
        return token
