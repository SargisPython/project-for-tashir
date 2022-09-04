from django.db import models
from django.contrib import admin
from django.utils import timezone




class Tashir_pizza(models.Model):
    image = models.ImageField(upload_to="image", null=True, blank=True)
    title = models.CharField(max_length=100, null=True)
    opening=models.IntegerField(null=True)
    closing=models.IntegerField(null=True)


    def __str__(self):
        return self.title



class Pizza(models.Model):
    tesaky=models.CharField(max_length=100, null=True,blank=True)
    arjeqy=models.IntegerField(null=True,blank=True)
    baxadrutyuny=models.TextField(null=True,blank=True)
    category = models.ForeignKey('Xohanocy', on_delete=models.CASCADE, blank=True,null=True )



    def __str__(self):
        return self.tesaky

    class Meta:
        verbose_name = 'pizza'
        verbose_name_plural = 'Պիցցաներ'
        ordering = ['id']




class Salat(models.Model):
    tesaky=models.CharField(max_length=100, null=True,blank=True)
    arjeqy=models.IntegerField(null=True,blank=True)
    baxadrutyuny=models.TextField(null=True,blank=True)
    category = models.ForeignKey('Xohanocy', on_delete=models.CASCADE, blank=True,null=True )



    def __str__(self):
        return self.tesaky

    class Meta:
        verbose_name = 'salat'
        verbose_name_plural = 'Սալատներ'



class Sous(models.Model):
    tesaky=models.CharField(max_length=100, null=True,blank=True)
    arjeqy=models.IntegerField(null=True,blank=True)
    baxadrutyuny=models.TextField(null=True,blank=True)
    category = models.ForeignKey('Xohanocy', on_delete=models.CASCADE, blank=True,null=True )



    def __str__(self):
        return self.tesaky

    class Meta:
        verbose_name = 'sous'
        verbose_name_plural = 'Սոուսներ'


class Xohanocy(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'xohanocy'
        verbose_name_plural = 'Խոհանոցներ'
        ordering = ['id']




class Patmutyun(models.Model):
    patmutyuny=models.TextField(blank=True)
    shefxoharar=models.CharField(max_length=50)
    imagexoharar = models.ImageField(upload_to="image", null=True, blank=True)
    imagerestoran = models.ImageField(upload_to="image", null=True, blank=True)
    erkushabti=models.ForeignKey('Jamer', on_delete=models.CASCADE, blank=True,null=True,related_name='erkushabti_1')
    erekshabti=models.ForeignKey('Jamer', on_delete=models.CASCADE, blank=True,null=True,related_name='erekshabti_2' )
    choreqshabti=models.ForeignKey('Jamer', on_delete=models.CASCADE, blank=True,null=True,related_name='choreqshabti_3' )
    hingshabti=models.ForeignKey('Jamer', on_delete=models.CASCADE, blank=True,null=True,related_name='hingshabti_4' )
    urbat=models.ForeignKey('Jamer', on_delete=models.CASCADE, blank=True,null=True,related_name='urbat_5' )
    shabat=models.ForeignKey('Jamer', on_delete=models.CASCADE, blank=True,null=True,related_name='shabat_6' )
    kiraki=models.ForeignKey('Jamer', on_delete=models.CASCADE, blank=True,null=True,related_name='kiraki_7')


    class Meta:
        verbose_name = 'patmutyun'
        verbose_name_plural = 'Պատմությունը'

class Jamer(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'jamer'
        verbose_name_plural = 'ժամերը'
        ordering = ['id']

class Social(models.Model):
    title=models.CharField(max_length=50)
    url=models.CharField(max_length=255)
    icon=models.ImageField(upload_to="icons")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'social'
        verbose_name_plural = 'Լինկեր'



class Contact(models.Model):
    name = models.CharField(max_length=80)
    people =models.TextField(max_length=150)
    date = models.DateTimeField(default=timezone.now)
    number = models.TextField(max_length=150)
    #created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'Զակասներ'


