import factory
from factory.django import DjangoModelFactory
from .models import Anggota, Prodi, Angkatan, Status_Anggota
import random

# Defining a factory
class AnggotaFactory(DjangoModelFactory):
    class Meta:
        model = Anggota

    nama = factory.Faker("name")
    nim = factory.Faker("ean8")
    no_hp = factory.Faker("phone_number")
    no_wa = factory.Faker("phone_number")
    prodi = Prodi.objects.get(pk=random.randint(1,3))
    email = factory.Faker("email")
    # GOL_DARAH = (
    #     ('A', 'A'),
    #     ('B', 'B'),
    #     ('O', 'O'),
    #     ('AB', 'AB'),
    # )
    tempat_lahir = factory.Faker("city")
    tanggal_lahir = factory.Faker("date")
    asal_daerah = factory.Faker("city")
    alamat_dms = factory.Faker("address")
    alamat_mks = factory.Faker("address")
    goldar = 'A'
    angkatan = Angkatan.objects.get(pk=random.randint(1,3))
    keterangan = Status_Anggota.objects.get(pk=random.randint(1,2))
    minat = "Tidak ada"
    bakat = "Tidak ada"