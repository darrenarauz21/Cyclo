from django.http import HttpResponse
from .models import QRCode

def generate_qr(request, content):
    qr_code = QRCode(content=content)
    qr_code.save()
    return HttpResponse("QR code generated and saved successfully!")
