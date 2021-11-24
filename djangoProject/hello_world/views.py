from django.shortcuts import render
from django.http import HttpResponse
import json
import os


def index_page(request):
    if os.path.exists("hello_world\\JSONResponse.JSON"):
        os.remove("hello_world\\JSONResponse.JSON")
    f = open("hello_world\\JSONResponse.JSON", "a")
    f.write(json.dumps({"Message": "Hello World!"}))
    f.close()
    return render(request, 'index.html')


def read_JSON(request):
    f = open("hello_world\\JSONResponse.JSON", "r")
    JSON = f.read()
    f.close()
    return HttpResponse(JSON, content_type="text/plain")
