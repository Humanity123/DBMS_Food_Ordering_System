from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomerForm, RestForm, MenuForm, OrderForm, ROrderDetailsForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Menu, CustomUser, Order, OrderDetails


# Create your views here.

def index(request):
    context = RequestContext(request)
    return render(request, 'cibusapp1/index.html', {})




def cregister(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    
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
            return index(request)

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
            return index(request)

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

        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                login(request, user)
                return redirect(restaurant)
            else:
                
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
		return HttpResponse("You are not authorised to view this page")
	context = RequestContext(request)
	return render(request, 'cibusapp1/restaurant.html', {})


@login_required(login_url='/cibusapp1/clogin/')
def customer(request):
	if request.user.user_type == 'R':
		return HttpResponse("You are not authorised to view this page")
	context = RequestContext(request)
	return render(request, 'cibusapp1/customer.html', {})



@login_required(login_url='/cibusapp1/rlogin/')
def add_dish(request):
    if request.user.user_type == 'C':
        return HttpResponse("You are not authorised to view this page")
    
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
            return restaurant(request)

        else:
            return HttpResponse("Error in signup.")
            print user_form.errors, profile_form.errors

    else:
        user_form = MenuForm()
        
    return render(request, 'cibusapp1/add_dish.html', {'user_form': user_form})


def catselect(request):
    context = RequestContext(request)
    if request.method == 'POST':
        order_form = OrderForm(data=request.POST)
        if order_form.is_valid():
            
            data = order_form.cleaned_data
            c=data['category']
            # print c 
            return searchres(request, c)
    else:
        order_form = OrderForm()
        return render(request, 'cibusapp1/catselect.html',{'order_form': order_form}) 


def searchres(request,c):
    print c
    query_result= Menu.objects.filter(category=c)
    x=[(y.restaurant.first_name,y.restaurant.username) for y in query_result]
    seen = set()
    z=[item for item in x if item[1] not in seen and not seen.add(item[1])]
    
    for s in z:
        print s[0]
    # print query_result
    return render(request, 'cibusapp1/searchres.html', {'query_result': z,'category':c})


def restdish(request,username,category):
    
    return HttpResponse("rest hai %s " %category)


# NOTE: COPIED IN RORDERS_INFO
@login_required(login_url='/cibusapp1/rlogin/')
def rorders(request):
    if request.user.user_type == 'C':
        return HttpResponse("Ma chuda bc")

    result = Order.objects.filter(restaurant__username = request.user.username)

    return render(request, 'cibusapp1/rorders.html', {'result': result})


@login_required(login_url='/cibusapp1/rlogin/')
def rorders_info(request, orderid):
    if request.user.user_type == 'C':
        return HttpResponse("Ma chuda bc")
    
    if request.method == 'POST':
        rorder_details_form = ROrderDetailsForm(data=request.POST)

        if rorder_details_form.is_valid():
            data = rorder_details_form.cleaned_data
            Order.objects.filter(orderid = orderid).update(status = data['status'])    
            result = Order.objects.filter(restaurant__username = request.user.username)
            return render(request, 'cibusapp1/rorders.html', {'result': result})
        else:
            print rorder_details_form.errors
            return HttpResponse("Unknown Error")

    else:
        x = Order.objects.filter(orderid = orderid).first()
        rorder_details_form = ROrderDetailsForm()
        rorder_details_form.fields["first_name"].initial = x.customer.first_name
        rorder_details_form.fields["last_name"].initial = x.customer.last_name
        rorder_details_form.fields["address"].initial = x.customer.address
        rorder_details_form.fields["contact"].initial = x.customer.contact
        rorder_details_form.fields["status"].initial = x.status
        result = OrderDetails.objects.filter(order__orderid = orderid)

        rorder_details_form.fields["amount"].initial = sum([x.dish.price * x.qty for x in result])
        
    return render(request, 'cibusapp1/rordersdetails.html', {'rorder_details_form': rorder_details_form, 'result': result})

@login_required(login_url='/cibusapp1/clogin/')
def myorder(request):
    context = RequestContext(request)
    username = request.user.username
    #result = Order.objects.raw('select * from Order where customer__username = %s order by status',username)
    result = Order.objects.filter(customer__username = username).order_by('status')
    return render(request, 'cibusapp1/order.html',{'result':result})

@login_required(login_url='/cibusapp1/clogin/')
def orderinfo(request,orderid):
    context = RequestContext(request)
    #result = Order.objects.raw('select * from Order where customer__username = %s order by status',username)
    result = OrderDetails.objects.filter(order__orderid = orderid)#.order_by('qty')
    total = 0
    for r in result:
        total += r.qty*r.dish.price
    
    print type(result)
    return render(request, 'cibusapp1/orderdetail.html',{'result':result,'total':total})
