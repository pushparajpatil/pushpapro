from django.shortcuts import render
from .forms import StudentForm
# Create your views here.
def studentdip(request):
    fm=StudentForm()
    return render(request,'testapp/form.html',{'form':fm})