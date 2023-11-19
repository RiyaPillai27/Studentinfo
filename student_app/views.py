from django.shortcuts import render ,HttpResponse,redirect
from .models import Std
# Create your views here.

def info(request):
    
    #context['greet']="hello we are creating db"
    
    if request.method=='POST':
        f=request.POST['fname']
        m=request.POST['mname']
        l=request.POST['lname']
        father=request.POST['fathername']
        mother=request.POST['mothername']
        d=request.POST['dob']
        mail=request.POST['mailid']
        age=request.POST['age']
        mob=request.POST['mobile']
        amob=request.POST['amobile']
        add=request.POST['address']
        s=request.POST['state']
        c=request.POST['city']
        r=Std.objects.create(firstname=f,middlename=m,lastname=l,father=father,mother=mother,d=d,email=mail,age=age,mobile=mob,amobile=amob,add=add,state=s,city=c)
        r.save()
        return redirect('/dashboard')
        #return HttpResponse("data inserted succesfully")
    else:
        #return render(request,'info.html',context)
        return render(request,'info.html') 

def dashboard(request):
    r= Std.objects.all()
    print(r)
    #return HttpResponse("data fetched") 
    context={}
    context['data']=r
    return render(request,'dashboard.html',context)

def delete(request,rid):
    r=Std.objects.filter(id=rid)
    r.delete()
    return redirect('/dashboard')   

def edit(request,rid):
    if request.method=='POST':
        f=request.POST['fname']
        m=request.POST['mname']
        l=request.POST['lname']
        father=request.POST['fathername']
        mother=request.POST['mothername']
        d=request.POST['dob']
        mail=request.POST['mailid']
        age=request.POST['age']
        mob=request.POST['mobile']
        amob=request.POST['amobile']
        add=request.POST['address']
        s=request.POST['state']
        c=request.POST['city']
        r=Std.objects.filter(id=rid)
        r.update(firstname=f,middlename=m,lastname=l,father=father,mother=mother,d=d,email=mail,age=age,mobile=mob,amobile=amob,add=add,state=s,city=c)
        return redirect('/dashboard')
        
    else:
        r=Std.objects.get(id=rid)
        context={}
        context['data']=r
        return render (request,'edit.html',context)





