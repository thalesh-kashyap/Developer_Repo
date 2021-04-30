from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from addEmp.models import  Developer
from addEmp import forms

def home(request):
     return render(request,'AddEmp/home.html')

def EmpData(request):
	developer = Developer.objects.all()
	return render(request, 'AddEmp/Data.html', {'developer':developer})

def DeveloperForm(request):
	form=forms.DeveloperForm()
	if request.method=='POST' :
		form=forms.DeveloperForm(request.POST)
		if form.is_valid() :
			print("In is valid part")
			form.save()
			messages.success(request,"Developer Added Succesfully")
			print(form.cleaned_data)
			print("Record inserted Succesfully.....!")
			return render(request,'AddEmp/empAdded.html')
	return render(request,'AddEmp/addEmp.html',{'form':form})

def edit_view(request,id):
	instance  =  Developer.objects.get(pk=id)
	if request.method=="POST":
		fm=forms.DeveloperForm(request.POST,instance=instance)


		if fm.is_valid:
			fm.save()
			return redirect('/home/data')
			#return redirect('addEmp/edit.html')
	fm=forms.DeveloperForm(instance=instance)
	return render(request,"AddEmp/edit.html",{'fm':fm})
