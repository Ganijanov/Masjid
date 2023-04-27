from django.db import models

class Viloyat(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class ShaharTuman(models.Model):
    STATUS = {
        'sh':'Shaxar',
        't':'Shaxar'
    }
    name = models.CharField(max_length=255, null=False, blank=False)
    status = models.CharField(STATUS, null=False, blank=False )
    viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Masjid(models.Model):
    name = models.CharField(max_length=255)
    sh_t = models.ForeignKey(ShaharTuman, on_delete=models.CASCADE)
    about = models.TextField(default='Malumot yoq')
    
    def __str__(self):
        return self.name
    
class Hodim(models.Model):
    STATUS = {
        1:'Imom',
        2:'Imom hatib',
        3:'Qori',
        4:'Muazzin'
    }
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS)
    masjid = models.ForeignKey(Masjid, on_delete=models.CASCADE)

class Image(models.Model):
    image = models.ImageField(upload_to='masjid/')
    masjid = models.ForeignKey(Masjid, on_delete=models.CASCADE)