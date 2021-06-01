import json
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


import tuple_label.label.models
from . import serializers


class ProjectStatus(View):
    def get(self, request):
        project_id = request.GET["project_id"]
        total_count = tuple_label.label.models.Document.objects.filter(project_id=project_id).count()
        is_checked_count = tuple_label.label.models.Document.objects.filter(
            project_id=project_id, is_checked=1
        ).count()
        return JsonResponse(
            {
                "total_count": total_count,
                "is_checked_count": is_checked_count,
                "precent": is_checked_count / total_count if total_count > 0 else 0,
            }
        )


class Login(View):
    def post(self,request):
        body_dict=json.loads(request.body)
        username=body_dict.get("username")
        password=body_dict.get("password")
        # password = request.POST['password']
        print(password)
        user = authenticate(username=username, password=password)

        print(user)
        if user != None:
            old_token = Token.objects.filter(user=user)
            old_token.delete()
            # 创建新的token并传递给前端
            token = Token.objects.create(user=user)
            print(token)
            return JsonResponse({
                "status": 200,
                "message": "成功登录",
                "token": token.key
            })
        else:
            return JsonResponse({
                "status": 201,
                "message": "登录失败,请校验用户名或者密码",
            })


class Register(View):
    def post(self,request):
        body_dict = json.loads(request.body)
        password = body_dict.get("password")
        username = body_dict.get("username")
        print(username, "+", password)
        #添加至数据库
        project_id = tuple_label.label.models.Project.objects.get(id=1)
        tuple_label.label.models.User.objects.create(
            password=password,
            username=username,
            project_id=project_id
        )

        # 校验注册，名字不可重复
        user = User.objects.filter(username=username).first()
        # 创建新的token并传递给前端
        user=User.objects.create_user(
                username=username,
                password=password
              )
        token = Token.objects.create(user=user)
        print(token)
        return JsonResponse({
                "status": 200,
                "message": "成功登录",
                "token": token.key
            })
        #   info = '该用户名已被注册'
        #   return render(request,'Myapp/ERROR.html',{'info':info})
        # else:
        #   # 注册成功，创建用户
        #   User.objects.create_user(
        #     username=username,
        #     password=password
        #   )
        #   # 重定向到登录页面
        #   return redirect('../login/')
      # 注册失败，重新注册
      # return render(request,'Myapp/register.html')

class ProjectImport(View):
    def post(self, request):
        try:
            import_list = json.load(request.FILES.get("file").file)
            project_id = request.POST["project_id"]
            for item in import_list:
                tuple_label.label.models.Document.objects.create(project_id=project_id, text=item["text"])
            return JsonResponse({"total_count": len(import_list)})
        except Exception as e:
            return JsonResponse({"err": "json格式有问题"}, status=400)


class ProjectExport(View):
    def get(self, request):
        project_id = request.GET["project_id"]
        documents_by_project_id = tuple_label.label.models.Document.objects.filter(project_id=project_id)
        serializer = serializers.DocumentSerializer(documents_by_project_id, many=True)
        return JsonResponse(serializer.data, safe=False)


class DocumentList(generics.ListCreateAPIView):
    queryset = tuple_label.label.models.Document.objects.all()
    serializer_class = serializers.DocumentSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["project_id"]


class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = tuple_label.label.models.Document.objects.all()
    serializer_class = serializers.DocumentSerializer


class LabelList(generics.ListCreateAPIView):

    queryset = tuple_label.label.models.Label.objects.all()
    serializer_class = serializers.LabelSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["project_id"]


class LabelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = tuple_label.label.models.Label.objects.all()
    serializer_class = serializers.LabelSerializer


class ProjectList(generics.ListCreateAPIView):
    queryset = tuple_label.label.models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = tuple_label.label.models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class UserList(generics.ListCreateAPIView):
    queryset = tuple_label.label.models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = tuple_label.label.models.User.objects.all()
    serializer_class = serializers.UserSerializer


