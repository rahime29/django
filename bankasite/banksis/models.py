from django.db import models

# Create your models here.

class Musteri(models.Model):
    mus_tc = models.AutoField(primary_key=True)
    mus_ad = models.CharField(max_length = 20, null = False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.mus_tc


class Hesap(models.Model):
    mus_tc = models.AutoField(primary_key=True)
    hesap_no = models.IntegerField(null = False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.hesap_no

class Transfer(models.Model):
    mus_tc = models.AutoField(primary_key=True)
    hesap_no = models.IntegerField(null = False)
    tutar = models.IntegerField(null = False)
    def publish(self):
        self.save()

    def __str__(self):
        return self.hesap_no 


class Odeme(models.Model):
    mus_tc = models.AutoField(primary_key=True)
    hesap_no = models.IntegerField(null = False)
    odeme_turu = models.CharField(max_length = 20, null = False)
    def publish(self):
        self.save()

    def __str__(self):
        return self.hesap_no