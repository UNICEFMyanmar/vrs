import datetime

from django.db import connection
from django.db.models import Count
from django.http import JsonResponse
from django.utils.timezone import now

from birth_registration.models import F101
from certification.models import F103


def stat_detail_103(request, num=1):

    if num == "365":
        data = F103.objects.extra(select={'day': connection.ops.date_trunc_sql('month', 'created_at')})
    else:
        data = F103.objects.extra(select={'day': connection.ops.date_trunc_sql('day', 'created_at')})

    data = data.values("ST_DV", 'day').annotate(number=Count("pk")).filter(
        created_at__gte=(datetime.date.today() - datetime.timedelta(days=int(num) + 1))
    ).order_by('day')

    data = list(data)

    if num == "365":
        for item in data:
            item['day'] = item['day'][0:7]

    if num == "31":
        for item in data:
            item['day'] = item['day'][5:]

    return JsonResponse(data, safe=False)


def stat_detail(request, num=1):

    if num == "365":
        data = F101.objects.extra(select={'day': connection.ops.date_trunc_sql('month', 'created_at')})
    else:
        data = F101.objects.extra(select={'day': connection.ops.date_trunc_sql('day', 'created_at')})

    data = data.values("ST_DV", 'day').annotate(number=Count("pk")).filter(
        created_at__gte=(datetime.date.today() - datetime.timedelta(days=int(num) + 1))
    ).order_by('day')

    data = list(data)

    if num == "365":
        for item in data:
            item['day'] = item['day'][0:7]

    if num == "31":
        for item in data:
            item['day'] = item['day'][5:]

    return JsonResponse(data, safe=False)


def stat(request, num=1):
    data = list(
        F101.objects.values("ST_DV").annotate(number=Count("pk")).values("ST_DV", "number", )
            .filter(created_at__gte=(datetime.date.today() - datetime.timedelta(days=int(num) + 1)))
    )

    return JsonResponse(data, safe=False)


def realtime(request):

    data = F101.objects.values("id", "ST_DV", "DIS", "TWN", "NSEX", "created_at").order_by("-created_at")[:25]
    data = list(data)

    for item in data:
        item['age'] = (now() - item['created_at']).total_seconds()

    return JsonResponse(list(data), safe=False)
