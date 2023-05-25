from django.contrib import admin
from .models import Angkatan, Status_Anggota, Prodi, Anggota

# Register your models here.
admin.site.register(Angkatan)
admin.site.register(Status_Anggota)
admin.site.register(Prodi)
admin.site.register(Anggota)