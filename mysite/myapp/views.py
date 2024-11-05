import pandas as pd
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.http import HttpResponse, HttpResponseRedirect

def scrape(request):
    if request.method == "POST":
        site = request.POST.get('site', '')
        element_type = request.POST.get('element_type', 'a')
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')
        
        # Scraping logic based on element type
        if element_type == 'a' or element_type == 'all':
            for link in soup.find_all('a'):
                link_address = link.get('href')
                link_text = link.string or 'No Link Text'
                Link.objects.create(address=link_address, name=link_text)
        
        if element_type == 'img' or element_type == 'all':
            for image in soup.find_all('img'):
                image_src = image.get('src')
                image_alt = image.get('alt', 'No Alt Text')
                Link.objects.create(address=image_src, name=image_alt)
        
        if element_type == 'h1' or element_type == 'all':
            for header in soup.find_all('h1'):
                header_text = header.get_text(strip=True)
                Link.objects.create(address='#', name=header_text)
        
        if element_type == 'p' or element_type == 'all':
            for paragraph in soup.find_all('p'):
                paragraph_text = paragraph.get_text(strip=True)
                Link.objects.create(address='#', name=paragraph_text)
        
        if element_type == 'h2' or element_type == 'all':
            for header in soup.find_all('h2'):
                header_text = header.get_text(strip=True)
                Link.objects.create(address='#', name=header_text)
        
        return HttpResponseRedirect('/')
    
    else:
        data = Link.objects.all()
    
    return render(request, "myapp/result1.html", {'data': data})

def clear(request):
    Link.objects.all().delete()
    return render(request, 'myapp/result1.html')

def export_csv(request):
    links = Link.objects.all().values('address', 'name')
    df = pd.DataFrame(list(links))  # Convert queryset to DataFrame
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="scraped_data.csv"'
    df.to_csv(path_or_buf=response, index=False)
    return response

def export_excel(request):
    links = Link.objects.all().values('address', 'name')
    df = pd.DataFrame(list(links))  # Convert queryset to DataFrame
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="scraped_data.xlsx"'
    with pd.ExcelWriter(response, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Scraped Data')
    return response
