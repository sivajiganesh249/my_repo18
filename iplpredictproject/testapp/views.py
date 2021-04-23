from django.shortcuts import render,redirect
from testapp.models import Matche
from testapp.forms import MatcheForm


# Create your views here.
def retrieve_view(request):
    matches=Matche.objects.all()
    return render(request,'testapp/index.html',{'matches':matches})

def create_view(request):
    form=MatcheForm()
    if request.method=='POST':
        form=MatcheForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testapp/create.html',{'form':form})

def delete_view(request,id):
    matche=Matche.objects.get(id=id)
    matche.delete()
    return redirect('/')

def update_view(request,id):
    matche=Matche.objects.get(id=id)
    if request.method=="POST":
        form=MatcheForm(request.POST,instance=matche)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'testapp/update.html',{'matche':matche})
