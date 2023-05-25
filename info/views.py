from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
from .models import Angkatan, Status_Anggota, Prodi, Anggota
from django.db.models import Q

def index(request):
    list_anggota = Anggota.objects.order_by('id')
    list_angkatan = Angkatan.objects.all()
    list_prodi = Prodi.objects.all()
    context = {'list_anggota': list_anggota, 'list_angkatan' : list_angkatan, 'list_prodi' : list_prodi}
    return render(request, 'info/index.html', context)

def detail(request, page):
    total_data = Anggota.objects.count()
    if total_data // 25 < page :
        raise Http404("Halaman tidak ditemukan") 
    list_anggota = Anggota.objects.order_by('nama')[page*25:(page+1)*25]
    return render(request, 'info/index.html', {'list_anggota': list_anggota})

def search(request):
    keyword = request.GET.get('search')
    s_angkatan = request.GET.get('angkatan')
    prodi = request.GET.get('prodi')
    if keyword == "" and s_angkatan == "" and prodi == "" :
        return redirect("/")
    if prodi == "" and s_angkatan != ""and keyword != "" :
        list_anggota = Anggota.objects.filter(Q(nama__icontains=keyword) & Q(angkatan=Angkatan.objects.get(pk=s_angkatan)))
    elif s_angkatan == "" and keyword != "" and prodi != "":
        list_anggota = Anggota.objects.filter(Q(nama__icontains=keyword) & Q(prodi=Prodi.objects.get(pk=prodi)))
    elif keyword == "" and prodi != "" and s_angkatan != "" :
        list_anggota = Anggota.objects.filter(Q(angkatan=Angkatan.objects.get(pk=s_angkatan)) & Q(prodi=Prodi.objects.get(pk=prodi)))
    elif keyword != "" :
        list_anggota = Anggota.objects.filter(Q(nama__icontains=keyword))
    elif prodi != "" :
        list_anggota = Anggota.objects.filter(Q(prodi=Prodi.objects.get(pk=prodi)))
    elif s_angkatan != "" :
        list_anggota = Anggota.objects.filter(Q(angkatan=Angkatan.objects.get(pk=s_angkatan)))
    else :
        list_anggota = Anggota.objects.filter(Q(nama__icontains=keyword) & Q(angkatan=Angkatan.objects.get(pk=s_angkatan)) & Q(prodi=Prodi.objects.get(pk=prodi)))
    list_angkatan = Angkatan.objects.all()
    list_prodi = Prodi.objects.all()
    return render(request, 'info/index.html', {'list_anggota': list_anggota, 'list_angkatan' : list_angkatan, 'list_prodi' : list_prodi})

def add(request):
    list_angkatan = Angkatan.objects.all()
    list_prodi = Prodi.objects.all()
    list_status = Status_Anggota.objects.all()
    list_goldar =["A", "B", "O", "AB"]
    context = {'list_angkatan' : list_angkatan, 'list_prodi' : list_prodi, 'list_status' : list_status, 'list_goldar' : list_goldar}
    return render(request, 'info/add_member.html', context)

def add_r(request):
    count = 0
    list_angkatan = Angkatan.objects.all()
    list_prodi = Prodi.objects.all()
    list_status = Status_Anggota.objects.all()
    list_goldar =["A", "B", "O", "AB"]
    context = {'list_angkatan' : list_angkatan, 
                'list_prodi' : list_prodi, 
                'list_status' : list_status,
                'list_goldar' : list_goldar}
    # error_list = {

    # }
    new_nama = request.POST['nama']
    new_nim = request.POST['nim']
    list_nim = Anggota.objects.values_list('nim', flat=True)
    if new_nim.upper() in list_nim :
        count = 1
        context["nim_error"] = "NIM telah terdaftar, silahkan isi kembali"
    new_hp = request.POST['hp']
    new_wa = request.POST['wa']
    new_prodi = request.POST['prodi']
    if new_prodi == "" :
        count = 1
        context["prodi_error"] = "Pilih satu"
        new_prodi = "-1"
    new_email = request.POST['email']
    new_goldar = request.POST['goldar']
    if new_goldar == "" :
        count = 1
        context["goldar_error"] = "Pilih satu"
        new_goldar = "-1"
    new_t_lahir = request.POST['t_lahir']
    new_tgl_lahir = request.POST['tgl_lahir']
    # x = new_tgl_lahir.split("/")
    # new_tgl_lahir = f"{x[2]}-{x[0]}-{x[1]}"
    new_daerah = request.POST['daerah']
    new_mks_ad = request.POST['mks_ad']
    new_dms_ad = request.POST['dms_ad']
    new_angkatan = request.POST['angkatan']
    if new_angkatan == "" :
        count = 1
        context["angkatan_error"] = "Pilih satu"
        new_angkatan = "-1"
    new_anggota = request.POST['anggota']
    if new_anggota == "" :
        count = 1
        context["anggota_error"] = "Pilih satu"
        new_anggota = "-1"
    new_minat = request.POST['minat']
    new_bakat = request.POST['bakat']
    # s_angkatan = request.GET.get('angkatan')
    # prodi = request.GET.get('prodi')
    # context = {'list_angkatan' : list_angkatan, 'list_prodi' : list_prodi, 'list_status' : list_status}
    # return render(request, 'info/form.html', context)
    if count == 0 :
        # if len(error_list) != 0 :
        #     raise Exception
        a = Anggota(
            nama = new_nama,
            nim = new_nim.upper(),
            no_hp = new_hp,
            no_wa = new_wa,
            prodi = Prodi.objects.get(pk=new_prodi),
            email = new_email,
            goldar = new_goldar,
            tempat_lahir = new_t_lahir,
            tanggal_lahir = new_tgl_lahir,
            asal_daerah = new_daerah,
            alamat_dms = new_dms_ad,
            alamat_mks = new_mks_ad,
            angkatan = Angkatan.objects.get(pk=new_angkatan),
            keterangan = Status_Anggota.objects.get(pk=new_anggota),
            minat = new_minat if new_minat != "" else "Tidak ada",
            bakat = new_bakat if new_bakat != "" else "Tidak ada",
            )
        a.save()
        return redirect("/")
    else :
        context["nama"] = new_nama
        context["nim"] = new_nim
        context["prodi"] = int(new_prodi)
        context["angkatan"] = int(new_angkatan)
        context["anggota"] = int(new_anggota)
        context["goldar"] = new_goldar
        context["hp"] = new_hp
        context["wa"] = new_wa
        context["email"] = new_email
        context["t_lahir"] = new_t_lahir
        context["tgl_lahir"] = new_tgl_lahir
        context["daerah"] = new_daerah
        context["alamat_dms"] = new_dms_ad
        context["alamat_mks"] = new_mks_ad
        context["minat"] = new_minat
        context["bakat"] = new_bakat
        return render(request, 'info/add_member.html', context)

def detail(request, pk_num) :
    member = get_object_or_404(Anggota, pk=pk_num)
    return render(request, 'info/member_detail.html', {'member': member})