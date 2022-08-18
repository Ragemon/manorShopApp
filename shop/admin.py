from django.contrib import admin
from .models import Product, Category
from django.utils.safestring import mark_safe
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name','slug']
	prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name','slug','price','stock',
		'available','created','updated']
	list_filter = ['available','created','updated']
	list_editable = ['price','stock','available']
	prepopulated_fields = {'slug':('name',)}
	#Showing image in admin panel
	readonly_fields = ["image_preview"]
	
	def image_preview(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width=obj.image.width,
			height=obj.image.height,
			)
	)
admin.site.register(Product,ProductAdmin)
