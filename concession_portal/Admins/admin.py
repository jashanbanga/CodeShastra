from django.contrib import admin
from .models import RailwayAdmin, CollegeAdmin
# Register your models here.
class RailwayAdminAdmin(admin.ModelAdmin):
	list_display = ('id', 'railwayEmpId', 'railwayEmployee')
	list_display_links = ('id', 'railwayEmpId', 'railwayEmployee')
	search_fields = ('railwayEmpId', 'railwayEmployee')
	def get_ordering(self, request):
		return ['railwayEmpId']

class CollegeAdminAdmin(admin.ModelAdmin):
	list_display = ('id', 'collegeEmpId', 'collegeEmployee')
	list_display_links = ('id', 'collegeEmpId', 'collegeEmployee')
	search_fields = ('collegeEmpId', 'collegeEmployee')
	def get_ordering(self, request):
		return ['collegeEmpId']	

admin.site.register(RailwayAdmin, RailwayAdminAdmin)
admin.site.register(CollegeAdmin, CollegeAdminAdmin)