from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomerForm, RestForm, MenuForm, OrderForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    context = RequestContext(request)
    return render(request, 'cibusapp1/index.html', {})


# def cregister(request):
# 	context = RequestContext(request)
# 	user_form = CustomerForm()
# 	registered = False
# 	return render(request, 'cibusapp1/cregister.html', {'user_form': user_form, 'registered': registered})

def cregister(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = CustomerForm(data=request.POST)
        

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            
            registered = True
            return sucess(context)

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            return HttpResponse("Error in signup.")
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = CustomerForm()
        
    # Render the template depending on the context.
    # return render_to_response(
    #         'register.html',
    #         {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
    #         context)
	return render(request, 'cibusapp1/cregister.html', {'user_form': user_form, 'registered': registered})


def rregister(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = RestForm(data=request.POST)
        

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.user_type='R'
            user.save()

            
            registered = True
            return sucess(context)

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            return HttpResponse("Error in signup.")
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = RestForm()
        
    # Render the template depending on the context.
    # return render_to_response(
    #         'register.html',
    #         {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
    #         context)
	return render(request, 'cibusapp1/rregister.html', {'user_form': user_form, 'registered': registered})

def clogin(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return redirect(customer)
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'cibusapp1/clogin.html', {})



def rlogin(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return redirect(restaurant)
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'cibusapp1/rlogin.html', {})

@login_required(login_url='/cibusapp1/rlogin/')
def restaurant(request):
	if request.user.user_type == 'C':
		return HttpResponse("Ma chuda bc")
	context = RequestContext(request)
	return render(request, 'cibusapp1/restaurant.html', {})


@login_required(login_url='/cibusapp1/clogin/')
def customer(request):
	if request.user.user_type == 'R':
		return HttpResponse("Ma chuda bc")
	context = RequestContext(request)
	return render(request, 'cibusapp1/customer.html', {})


@login_required(login_url='/cibusapp1/rlogin/')
def add_dish(request):
    if request.user.user_type == 'C':
        return HttpResponse("Ma chuda bc")
    
    context = RequestContext(request)

    if request.method == 'POST':
        user_form = MenuForm(data=request.POST)

        if user_form.is_valid():
            data = user_form.cleaned_data
            m = Menu()
            r = CustomUser.objects.get(username = request.user.username)
            m.name = data['name']
            m.price = data['price']
            m.category = data['category']
            m.restaurant = r
            m.save()
            return sucess(context)

        else:
            return HttpResponse("Error in signup.")
            print user_form.errors, profile_form.errors

    else:
        user_form = MenuForm()
        
    return render(request, 'cibusapp1/add_dish.html', {'user_form': user_form})


def catselect(request):
    context = RequestContext(request)
    if request.method == 'POST':
        return render(request, 'cibusapp1/catselect.html',{}) 
    else:
        order_form = OrderForm()
        return render(request, 'cibusapp1/catselect.html',{'order_form': order_form}) 