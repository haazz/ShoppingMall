from django.shortcuts import render

def main_page(request):
    return render(request, 'single_pages/main_page.html')