from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm, ListingForm


# Create your views here.
def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", context={'bands': bands})


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})


def band_create(request):
    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()

    return render(request, "listings/band_create.html", context={'form': form})


def band_change(request, id):
    band = Band.objects.get(id=id)
    if request.method == "POST":
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band_change.html', {'form': form})


def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        band.delete()
        return redirect('band-list')
    return render(request,
                  'listings/band_delete.html',
                  {'band': band})


def about(request):
    return render(request, 'listings/about.html')


def listing_list(request):
    Liste = Listing.objects.all()
    return render(request, 'listings/listing_list.html', context={"Liste": Liste})


def listing_detail(request, id):
    Liste = Listing.objects.get(id=id)
    return render(request, 'listings/listing_detail.html', context={"Liste": Liste})


def listing_create(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            Liste = form.save()
            return redirect('listing-detail', Liste.id)
    else:
        form = ListingForm()

    return render(request, "listings/listing_create.html", {'form': form})


def listing_change(request, id):
    Liste = Listing.objects.get(id=id)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=Liste)
        if form.is_valid():
            Liste = form.save()
            return redirect('listing-detail', Liste.id)
    else:
        form = ListingForm(instance=Liste)
    return render(request, 'listings/listing_change.html', {'form': form})


def listing_delete(request, id):
    Liste = Listing.objects.get(id=id)
    if request.method == 'POST':
        Liste.delete()
        return redirect('listing-list')
    return render(request,
                  'listings/listing_delete.html',
                  {'Liste': Liste})


def contact(request):
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)

    if request.method == "POST":
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()

    return render(request, 'listings/contact.html', {'form': form})
