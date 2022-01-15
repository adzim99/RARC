from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from functions.models import Applicant, Booking
from .models import *
from .forms import *
from .filters import *
from .decorators import *

# Create your views here.

@unauthenticated_user
def officeRegister(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            group = Group.objects.get(name='office')
            user.groups.add(group)
            Office.objects.create(
                user=user,
                staff_no=user.username,
                )
            
            messages.success(request, 'Account was created for ' + username)
            return redirect('office_login')

    context = {'form':form}
    return render(request, 'office_register.html', context)

@unauthenticated_user
def officeLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('office_account')                       
        else:
            messages.info(request, 'Incorrect username OR password')

    context = {}

    return render(request, 'office_login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('office_login')

@login_required(login_url='office_login')
def home(request):
    applicant = Applicant.objects.all()
    booking = Booking.objects.all()

#    total_applicant = applicant.count()

    total_booking = booking.count()
    approved = booking.filter(booking_status='Approved').count()
    pending = booking.filter(booking_status='Pending').count()

    context = {'applicant':applicant, 'booking':booking, 'total_booking':total_booking, 'approved':approved, 'pending':pending}

    return render(request, 'index.html', context)

@login_required(login_url='office_login')
def applicant(request, pk):
    applicant = Applicant.objects.get(id=pk)
    booking = applicant.booking_set.all()

    total_booking = booking.count()
    approved = booking.filter(booking_status='Approved').count()
    pending = booking.filter(booking_status='Pending').count()

    myFilter = BookingFilter(request.GET, queryset=booking)
    booking = myFilter.qs

    context = {'applicant':applicant, 'booking':booking, 'total_booking':total_booking, 'approved':approved, 'pending':pending, 'myFilter':myFilter}

    return render(request, 'applicant.html', context)

@login_required(login_url='applicant_login')
@allowed_users(allowed_roles=['office'])
def officeAccount(request):
    office = request.user.office
    form = OfficeForm(instance=office)

    if request.method == 'POST':
        form = OfficeForm(request.POST, request.FILES, instance=office)
        if form.is_valid:
            form.save()

    context = {'form':form}

    return render(request, 'office_account.html', context)

@login_required(login_url='office_login')
def booking(request, pk):
    BookingFormSet = inlineformset_factory(Applicant, Booking, fields=('laboratory_code','number_of_users','HI_work_activity','HI_hazard','HI_source','RA_existing_risk_control','RA_likelihood','RA_severity','RA_risk','RC_countermeasure','RC_PIC'), extra=1)
    applicant = Applicant.objects.get(id=pk)
    bookingset = BookingFormSet(queryset=Booking.objects.none(), instance=applicant)
#    form = BookingForm(initial={'applicant':applicant})

    if request.method == 'POST':
#        form = BookingForm(request.POST)
        bookingset = BookingFormSet(request.POST, instance=applicant)
        if bookingset.is_valid():
            bookingset.save()
            return redirect('/')

    context = {'bookingset':bookingset}
    
    return render(request, 'booking.html', context)

@login_required(login_url='office_login')
def editBooking(request, pk):
    booking = Booking.objects.get(id=pk)
    bookingset = BookingForm(instance=booking)

    if request.method == 'POST':
        bookingset = BookingForm(request.POST, instance=booking)
        if bookingset.is_valid():
            bookingset.save()
            return redirect('/')

    context = {'bookingset':bookingset}

    return render(request, 'booking.html', context)

@login_required(login_url='office_login')
def deleteBooking(request, pk):
    booking = Booking.objects.get(id=pk)

    if request.method == "POST":
        booking.delete()
        return redirect('/')

    context = {'booking':booking}

    return render(request, 'delete.html', context)

@login_required(login_url='office_login')
def officeFeedback(request):
    if request.method == 'POST':
        comment = OfficeFeedbackForm(request.POST)
        if comment.is_valid():
            try:
                comment.save()
                return redirect('/')
            except:
                pass
    else:
        comment = OfficeFeedbackForm()
    return render(request, 'office_feedback.html', {'comment':comment})