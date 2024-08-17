from django.shortcuts import render, redirect
from .forms import TINForm
from .utils import *
from .models import Organization
from django.contrib import messages
from django.urls import reverse

def org_info_view(request):
    if request.method == 'POST':
        form = TINForm(request.POST)
        if form.is_valid():
            tin = form.cleaned_data['tin']
            
            # Проверяем, существует ли уже организация с этим ИНН
            # existing_org = Organization.objects.filter(tin=tin).first()
            # if existing_org:
            #     # Если организация с таким ИНН существует, выводим сообщение и ссылку
            #     messages.warning(request, f"Организация с ИНН {tin} уже существует. Посмотрите информацию о ней <a href='{reverse('org_info')}?tin={tin}'>здесь</a>.")
            # return redirect('org_info')
            
            org_info = fetch_org_info(tin)
            if org_info:
                # Сохраняем информацию в базу данных
                organization = Organization.objects.create(
                    tin=org_info.get('TIN', 'Not Found'),
                    name=org_info.get('Name', 'Not Found'),
                    registration_date=org_info.get('RegistrationDate', 'Not Found'),
                    address=org_info.get('Address', 'Not Found')
                )
                
                # Отправляем данные в Google Sheets
                # fetch_org_info_and_send_to_gas(tin)
                
                # Получаем информацию из базы данных для отображения
                org_info_from_db = {
                    'TIN': organization.tin,
                    'Name': organization.name,
                    'RegistrationDate': organization.registration_date,
                    'Address': organization.address
                }

                # Сохраняем данные в сессии для отображения на странице
                # Отправляем данные в Google Sheets
                send_to_google_sheets(org_info_from_db)
                

                # Перенаправляем на GET-запрос для предотвращения повторной отправки формы
                return redirect('org_info')
    else:
        form = TINForm()
        
        
    all_orgs = Organization.objects.all()

    return render(request, 'org_info.html', {'form': form, 'all_orgs': all_orgs})


# Kozimjon raxmat kottakon

