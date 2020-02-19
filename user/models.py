# -*-coding:utf-8-*-

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=150, blank=True, null=False, unique=True, verbose_name='用户名')
    account = models.CharField(max_length=20, default='', verbose_name="账号")
    password = models.CharField(max_length=150, null=False, verbose_name="密码")
    email = models.CharField(max_length=20, verbose_name="邮箱", null=True)
    u_image = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', verbose_name="头像图片路径" )
    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class Classify(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称')
    intro = models.CharField(max_length=100, verbose_name='分类简介')

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class College(models.Model):
    name = models.CharField(max_length=20, verbose_name='大学名称')
    intro = models.CharField(max_length=50, verbose_name='大学简介')
    logo = models.CharField(max_length=50, verbose_name='大学 logo')
    co_image = models.CharField(max_length=50, verbose_name='大学图片')
    schoolbadge = models.CharField(max_length=50, verbose_name='大学背景图片')

    class Meta:
        verbose_name = "大学"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=20, verbose_name='资料名称')
    author = models.CharField(max_length=20, verbose_name='作者')
    intro = models.CharField(max_length=50, verbose_name='资料简介')
    downloadnum = models.IntegerField(verbose_name='下载数量')
    m_image = models.CharField(max_length=20, verbose_name='资料图片')

    classifyid = models.ForeignKey(to=Classify, on_delete=models.CASCADE,verbose_name='所属分类')

    class Meta:
        verbose_name = "资料"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=20, verbose_name='课程名称')
    author = models.CharField(max_length=20, verbose_name='作者')
    intro = models.CharField(max_length=50, verbose_name='课程简介')
    v_image = models.CharField(max_length=30, verbose_name='课程图片地址')
    viewnum = models.IntegerField(verbose_name='观看数量',null=True )
    likenum = models.IntegerField(verbose_name='点赞数量',null=True)
    collectnum = models.IntegerField(verbose_name='收藏数量',null=True)
    coursefile = models.CharField(max_length=30, verbose_name='课件')
    sumtime = models.IntegerField(verbose_name='课程总时长')

    collegeid = models.ForeignKey(to=College, on_delete=models.CASCADE, verbose_name='所属大学')
    classifyid = models.ForeignKey(to=Classify, on_delete=models.CASCADE,verbose_name='所属分类')

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Video(models.Model):
    videoid = models.CharField(max_length=30, verbose_name='视频地址')
    sectionname = models.CharField(max_length=30, verbose_name='视频章节名称')
    time = models.CharField(max_length=20, verbose_name='视频时长')

    courseid = models.ForeignKey(to=Course, on_delete=models.CASCADE,verbose_name='所设课程')

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.sectionname


class History(models.Model):
    historytime = models.CharField(max_length=50, verbose_name="历史时间", null=True)
    collect = models.BooleanField(verbose_name="收藏", default=False)

    userid = models.ForeignKey(to=User, on_delete=models.CASCADE,verbose_name='所属用户')
    videoid = models.ForeignKey(to=Video, on_delete=models.CASCADE,verbose_name='所属视频')

    class Meta:
        verbose_name = "观看历史"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.collect
