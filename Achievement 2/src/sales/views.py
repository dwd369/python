from django.shortcuts import render
from django.contrib.auth.decorators import login_required


#define function-based view - records(request)
#keep protected

# Create your views here.
def home(request):
   return render(request, 'sales/home.html')

#define function-based view - records(records()
@login_required
def records(request):
   #do nothing, simply display page    
   return render(request, 'sales/records.html')