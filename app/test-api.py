from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(["GET"])
def test_api(request):
    response = {}
    try:
        response['msg'] = 'success'
        response['data'] = 'django,vue 搭建前后端分离平台成功'
    except:
        response['msg'] = 'fail'
        response['data'] = 'django,vue 搭建前后端分离平台失败'
    return JsonResponse(response)