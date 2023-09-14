from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

# Create your views here.
def home(request):
    return HttpResponse("OK")

def api(request):
    if request.method == "POST":


@api_view(http_method_names=["GET", "POST"])
def news(request: Request) -> Response:
    if request.method == "GET":
        with open("messages.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        data = {"messages": lines}
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        print(request.GET)
        print(request.POST)
        print(request.FILES)
        print(request.data)

        message: str = request.data.get('message', '')
        with open("messages.txt", "a", encoding="utf-8") as file:
            file.write(f"{message}\n")

        return Response(data={"message": "OK"}, status=status.HTTP_201_CREATED)