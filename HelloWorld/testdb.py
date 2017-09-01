# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test

# 数据库操作
def save(request):
	test1 = Test(name='runoob')
	test1.save()
	return HttpResponse("<p>数据添加成功!</p>")

# 更新数据库
def update(request):
	test1 = Test.objects.get(id=1)
	test1.name = '代立旺'
	Test.objects.filter(id=2).update(name='高丽君')
	test1.save()
	return HttpResponse('<p>修改成功</p>')

# 删除数据
def delete(request):
	Test.objects.all().delete()
	return HttpResponse('<p>删除成功</p>')

# 查看request
def look(request):
	return HttpResponse('123')