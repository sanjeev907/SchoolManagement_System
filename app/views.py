from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password, check_password
import jwt
# Create your views here.

def api_response(code,data,message,errors):
   res = {}
   res['code'] = code
   res['data'] = data
   res['message'] = message
   res['errors']= errors
   return res

def check_auth(request):
   try:
      encoded_jwt = request.headers['Authorization']
      a = jwt.decode(encoded_jwt,"secret", algorithms=['HS256'])
      print(a['school_id'])
      return True, a['school_id']
   except Exception as e:
      print(e)
      return False, 0



class SchoolRigrationView(generics.GenericAPIView):
#  permission_classes =[IsAuthenticated]
 def get(self,request):
     sch=school.objects.all()
     serializers=schoolSerializer(sch, many= True)
     return Response(serializers.data)
 
 def post(self,request):
    serializers=schoolSerializer(data=request.data)
    if serializers.is_valid():
        school.objects.create(email=serializers.data['email'],name=serializers.data['name'],city=serializers.data['city'],pincode=serializers.data['pincode'],password=make_password(serializers.data['password']))
        return Response (serializers.data)
    else:
       return Response(serializers.errors)

class schoolLogin(generics.GenericAPIView):
   def post(self,request,*args, **kwargs):
      try:
         serializers = schoolLoginSerializer(data=request.data)
         if serializers.is_valid():
            instance = school.objects.filter(email=serializers.data['email'])
            print(instance[0].password)
            if instance:
               if check_password(serializers.data['password'], instance[0].password):
                  encoded_jwt = jwt.encode({"school_id":instance[0].id}, "secret", algorithm='HS256')
                  print(encoded_jwt)
                  return JsonResponse({'token':encoded_jwt})
      except Exception as e:
         print(e)
    

class studentsRigrationView(generics.GenericAPIView):
    # permission_classes =[IsAuthenticated]
    # print(permission_classes) 
    def get(self,request):
       stu=students.objects.all()
       
       serializer_class=studentsSerializer(stu, many =True)
       return Response(serializer_class.data)
      
      
    def post(self, request, *args, **kwargs):
        try:
            auth_status,school_id = check_auth(request)
            print(school_id)
            print(type(school_id))
            serializers=studentsSerializer(data=request.data)
            if auth_status:
                if serializers.is_valid():
                   students.objects.create(school_name_id=int(school_id),name=serializers.data['name'],grade=serializers.data['grade'],username=serializers.data['username'],password=serializers.data['password']) 
                   return JsonResponse(api_response(0,[],"student registered", []))
                else:
                    return JsonResponse(api_response(0,[],"student registered", []))
        except Exception as e:
           print(e)

class StudentRegisterAPI(generics.GenericAPIView):
   def post(self,request, *args, **kwargs):
      try:
         auth_status,school_id = check_auth(request)
         school_name = int(school_id)
         if auth_status:
            validation = studentsSerializer(data=request.data)
            if validation.is_valid():
               students.objects.create(school_name_id=school_id,name=validation.data['name'],grade=validation.data['grade'],username=validation.data['username'],password=validation.data['password'])
               return JsonResponse(api_response(0,[],"student register",[]))
            else:
               err = validation.errors
               return JsonResponse(1,[],"error",[])
         else:
            return JsonResponse(api_response(1,[],"Unauthorized",[]))
      except Exception as e:
         print(e)
         return JsonResponse(api_response(0,[],"Error",str(e)))
    

                  

      # except Exception as e:
      #    print(e)
      
#  Abhi aaraha hum mai bhi bahar jarkr 
        
        








































# student registration / apply conditoin if school h to student registration karo nahi to response no school found.
# login school / username ya fir email usse pucho ki email and password jo login k time pr daalye h kya vo db mai h agr ha to respnce login successfully.

# login student 

