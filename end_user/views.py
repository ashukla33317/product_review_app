
from django.shortcuts import redirect, render
from django.views import View
import gridfs
from .import forms
from django.contrib.auth.models import auth,User
import dbinfo
import base64
from bson.objectid import ObjectId






class HomePage(View):
    # def get(self,request):
    #     collection=dbinfo.database['product_info']
    #     content={
    #         'page_title':'base_page',
    #         'product_info':collection.find()
    #     }
    #     return render(request,'index.html',content)
    def get(self,request):
        collection = dbinfo.database['product_info']
        
        data = list()
        fs = gridfs.GridFS(dbinfo.database)
        for item in collection.find():
            image_path = fs.get(ObjectId(item['image_id']))
           
            product_info = {
                'uid':item['uid'],
                'price':item['price'],
                'product_name':item['product_name'],
                'image_path': base64.b64encode(image_path.read()).decode('utf-8')
            }
            data.append(product_info)
            
        content = {
            'page_title':'Home Page',
            'product_list': data
        }
        
        return render(request,'index.html',content)




class LoginUser(View):
    def get(self,request):
        content={
            'page_title':'login_page',
            'login_form':forms.LoginForm()
        }
        return render(request,'login.html',content)

    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
        return redirect('/')


class SignupUser(View):
    def get(self,request):
        content={
            'page_title':'signup_form',
            'signup':forms.SignUpForm()
        }
        return render(request,'signup.html',content)


    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        new_user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
        new_user.save()
        return redirect('/')
    
class LogoutUser(View):
    def get(self,request):
        auth.logout(request)
        return redirect('/')    