from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Company
from .serializers import CompanySerializer


class CompanyView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = PageNumberPagination


@api_view(http_method_names=["POST"])
def send_company_email(request: Request) -> Response:
    """
    send email with request palyload
    sender: me@ngelrojas.com
    receiver: info@ngelrojas.com
    """
    send_mail(
        subject=request.data.get("subject"),
        message=request.data.get("message"),
        from_email="info@yopmail.com",
        recipient_list=["info@rednodes.com"],
    )
    return Response(
        {"status": "success", "info": "email sent successfully"}, status=200
    )
