from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SalesSearchForm
from .models import Sale
from .utils import get_bookname_from_id, get_chart
import pandas as pd


#define function-based view - records(request)
#keep protected

# Create your views here.
def home(request):
   return render(request, 'sales/home.html')

#define function-based view - records(records()
@login_required
def records(request):
   #do nothing, simply display page

   #create an instance of SalesSearchForm that you defined in sales/forms.py
   form = SalesSearchForm(request.POST or None)
   sales_df = None   #initialize dataframe to None
   chart = None

   #check if the button is clicked
   if request.method == 'POST':
      #read book_tile and chart_type
      book_title = request.POST.get('book_title')
      chart_type = request.POST.get('chart_type')

      # #apply filter to extract data
      qs = Sale.objects.filter(book__name = book_title)
      if qs:   #if data found
         #convert the queryset values to pandas dataframe
         sales_df = pd.DataFrame(qs.values())

         #convert the ID to Name of book
         sales_df['book_id'] = sales_df['book_id'].apply(get_bookname_from_id)
         chart = get_chart(chart_type, sales_df, labels = sales_df['date_create'].values)

         #convert the dataframe to HTML
         sales_df= sales_df.to_html()

   #pack up data to be sent to template in the context dictionar
   context = {
      'form': form,
      'sales_df': sales_df,
      'chart': chart
   }

   #load the sales/record.html page using the data that you just prepared
   return render(request, 'sales/records.html', context)