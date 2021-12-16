
from django.shortcuts import render, redirect
from .forms import appointmentForm, contactform,MedicineForm
from django.views.generic import View
from django.http import JsonResponse
from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required

import requests

# Create your views here.
from .models import Hospital, appointment,Department
@login_required(login_url="/MyApp/home")
def appointForm(request):
    form = appointmentForm()
    forms = MedicineForm()
    departcount = Department.objects.all().count()
    appoint = appointment.objects.all().count()

    if request.method == 'POST':
        form = appointmentForm(request.POST)
        forms = MedicineForm(request.POST)
        if form.is_valid():
            pm = form.cleaned_data.get("payment_method")
            bill = form.cleaned_data.get("hospital")
            s = form.save()
            print(s.hospital.price)

            body = {
                'first_name': form.cleaned_data['fname'],
                'last_name': form.cleaned_data['lname'],
                # 'phone': form.cleaned_data['phone'],

                'email': form.cleaned_data['email'],
                'gender': form.cleaned_data['gender'],
                # 'department': form.cleaned_data['dname'],
                # 'age': form.cleaned_data['age'],
                # 'date': form.cleaned_data['date'],

            }
            subject = "Appointment Query"

            message = " Here is the details of Patient \n " + '\n'.join(body.values())
            send_mail(
                subject,
                message,
                'basban987@gmail.com',
                [s.hospital.email],
                fail_silently=False,
            )
            print(pm)

            if pm == "Khalti":

                formid = s.id
                return redirect("/khaltirequest" + '?id=' + str(formid))



        elif forms.is_valid():
            forms.save()

        else:
            print(form.errors)

    context = {
        'form': form,
        'forms':forms,
        'appoint': appoint,
        'departcount': departcount,

    }

    return render(request, 'index.html', context)


def contact(request):
    form = contactform()
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'fm': form
    }
    return render('index.html', context)







class khaltiRequestView(View):
    def get(self, request, *args, **kwargs):
        id = request.GET.get('id')
        form=appointment.objects.get(id=id)
        hosbill = Hospital.objects.get(hname=form.hospital)
        bill = hosbill.price
        context = {
            'form': form,
            'bill': bill
        }
        return render(request, "khaltirequest.html", context)


class khaltiVerifyView(View):
    def get(self, request, *args, **kwargs):
        token = request.GET.get("token")
        amount = request.GET.get("amount")
        form = request.GET.get("form")
        datachange=appointment.objects.get(id=form)
        datachange.payment_comlpeted=True
        datachange.save()
        print(token, amount)
        # url = "https://khalti.com/api/v2/payment/verify/"
        # payload = {
        #     "token": token,
        #     "amount": amount
        # }
        # headers = {
        #     "Authorization": "test_secret_key_c62e58d53057447087754a7e3d34c7db"
        # }
        #
        # response = requests.post(url, payload, headers=headers)
        # print(response)
        data = {
            "success": True
        }
        return JsonResponse(data)
