from django.shortcuts import redirect,render
from studentdata.models import student
from studentdata.forms import studentForm

# Create your views here.
def std(request):
	if request.method=="POST":
		form=studentForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect("/show")
			except:
				pass
	else:			
		form = studentForm()
		return render(request,'index.html',{'form':form})

def show(request):
    studentdatas=student.objects.all()
    return render(request,'show.html',{'studentdatas:studentdatas'})

def edit(request,id):
    studentdata=student.objects.all()
    return render(request,'edit.html',{'studentdata:studentdata'})

def update(request,id):
    studentdata=student.objects.get(id=id)
    form=studentForm(request.POST,instance=studentdata)
    if form.is_valid():
    	form.save()
    	return redirect("/show")
    return render(request,'edit.html',{'studentdata':studentdata})
def destroy(request,id):
    studentdata = student.objectsget(id=id)
    studentdata.delete()
    return redirect("/show")
