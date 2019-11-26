from django.contrib import admin
from myapp.models import restaurant
# Register your models here.
class restaurantAdmin(admin.ModelAdmin):
    # 第三種方式，加入 ModelAdmin 類別，定義顯示欄位、欄位過濾資料、搜尋和排序
	list_display=('id','cTitle','cAddr','cCate','cLatitude','cLongitude','cName')
	search_fields=('cTitle',)
	ordering=('id',)
	
admin.site.register(restaurant,restaurantAdmin)#把model跟admin綁起來