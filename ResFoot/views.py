from django.shortcuts import render,redirect
from .forms import CalendarForm
from django.contrib.auth.decorators import login_required
from .forms import CalendarForm
from .models import UserProfile
# Create your views here.
def ResFoot(request):
 return render(request,'ResFoot/ResFoot.html')

@login_required
def save_date(request):
    if request.method == 'POST':
        form = CalendarForm(request.POST)
        if form.is_valid():
            selected_date = form.cleaned_data['selected_date']
            user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
            user_profile.selected_date = selected_date
            user_profile.save()
            return redirect('success', selected_date=selected_date.strftime('%Y-%m-%d'))
    else:
        form = CalendarForm()
    
    return render(request, 'ResFoot/ResFoot.html', {'form': form})
            

def success(request , selected_date):
 return render(request, 'ResFoot/success.html', {'selected_date': selected_date})