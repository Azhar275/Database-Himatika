from django.db import models


class Status_Anggota(models.Model):
    nama_status = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.nama_status}"

class Angkatan(models.Model):
    tahun = models.CharField(max_length=4)
    nama_angkatan = models.CharField(max_length=200, default="Tidak ada")
    def __str__(self):
        return f"{self.nama_angkatan}, {self.tahun}"

class Prodi(models.Model):
    nama_prodi = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.nama_prodi}"

class Anggota(models.Model):
    nama = models.CharField(max_length=200)
    nim = models.CharField(max_length=20, unique=True)
    no_hp = models.CharField(max_length=20, null=True)
    no_wa = models.CharField(max_length=20, null=True)
    prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE)
    email = models.EmailField()
    GOL_DARAH = (
        ('A', 'A'),
        ('B', 'B'),
        ('O', 'O'),
        ('AB', 'AB'),
    )
    tempat_lahir = models.CharField(max_length=100, null=True)
    tanggal_lahir = models.DateField()
    asal_daerah = models.CharField(max_length=100, null=True)
    alamat_dms = models.CharField(max_length=500, null=True)
    alamat_mks = models.CharField(max_length=500, null=True)
    goldar = models.CharField(max_length=2, choices=GOL_DARAH, null=True)
    angkatan = models.ForeignKey(Angkatan, on_delete=models.CASCADE)
    keterangan = models.ForeignKey(Status_Anggota, on_delete=models.CASCADE)
    minat = models.CharField(max_length=200, default="Tidak ada")
    bakat = models.CharField(max_length=200, default="Tidak ada")
    
    def __str__(self):
        return f"{self.nama}, {self.angkatan.tahun}"
