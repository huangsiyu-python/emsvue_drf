from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.generics import GenericAPIView
from api.models import User, Employee
from api.serializers import UserModelSerializer,EmployeeModelSerializer
from utils.response import APIResponse
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin, \
    RetrieveModelMixin


class UserAPIView(APIView):
    def post(self,request,*args,**kwargs):
        request_data=request.data
        # print(request_data)
        password=request.data.get("password")
        re_pwd=request.data.get("re_pwd")
        print(password)
        print(re_pwd)
        # serializer=UserModelSerializer(data=request_data)
        # serializer.is_valid(raise_exception=True)
        if password ==re_pwd:
            serializer = UserModelSerializer(data=request_data)
            serializer.is_valid(raise_exception=True)
            user_obj=serializer.save()
            return APIResponse(200,True,results=UserModelSerializer(user_obj).data)
        return APIResponse(400,False)
    def get(self,request,*args,**kwargs):
        username=request.query_params.get("username")
        password=request.query_params.get("password")
        # print(query_params)
        user=User.objects.filter(username=username,password=password).first()
        if user:
            data=UserModelSerializer(user).data
            return APIResponse(200,True,results=data)
        return APIResponse(400,False)

class EmployeeView(DestroyModelMixin,ListModelMixin,GenericAPIView,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    lookup_field = 'id'
    def get(self,request,*args,**kwargs):
        emp_id=kwargs.get("id")
        if emp_id:
            emp = self.retrieve(request, *args, **kwargs)
            return APIResponse(status.HTTP_200_OK, True, results=emp.data)
        else:
            emp_list = self.list(request, *args, **kwargs)
            print(emp_list)
            return APIResponse(status.HTTP_200_OK, True, results=emp_list.data)
        # print(emp_id)
        # user_list=self.list(request,*args,**kwargs)
        # print(user_list)
        # return APIResponse(200,True,results=user_list.data)
    def post(self,request,*args,**kwargs):
        # data=request.data
        # print(data)
        user_obj=self.create(request,*args,**kwargs)
        return APIResponse(200,True,results=user_obj.data)
    # def patch(self,request,*args,**kwargs):
    #     # print('123')
    #     response = self.partial_update(request, *args, **kwargs)
    #     return APIResponse(results=response.data)
    def put(self, request, *args, **kwargs):
        response = self.update(request, *args, **kwargs)
        print(response)
        return APIResponse(results=response.data)
    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return APIResponse(http_status=status.HTTP_204_NO_CONTENT)
class RegisterView(ViewSet):
    def check_user(self,request,*args,**kwargs):
        return APIResponse("ok")