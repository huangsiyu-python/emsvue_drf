from rest_framework import exceptions
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from api.models import User, Employee


class UserModelSerializer(ModelSerializer):
    class Meta:
        model=User
        # fields ="__all__"
        fields=("username","real_name","password","gender")
        extra_kwargs={
            "username":{
                "required":True,
                "min_length":2,
                "error_messages":{
                    "required":"用户名必填",
                    "min_length":"用户名太短"
                }
            }
        }

    def validate(self, attrs):
        username=attrs.get("username")
        # pwd=attrs.get("password")
        # re_pwd=attrs.pop("re_pwd")
        # print(pwd)
        # print(re_pwd)
        user=User.objects.filter(username=username).first()
        if user:
            raise exceptions.ValidationError("用户名已存在")
        return attrs

class EmployeeModelSerializer(ModelSerializer):
    class Meta:
        model=Employee
        # fields="__all__"
        fields=("id","emp_name","salary","img","age","age_name")
        extra_kwargs = {
            "empname": {
                "required": True,
                "min_length": 2,
                "error_messages": {
                    "required": "用户名必填",
                    "min_length": "用户名太短"
                }
            }}
