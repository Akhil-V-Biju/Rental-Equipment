from django.shortcuts import render,redirect
from .models import*
from django.contrib import messages

import os
from django.contrib.auth import authenticate,logout,login,login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required




# Create your views here.

def index(request):
    items = Equipment.objects.all()
    testimonials = Testi.objects.all()
    context={
        'items': items,
        'testimonials':testimonials
    }
    return render(request,'index.html',context)

def testi(request):
    if request.method == 'POST':
        text=request.POST.get('text2')
        user=request.user
        add_profile_instance = Add_profile.objects.get(user=user)

        # Create Testi object with the correct Add_profile instance
        Testi.objects.create(text=text, user=add_profile_instance)
        
        return redirect('index')  # Assuming 'index' is the name of your index view or URL
    else:
        return render(request,'index.html')   


              # register

def register(request):
    if request.method=='POST':
        username1=request.POST.get('username')
        password1=request.POST.get('password')
        email1=request.POST.get('email')
        # fname1=request.POST.get('fname')
        user=User.objects.create_user(
            username=username1,
            password=password1,
            # first_name=fname1,
            email=email1,
        )
        user.save()
        messages.success(request,"SUCESSFULLY REGISTERED")
    return render(request,'register.html') 
 

                           # log in

def login(request):
    if request.method=='POST':
        username1=request.POST.get('username')
        password1=request.POST.get('password')
        user=authenticate(request,username=username1,password=password1)

        if user is not None:
            auth_login(request,user)
            return redirect('index')
    return render(request,'login.html')  


                  # add profile 

# def add_profile(request):
#     return render(request,'add_profile.html')


                                               # add profile

def add_pro(request): 
    if request.method=='POST':
        name1=request.POST.get('name')
        place1=request.POST.get('place')
        phone1=request.POST.get('cnumber')
        address1=request.POST.get('address')
        img1=request.FILES.get('image')
        user2=request.user

        var1=Add_profile.objects.create(
            name=name1,
            place=place1,
            phone=phone1,
            address=address1,
            image=img1,
            user=user2

        )
        var1.save()
        messages.success(request,"SUCESSFULLY added")
        return redirect('add_pro')
    return render(request,'add_profile.html') 



def profile(request):
    profile = Add_profile.objects.get(user=request.user)
    context = {
        'var1': profile
    } 
    return render(request,'profile.html',context)



def update_profile(request,pk):
    update=Add_profile.objects.get(pk=pk)
    if request.method=='POST':
        if 'image' in request.FILES:
            os.remove(update.image.path)
            update.image=request.FILES['image']
        update.name=request.POST.get('name')
        update.phone=request.POST.get('cnumber')
        update.place=request.POST.get('place')
        update.address=request.POST.get('address')
        update.save()  
        messages.success(request,"Successfully UPDATED")
        return redirect('profile')  
    context={
        'update':update
    }
    
    return render(request,'update_profile.html',context)


       # DELETE EQUIPMENT 

def del_st(request,pk):
    del_std=Equipment.objects.get(pk=pk)
    del_std.delete()
    messages.success(request,"Successfully DELETED")
        
    return redirect('view_equipment')






            # view cart
def view_cart(request,pk):
    cart = Equipment.objects.get(pk=pk)
    context = {
        'item': cart
    } 
    return render(request,'view_cart.html',context)



        # buy cart
@login_required(login_url='login')
def buy_cart(request,pk):
    equipment=Equipment.objects.get(pk=pk)
    if request.method=='POST':
        date = request.POST.get('date')
        hours = request.POST.get('hour')
        proof = request.FILES.get('image')
        days = request.POST.get('day')
        book = Buy_cart(
            user=request.user, 
            equipment=equipment,
            ndate=date,
            nhours=hours,
            ndays=days,
            prof=proof
        )
        book.save()
        messages.success(request,"Successfully Booked")
        return redirect('buy_cart',pk=pk)
    context = {
        'equipment': equipment
    } 
    return render(request,'buy_cart.html',context)


                            # history
@login_required(login_url='login')
def history(request):
    details = Buy_cart.objects.filter(user=request.user)
    context = {
        'order': details
    } 
    return render(request,'history.html',context)




# user logout 

def user_logout(request):
    logout(request)
    return redirect('index')



# ******************************************************************************************************************************************************************************ADMIN***************************************************************************************


                                      # admin login
def adminlogin(request):
    if request.method=='POST':
        username1=request.POST.get('username')
        password1=request.POST.get('password')
        user=authenticate(request,username=username1,password=password1)

        if user is not None and user.is_staff:
            auth_login(request,user)
            return redirect('admin_panel')
    return render(request,'admin/adminlogin.html')  

                                        # admin panel

def admin_panel(request):
    details = Buy_cart.objects.all()
    context = {
        'order': details
    } 
    return render(request,'admin/admin_panel.html',context)





def approve_requst(request,pk):
    update=Buy_cart.objects.get(pk=pk)
    if request.method=='POST':
    
           update.bookstatus= True
           update.save()
    return redirect('admin_panel')

              # admin profile 

def admin_profile(request):
    return render(request,'admin/admin_profile.html')


# admin equipment update 

def update_equipment(request,pk):
    update=Equipment.objects.get(pk=pk)
    if request.method=='POST':
        if 'image' in request.FILES:
            os.remove(update.image.path)
            update.image=request.FILES['image']
        update.name=request.POST.get('name')
        update.quantity=request.POST.get('quantity')
        update.description=request.POST.get('description')
        update.priceday=request.POST.get('priceday')
        update.pricehour=request.POST.get('price_hour')
        update.save()  
        messages.success(request,"Successfully UPDATED")
        return redirect('view_equipment')  
    context={
        'update':update
    }
    
    return render(request,'admin/admin_updateequi.html',context)





# admin log out


def admin_logout(request):
    logout(request)
    return redirect('index')
 


                            #  admin form 

def add_equipment(request):
    if request.method=='POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        quantity = request.POST.get('quantity')
        price1= request.POST.get('price_day')
        price2 = request.POST.get('price_hour')

        
        new_equipment = Equipment(name=name, description=description, image=image, quantity=quantity,priceday=price1,pricehour=price2)
        new_equipment.save()

        
        messages.success(request, "Equipment added successfully.")

        
        return redirect('admin_panel') 

    return render(request,'admin/add_equipments.html')    



                # view equipment 

def view_equipment(request):
    items = Equipment.objects.all()
    context = {
        'var1': items
    }  
    return render(request, 'admin/admin_viewpro.html', context)     















