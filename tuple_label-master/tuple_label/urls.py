"""tuple_label URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from tuple_label.label import views

# urlpatterns = [
#     path("", views.ProjectList.as_view()),
#     path("", views.ProjectDetail.as_view()),
#     path("", views.LabelList.as_view()),
#     path("", views.LabelDetail.as_view()),
#     path("", views.DocumentList.as_view()),
#     path("", views.DocumentDetail.as_view()),
#     path("", views.ProjectStatus.as_view()),
#     path("", views.ProjectImport.as_view()),
#     path("", views.ProjectExport.as_view()),
# ]

urlpatterns = [
    path("api/project/", views.ProjectList.as_view()),
    path("api/project/<int:pk>/", views.ProjectDetail.as_view()),
    path("api/label/", views.LabelList.as_view()),
    path("api/label/<int:pk>/", views.LabelDetail.as_view()),
    path("api/document/", views.DocumentList.as_view()),
    path("api/document/<int:pk>/", views.DocumentDetail.as_view()),
    path("api/project_status/", views.ProjectStatus.as_view()),
    path("api/project_import/", views.ProjectImport.as_view()),
    path("api/project_export/", views.ProjectExport.as_view()),
    path("api/login/",views.Login.as_view()),
    path("api/register/",views.Register.as_view()),
    path("api/signer/", views.SignerList.as_view()),
    # path("api/user/", views.UserList.as_view()),
    path("api/signer/<int:pk>/", views.SignerDetail.as_view()),
    path("", views.ProjectList.as_view()),
]