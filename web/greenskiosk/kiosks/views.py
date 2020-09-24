from django.shortcuts import render,redirect
from .forms import KioskForm
from catalogue import views, templates
# Create your views here.



def upload_kiosk(request):

    form = KioskForm()
    if request.method == "POST":
        form = KioskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploads')

    else:
        form = KioskForm
    return render(request, 'kiosks/upload_kiosk.html', {'form': form} )