from django.db import models
# Create your models here.
class restaurant(models.Model):
	cTitle = models.CharField(max_length=20, null=False,help_text="店名")
	cAddr = models.CharField(max_length=255, default='',help_text="地址")
	cCate = models.CharField(max_length=255, default='',help_text="類別(飯、麵)")	
	cLatitude = models.CharField(max_length=255, default='' ,blank=True,help_text="緯度")
	cLongitude=models.CharField(max_length=255, default='',blank=True,help_text="經度")
	cName = models.CharField(max_length=20, null=False,help_text="推薦人")
	def __str__(self):
		return self.cTitle
