from django.db import models


class Project(models.Model):
    """项目表"""

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    admin_id = models.IntegerField()
    class Meta:
        managed = True
        db_table = "label_project"
        app_label = 'label'

class Label(models.Model):
    """项目Label"""

    project_id = models.ForeignKey(
        Project,
        db_column="project_id",
        related_name="project_label",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=128)
    shortcut = models.CharField(max_length=8)
    background_color = models.CharField(max_length=8)
    text_color = models.CharField(max_length=8)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "label_label"
        app_label = 'label'

class Document(models.Model):
    """标注文本表"""

    text = models.TextField()
    project_id = models.IntegerField()
    annotations = models.CharField(max_length=2048, default="[[]]")
    predications = models.TextField(default="[[]]")
    is_checked = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "label_document"
        app_label = 'label'


class Admin(models.Model):
    """管理员信息表"""
    name=models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    class Meta:
        managed = True
        db_table = "label_admin"
        app_label = 'label'


class Signer(models.Model):
    """用户信息表"""
    admin_id = models.IntegerField()
    name = models.CharField(max_length=128)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        managed = True
        db_table = "label_signer"
        app_label = 'label'
