from django.db import models
from django.db.models.fields.files import FieldFile

class PdfFile(models.Model):
    file=models.FileField(upload_to="pdf/",blank=True)
    # {
    # "Contract Awarder": "MINDEF",
    # "Contracted Services": [
    #       "Supply of Fully Equipped Ambulance",
    #       "Installation of Medical Equipment and Accessories"
    #  ],
    #  "Nature of Contract": "Recurring",
    #  "Collection Via": "ePerolehan (eP)",
    #  "Contract Description": "SUPPLY OF FULLY EQUIPPED AMBULAN - PEROLEHAN PERALATAN PERUBATAN HOSPITAL SERTA AMBULAN UNTUK UNIT DIBAWAH NAUGAN PERKHIDMATAN KESIHATAN ANGKATAN TENTERA (PKAT) MENGGUNAKAN PERBELANJAAN DARULAT 173.2 HARTA MODAL",
    #  "Tenure of Contract": "6 months",
    #  "Delivery Period": "25 May 2022 to 30 Nov 2022",
    #  "Contract Value": "RM 25,000,000.00"
    # }
# Create your models here.
