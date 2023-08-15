from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import SearchForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import InputRecord
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from rest_framework import generics
from .serializers import InputRecordSerializer

# This function will be triggered for registration view


def register(request):

    # For post request form will be validated
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('search')
    # For get request form will be Created
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def procces(val):
    # splitting the string where ',' detected and putting the valus in a temp list
    tmp = val.split(',')
    lst = []
    for num in tmp:
        lst.append(int(num))  # converting the string values to a int value
    sorted(lst, reverse=True)
    return lst

# This function will be triggered for search view


@login_required(login_url='/login/')
def search(request):
    if request.method == 'POST':  # if it is a Post request
        form = SearchForm(request.POST)
        if form.is_valid():  # validating the form
            # getting the input string
            input = form.cleaned_data['input_values']
            # getting the search value
            search = form.cleaned_data['search_value']
            processed_input = procces(input)  # proccesing the input string
            result = False
            InputRecord.objects.create(
                user=request.user, input_values=processed_input)  # creating a record in the database table
            if search in processed_input:  # checking is the search value exist in the input
                result = True
            return render(request, 'search/search.html', {'form': form, 'search_result': result})
    else:
        form = SearchForm()
    return render(request, 'search/search.html', {'form': form})

# This function will be triggered for login view


class LoginView(LoginView):
    def get_success_url(self):
        return reverse_lazy('search')


def custom_logout(request):
    logout(request)
    return redirect(reverse_lazy('login'))


class InputRecordList(generics.ListAPIView):
    serializer_class = InputRecordSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        start_datetime = self.request.query_params.get('start_datetime')
        end_datetime = self.request.query_params.get('end_datetime')

        queryset = InputRecord.objects.filter(
            user_id=user_id,
            timestamp__gte=start_datetime,
            timestamp__lte=end_datetime
        )
        return queryset
