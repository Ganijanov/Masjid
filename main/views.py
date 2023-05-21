from django.shortcuts import render, redirect
from . import models
from itertools import chain
import operator
viloyatlar = models.Viloyat.objects.all().order_by('name')
def count_masjids(request):
    ctsDic = {}
    for cts in models.Viloyat.objects.all():
        ctsQnt = models.Masjid.objects.filter(sh_t__viloyat=cts).count()

        ctsDic[cts] = ctsQnt
        
    return ctsDic

def masjid(request, id):
    masjid = models.Masjid.objects.get(id=id)
    context = {
        'masjid':masjid,
        'hodimlar':models.Hodim.objects.all(),
        'viloyatlar':viloyatlar,
        'ctsDic':count_masjids(request)

    }
    return render(request, 'masjid.html', context)

def mp(request):
    context = {
        'masjids':models.Masjid.objects.all(),
        'viloyatlar':viloyatlar,
        'ctsDic':count_masjids(request)

    }
    return render(request, 'index.html', context)

def about(request, id):
    context = {
        'hodim':models.Hodim.objects.get(id=id),
        'viloyatlar':viloyatlar,
        'ctsDic':count_masjids(request)
    }
    return render(request, 'about.html', context)

def sh_t_detail(request, id):
    sh_t = models.ShaharTuman.objects.get(id=id)
    context = {
        'sh_t':sh_t,
        'sh_t_masjids':models.Masjid.objects.filter(sh_t=sh_t),
        'viloyatlar':viloyatlar,
        'ctsDic':count_masjids(request)
    }
    return render(request, 'sh_t.html', context)

def viloyat_detail(request, id):
    viloyat = models.Viloyat.objects.get(id=id)
    context = {
        'viloyat':viloyat,
        'viloyat_masjids':models.Masjid.objects.filter(sh_t__viloyat=viloyat),
        'viloyatlar':viloyatlar,
        'ctsDic':count_masjids(request)
    }
    return render(request, 'viloyat.html', context  )

def serchfilter(request):
    s = request.GET.get('Ss')
    if s is not None :
        print(True)
        search = sorted(
            list(
                chain(
                    # models.Masjid.objects.filter(name__icontains=s),
                    models.ShaharTuman.objects.filter(status__icontains=s, name__icontains=s)
                )
            ),
            key=operator.attrgetter('id')
        )
        print(search)
        context = {
            'masjids':search,
            'ctsDic':count_masjids(request),
            'viloyatlar':viloyatlar,
        }
    else:
        context = {
            'ctsDic':count_masjids(request)
        }
    return render(request, 'search.html', context)