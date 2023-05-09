from django.db import models

class Viloyat(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class ShaharTuman(models.Model):
    STATUS = {
        ('Shaxar','Shaxar'),
        ('Tuman','Tuman')
    }
    name = models.CharField(max_length=255, null=False, blank=False)
    status = models.CharField(choices=STATUS, null=False, blank=False, max_length=255 )
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
        ('Imom','Imom'),
        ('Imom hatib','Imom hatib'),
        ('Qori','Qori'),
        ('Muazzin','Muazzin')
    }
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    about = models.TextField(default="Malumot yoq")
    status = models.CharField(choices=STATUS, max_length=255)
    masjid = models.ForeignKey(Masjid, on_delete=models.CASCADE, related_name='masjidi')

    def __str__(self):
        return self.f_name

class Image(models.Model):
    image = models.ImageField(upload_to='masjid/')
    masjid = models.ForeignKey(Masjid, on_delete=models.CASCADE, related_name='images')
    
    def __str__(self):
        return self.masjid.name

class HodimImage(models.Model):
    image = models.ImageField(upload_to='hodim/')
    hodim = models.ForeignKey(Hodim, on_delete=models.CASCADE, related_name='photos')

    def __str__(self) -> str:
        return self.hodim.f_name