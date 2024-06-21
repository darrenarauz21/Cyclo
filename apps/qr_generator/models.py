from django.db import models
import qrcode
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class QRCode(models.Model):
    content = models.CharField(max_length=255)
    image = models.ImageField(upload_to='qr_codes', blank=True)

    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.content)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        buffer = BytesIO()
        img.save(buffer, format='PNG')

        filename = f'qr_{self.pk}.png'
        file_buffer = BytesIO()
        img.save(file_buffer, format='PNG')
        self.image.save(filename, InMemoryUploadedFile(
            file_buffer, None, filename, 'image/png', file_buffer.getbuffer().nbytes, None))

    def save(self, *args, **kwargs):
        if not self.image:
            self.generate_qr_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Código QR: {self.pk}'
