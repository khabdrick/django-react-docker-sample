from django.views import View
from django.http import JsonResponse
from .models import DateTime

class DateTimeView(View):

    def get(self, request):
        date_and_time = DateTime.objects.all()

        dt_data = []
        for dt in date_and_time:
            dt_data.append({
                'date': dt.date,
                'time': dt.time,
            })

        data = {
            'dt': dt_data,
        }

        return JsonResponse(data)
