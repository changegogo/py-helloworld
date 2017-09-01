from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
	context = {}
	context['hello'] = '模板数据'
	context['condition'] = False
	context['strlist'] = 'abcdefg'
	context['a'] = 123
	context['b'] = 1234
	return render(request, 'hello.html', context)