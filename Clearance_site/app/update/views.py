import datetime

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


from .models import Updateinfo

from accounts.models import Clearance
from accounts.decorators import allowed_users

import update.templates


@csrf_exempt
@login_required(login_url='Login')
@allowed_users(allowed_roles=["Staff"])
def updateInfo(request):

    if request.method == 'GET':
        return render(request, 'updateform.html', {})

    if request.method == 'POST':
        number = len(Updateinfo.objects.all())
        date_cleared = datetime.datetime.now()
        result = request.POST
        if result['amount'] == '':
            amount = 0
        else:
            amount = result['amount']

        try:
            infos = Updateinfo.objects.create(
                id=number, student=result['std_id'], Department=result['Department'], name=result['name'], Clear=result['clear'], ClearedBy=request.user, DateCleared=date_cleared, AmountLeft=amount)
            infos.save()

        except:
            return render(request, 'Errorpage.html', {})

        try:
            update_Clearance = Clearance.objects.get(
                Department=result["Department"], name=result['name'], student=result["std_id"])
            update_Clearance.DateCleared = date_cleared
            update_Clearance.Clear = result['clear']
            update_Clearance.ClearedBy = request.user
            update_Clearance.AmountLeft = amount
            update_Clearance.save()

        except:
            return render(request, 'Errorpage.html', {})

    return render(request, 'sucesspage.html', {})
