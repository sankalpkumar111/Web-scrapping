# <!-- Copyright [2024] [Sankalp kumar]

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License. -->

from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.http import HttpResponseRedirect

def scrape(request):
    if request.method == "POST":
        site = request.POST.get('site', '')
        element_type = request.POST.get('element_type', 'a')  # Get the selected element type
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
