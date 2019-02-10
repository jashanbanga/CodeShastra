from django.shortcuts import render
from .models import CollegeApplication 
# Create your views here.

def college(request):
	Collegdeets=CollegeApplication.objects.all()
	deets={'details':Collegdeets}
	print(Collegdeets)
	return render(request,'tables/tableApproved.html',deets)
