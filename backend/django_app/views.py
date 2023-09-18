from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.templatetags.rest_framework import data
from rest_framework.views import APIView
from .models import News, Complaint
from .serializers import NewsSerializer, ComplaintSerializer


# Create your views here.
def home(request):
    return HttpResponse("OK")
@api_view(http_method_names=["GET", "POST"])
def api(request):
    if request.method == "POST":
        print(data)
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Unsupported method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# @api_view(http_method_names=["GET", "PUT", "DELETE", "POST"])
# def add_complaint(request: Request, point_id: str = "-1") -> Response:
#     if point_id == "-1":
#         if request.method == "GET":
#             compl_json = ComplaintSerializer(data=request.data)
#             return Response(data=compl_json, status=status.HTTP_200_OK)
#         elif request.method == "POST":
#             if compl_json.is_valid():
#                 compl_json.save()
#                 return Response(data={"message": "success"}, status=status.HTTP_201_CREATED)
#     else:
#         if request.method == "GET":
#             # Получение детальных данных по point_id
#             return Response(data={"data": []}, status=status.HTTP_200_OK)
#         elif request.method == "PUT":
#             # Обновление записи по point_id
#             return Response(data={"message": "success"}, status=status.HTTP_200_OK)
#         elif request.method == "DELETE":
#             # Удаление записи по point_id
#             return Response(data={"message": "success"}, status=status.HTTP_200_OK)

@api_view(["GET", "POST", "PUT", "DELETE"])
def add_complaint(request: Request, point_id: str = None) -> Response:
    if point_id:
        try:
            complaint = Complaint.objects.get(pk=point_id)
        except Complaint.DoesNotExist:
            return Response({"error": "Complaint not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        if point_id:
            serializer = ComplaintSerializer(complaint)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            complaints = Complaint.objects.all()
            serializer = ComplaintSerializer(complaints, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        if point_id:
            serializer = ComplaintSerializer(complaint, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Point ID is required for update."}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        if point_id:
            complaint.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "Point ID is required for deletion."}, status=status.HTTP_400_BAD_REQUEST)