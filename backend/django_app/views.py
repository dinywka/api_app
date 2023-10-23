from django.http import HttpResponse, HttpResponseNotAllowed
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.templatetags.rest_framework import data
from .models import News, Complaint
from .serializers import NewsSerializer, ComplaintSerializer
from django.shortcuts import render
from django.db import transaction
import datetime


def home(request):
    if request.method == "POST":
        return HttpResponseNotAllowed(['GET'])
    return HttpResponse("OK")

@swagger_auto_schema(method='GET', responses={200: NewsSerializer(many=True)})
@swagger_auto_schema(method='POST', request_body=NewsSerializer, responses={201: NewsSerializer, 400: "Bad Request"})
@api_view(http_method_names=["GET", "POST"])
def api(request):
    '''Create new news'''
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

def index(request):
    return render(request, "index.html", context={})

@swagger_auto_schema(method='GET', responses={200: ComplaintSerializer(many=True)})
@swagger_auto_schema(method='POST', request_body=ComplaintSerializer, responses={201: ComplaintSerializer, 400: "Bad Request"})
@api_view(["GET", "POST", "PUT", "DELETE"])
def add_complaint(request: Request, point_id: str = None) -> Response:
    """
    Add a new complaint
    """
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

def orm_methods(request):
    top_5_news = News.objects.all()[:5]
    print(top_5_news)

    breaking_news = News.objects.filter(name="Breaking News")
    print(breaking_news)

    sport_news = News.objects.filter(name__startswith="Sport")
    print(sport_news)

    all_complaints = Complaint.objects.all()
    print(all_complaints)

    service_complaints = Complaint.objects.filter(name__icontains="Service")
    print(service_complaints)

    news_count = News.objects.count()
    print(news_count)

    new_news = News(name="New Report", title="About Weather", news="It's sunny today.")
    new_news.save()

    new_complaint = Complaint(name="Product Issue", description="The product was damaged on arrival.")
    new_complaint.save()

    first_news = News.objects.first()
    first_news.name = "Updated Report"
    first_news.save()

    last_news = News.objects.last()
    last_news.delete()

    long_titles = News.objects.filter(title__length__gt=50)
    print(long_titles)

    complaints_desc = Complaint.objects.order_by('-name')
    print(complaints_desc)

    weather_news = News.objects.filter(news__icontains="Weather")
    print(weather_news)

    unique_names = News.objects.values_list('name', flat=True).distinct()
    print(unique_names)

def create(request):
    list_objects = []
    for i in range(1, 100):
        news1 = News.objects.create(title=f"Breaking News {i}")
        list_objects.append(news1)
        News.objects.bulk_create(list_objects, batch_size=30)
    return HttpResponse("Новость успешно создана!")

def trasaction_create(request):
    try:
        transaction.set_autocommit(False)
        print("До операции")
        News.objects.create(title="Urgent content")
        print("После операции")
        transaction.commit()
        return HttpResponse("Новость успешно создана!")
    except Exception as error:
        print(f"[ERROR] ({datetime.datetime.now()}): ", error)
        transaction.rollback()
        return HttpResponse(f"Ошибка создания {error}")


