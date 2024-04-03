from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from techapp.models import laptop,Cart,Billingdetails,Order
from django.contrib import messages
from django.db.models import Q
import razorpay
import random
from django.core.mail import send_mail
# Create your views here.
def home(request):
    context={}
    data=laptop.objects.all()
    context['laptops']=data
    return render(request,'index.html',context)

def contactus(request):
    return render(request,'contactus.html')

def privacyp(request):
    return render(request,'privacypolicy.html')

def Userlogin(request):
    if request.method=="GET":
        return render(request,'login.html')
    else:
        context = {}
        n = request.POST['username']
        p = request.POST['password']
        if n=='' or p=='':
            context['error'] = 'Please enter all the fields'
            return render(request,'login.html',context)
        else:
            user = authenticate(username = n, password= p)
            if user is not None:
                login(request,user)

                context['success'] = 'Logged in successfully'
                return redirect('/')
            else:
                context['error'] = 'Please provide correct details'
                return render(request,'index.html',context)

def userlogout(request):
    logout(request)
    return render(request,'index.html')        


def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    else:
        context={}
        e=request.POST['email']
        n=request.POST['username']
        p=request.POST['password']
        cp=request.POST['confirmpassword']
        if e=='' or n=='' or p=='' or cp=='':
            context['error'] ="plase enter all fields"
            return render(request,'register.html',context)
        elif p!= cp:
            context['error'] ="password does not match "
            return render(request,'register.html',context)
        else:
            context['success'] = " registered sucessfully please login"
            user = User.objects.create(email=e,username=n)
            user.set_password(p)
            user.save()
            return render(request,'login.html',context)
        
def userlogout(request):
    logout(request)
    return render(request,'index.html')

# def laptopdetails(request,pid):
#     context={}
#     data=laptop.objects.filter(id=pid)
#     context['laptop']=data[0]
#     context1={}
#     data1=laptop.objects.all()
#     context['product'] = data1
#     return render(request,'product.html',context,)

def laptopdetails(request, pid):
    context = {}
    data = laptop.objects.filter(id=pid)
    if data.exists():
        context['laptop'] = data.first()
    
    context['products'] = laptop.objects.all()
    return render(request, 'product.html', context)

def addtocart(request,laptopid):
    userid=request.user.id
    if userid is None:
        context= {}
        context['error']= "Please login "
        return render (request,'login.html',context)
    else:
        userid =request.user.id
        users=User.objects.filter(id=userid)
        laptops=laptop.objects.filter(id=laptopid)
        cart =Cart.objects.create(pid=laptops[0], uid=users[0])
        cart.save()
        messages.success(request,"item has been added sucessfully ")
        return redirect('/mycart')

def showmycart(request):
        context ={}
        userid = request.user.id
        data = Cart.objects.filter(uid=userid)
        context['mycart'] = data
        count =len(data)
        total=0
        for cart in data:
            total += cart.pid.price * cart.quantity
        context['count'] = count
        context['total'] = total
        return render(request,'cart.html',context)

def delete(request,cartid):
    data=Cart.objects.filter(id=cartid)
    data.delete()
    return redirect('/mycart')

def checkout(request):
    context ={}
    userid = request.user.id
    data = Cart.objects.filter(uid=userid)
    context['mycart'] = data
    count =len(data)
    total=0
    for cart in data:
        total += cart.pid.price * cart.quantity
    context['count'] = count
    context['total'] = total
    return render(request,'checkout.html',context)

def billing(request):
        if request.method=='GET':
            return render(request,'register.html')
        else:
            context={}
            f=request.POST['first-name']
            s=request.POST['f_email']
            t=request.POST['address']
            u=request.POST['city']
            data=Billingdetails.objects.create(F_name=f,Email=s,Address=t,city=u)
            data.save()
            context['useraddress'] = data
            return render(request,'pay.html',context)
        
def makepayment(request):
    context={}
    userid = request.user.id
    data = Cart.objects.filter(uid=userid)
    context['mycart'] = data
    count =len(data)
    total=0
    for cart in data:
        total += cart.pid.price * cart.quantity
    client = razorpay.Client(auth=("rzp_test_HkubfwbV338ozD","2Hg3ShRVrg2wfYvO2UGPlNhq"))
    data = {"amount":total*10, "currency":"INR","receipt": ""}
    payment = client.order.create(data=data)
    print(payment)
    context['data'] = payment
    return render (request,'pay.html',context)

def order(request):
        userid = request.user.id
        print("within in place order",userid)
        user = User.objects.filter(id=userid)
        mycart = Cart.objects.filter(uid=userid)
        ordid=random.randrange(1000,9999)
        for cart in  mycart:
            pet = laptop.objects.filter(id = cart.pid.id)
            ord = Order.objects.create(uid =user[0],pid=pet[0],quantity=cart.quantity ,orderid=ordid)
            ord.save()
        mycart.delete()

        msg_body ='order id is '+str(ordid)
        custEmail = request.user.email
        print("userdetails",userid,custEmail)
        send_mail(
            "order placed succesfully",
            msg_body,
            "mpsgroceryapp@gmail.com",
            [custEmail],
            fail_silently=False,
        )

        messages.success(request,"order  placed suceesfully")
        return redirect('/')

def shopnow(request):
    context={}
    data=laptop.objects.all()
    context['laptops']=data
    return render(request,'store.html',context)

def thankyou(request):
    return render(request,'thankyou.html')