from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomerForm, RestForm, MenuForm, OrderForm, ROrderDetailsForm, CDishForm,CeditForm, ReditForm, cartForm, EmptyForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Menu, CustomUser, Order, OrderDetails, Cart
from django.contrib import messages
from django.db import connection
from datetime import datetime
# Create your views here.

def index(request):
	context = RequestContext(request)
	return render(request, 'cibusapp1/index.html', {})

@login_required
def user_logout(request):
	# Since we know the user is logged in, we can now just log them out.
	logout(request)

	# Take the user back to the homepage.
	return redirect('/cibusapp1')



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
			# messages.success(request, "Error"+str(user_form.errors))
			return render(request, 'cibusapp1/cregister.html', {'user_form': user_form, 'registered': registered})
			# return HttpResponse("Error in signup.")
			# print user_form.errors, profile_form.errors

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
			return render(request, 'cibusapp1/rregister.html', {'user_form': user_form, 'registered': registered})


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
	# print help(CustomUser)
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
				return HttpResponse("Your Cibus account is disabled.")
		else:
			# Bad login details were provided. So we can't log the user in.
			print "Invalid login details: {0}, {1}".format(username, password)
			messages.success(request, "Invalid login details")
			return render(request, 'cibusapp1/clogin.html')

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
			messages.success(request, "Invalid login details")
			return render(request, 'cibusapp1/rlogin.html')

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
	return render(request, 'cibusapp1/restaurant.html', {'Restaurant':request.user.first_name})


@login_required(login_url='/cibusapp1/clogin/')
def customer(request):
	if request.user.user_type == 'R':
		return HttpResponse("You are not authorised to view this page")
	context = RequestContext(request)
	cursor = connection.cursor()
	cursor.execute('SELECT name,first_name from cibusapp1_CustomUser, (SELECT name,restaurant_id from cibusapp1_Menu where category in (SELECT category from cibusapp1_Menu where id in (SELECT dish_id from cibusapp1_OrderDetails where order_id in (select orderid from cibusapp1_Order where customer_id=%s  )) group by category order by count(category) desc limit 1)) where id = restaurant_id',[request.user.id])
	
	row=cursor.fetchall()

	for r in row: 
		print r 
	return render(request, 'cibusapp1/customer.html', {'Customer':request.user.first_name, 'dishes':row[0:5], 'toprint':len(row)!=0})



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
			if Menu.objects.filter(restaurant__username = request.user.username, name = m.name).exists():
				messages.success(request, 'Dish already exists')
				return render(request, 'cibusapp1/add_dish.html', {'user_form': user_form})
				# render_to_response('cibusapp1/restaurant.html', message='Dish already exists')
			m.save()
			return restaurant(request)

		else:
			return HttpResponse("Error in signup.")
			print user_form.errors, profile_form.errors

	else:
		user_form = MenuForm()
		
	return render(request, 'cibusapp1/add_dish.html', {'user_form': user_form})

@login_required(login_url='/cibusapp1/clogin/')
def catselect(request):
	if request.user.user_type == 'R':
		return HttpResponse("You are not authorised to view this page")
	context = RequestContext(request)
	if request.method == 'POST':
		order_form = OrderForm(data=request.POST)
		if order_form.is_valid():
			
			data = order_form.cleaned_data
			c=data['category']
			# print c 
			# return searchres(request, c)
			return redirect('/cibusapp1/customer/searchres/'+c)
	else:
		order_form = OrderForm()
		return render(request, 'cibusapp1/catselect.html',{'order_form': order_form}) 


@login_required(login_url='/cibusapp1/clogin/')
def searchres(request,c):
	if request.user.user_type == 'R':
		return HttpResponse("You are not authorised to view this page")
	cursor = connection.cursor()
	cursor.execute('SELECT first_name,username,address,contact FROM cibusapp1_CustomUser WHERE user_type==%s AND id in (SELECT restaurant_id FROM cibusapp1_Menu WHERE category==%s)',['R',c])
	rows = cursor.fetchall()
	for item in rows:
		print item
	return render(request, 'cibusapp1/searchres.html', {'query_result': rows,'category':c})



@login_required(login_url='/cibusapp1/clogin/')
def restdish(request,username,category):
	if request.user.user_type == 'R':
		return HttpResponse("You are not authorised to view this page")
	cat_dishes = Menu.objects.filter(restaurant__username = username, category = category)
	non_cat_dishes = Menu.objects.filter(restaurant__username = username).exclude(category = category)

	return render(request, 'cibusapp1/restdish.html', {'cat_dishes': cat_dishes, 'non_cat_dishes':non_cat_dishes, 'username':username,'category':category})

@login_required(login_url='/cibusapp1/clogin/')
def restdishselect(request,username,category,name):
	if request.user.user_type == 'R':
		return HttpResponse("You are not authorised to view this page")

	if request.method == 'POST':
		cdish_form = CDishForm(data=request.POST)

		if cdish_form.is_valid():
			data = cdish_form.cleaned_data
			c = Cart()
			c.customer = request.user
			c.dish = Menu.objects.filter(restaurant__username = username,name = name).first()
			c.qty = data["qty"]
			d = Cart.objects.filter(customer__username = request.user.username)
			e = [x.dish.restaurant.username for x in d]
			print e
			if (len(e) > 0):
				if (e[0] != username):
					Cart.objects.filter(customer__username = request.user.username).delete()
			c.save()
			# cat_dishes = Menu.objects.filter(restaurant__username = username, category = category)
			# non_cat_dishes = Menu.objects.filter(restaurant__username = username).exclude(category = category)
			return redirect('/cibusapp1/customer/restdish/'+username+'/'+category)
		else:
			print cdish_form.errors
			return HttpResponse("Unknown Error")
	else:
		cdish_form = CDishForm()

	return render(request, 'cibusapp1/resetdishselect.html', {'cdish_form': cdish_form})


# NOTE: COPIED IN RORDERS_INFO
@login_required(login_url='/cibusapp1/rlogin/')
def rorders(request):
	if request.user.user_type == 'C':
		return HttpResponse("You are not authorised to view this page")

	result = Order.objects.filter(restaurant__username = request.user.username)

	return render(request, 'cibusapp1/rorders.html', {'result': result})


@login_required(login_url='/cibusapp1/rlogin/')
def rorders_info(request, orderid):
	if request.user.user_type == 'C':
		return HttpResponse("You are not authorised to view this page")
	
	if request.method == 'POST':
		rorder_details_form = ROrderDetailsForm(data=request.POST)

		if rorder_details_form.is_valid():
			data = rorder_details_form.cleaned_data
			Order.objects.filter(orderid = orderid).update(status = data['status'])    
			# result = Order.objects.filter(restaurant__username = request.user.username)
			return redirect('/cibusapp1/restaurant/rorders')
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
		rorder_details_form.fields["when"].initial = x.when
		result = OrderDetails.objects.filter(order__orderid = orderid)

		rorder_details_form.fields["amount"].initial = sum([x.dish.price * x.qty for x in result])
		
	return render(request, 'cibusapp1/rordersdetails.html', {'rorder_details_form': rorder_details_form, 'result': result})

@login_required(login_url='/cibusapp1/clogin/')
def myorder(request):
	if request.user.user_type == 'R':
		return HttpResponse("You are not authorised to view this page")
	context = RequestContext(request)
	username = request.user.username
	result = Order.objects.filter(customer__username = username).order_by('status')
	return render(request, 'cibusapp1/order.html',{'result':result})

@login_required(login_url='/cibusapp1/clogin/')
def orderinfo(request,orderid):
	if request.user.user_type == 'R':
		return HttpResponse("You are not authorised to view this page")
	context = RequestContext(request)
	#result = Order.objects.raw('select * from Order where customer__username = %s order by status',username)
	result = OrderDetails.objects.filter(order__orderid = orderid).order_by('qty')
	total = 0
	for r in result:
		total += r.qty*r.dish.price
	when = Order.objects.get(orderid = orderid).when
	return render(request, 'cibusapp1/orderdetail.html',{'result':result,'total':total, 'when':when})


@login_required(login_url='/cibusapp1/clogin/')
def cart(request):
	if request.user.user_type == 'R':
		return HttpResponse("You are not authorised to view this page")
	context = RequestContext(request)
	cart_form = cartForm()
	if request.method == 'POST':
		username = request.user.username
		cartData = Cart.objects.filter(customer__username = username)
		order = Order()
		orderdetail = OrderDetails()
		c = 0 
		r = 0
		maxId = -1
		for i in cartData:
			c = i.customer
			r = i.dish.restaurant
		if c ==0:
			messages.success(request, "Empty cart")
			return render(request, 'cibusapp1/cart.html')

		OrderIter = Order.objects.all()
		for i in OrderIter:
			maxId = max(maxId,i.orderid)
		order.orderid = maxId+1
		order.customer = c
		order.restaurant = r
		order.when = datetime.now()
		order.save()
		for i in cartData:
			orderdetail = OrderDetails()
			orderdetail.dish = i.dish
			orderdetail.qty = i.qty
			orderdetail.order = order
			orderdetail.save()
		Cart.objects.filter(customer__username = username).delete()
		messages.success(request, "Order placed successfully")
		return redirect("/cibusapp1/customer")
	else:
		username = request.user.username
		result = Cart.objects.filter(customer__username = username).order_by('qty')
		r = 0
		if result.exists():
			r = result.first().dish.restaurant
		total = 0
		for x in result:
			total += x.qty*x.dish.price
		if r == 0:
			return render(request, 'cibusapp1/cart.html',{'cart_form':cartForm,'result':result,'total':total,'Res':'','Add':'','Con':''})			

		return render(request, 'cibusapp1/cart.html',{'cart_form':cartForm,'result':result,'total':total,'Res':r.first_name,'Add':r.address,'Con':r.contact})

@login_required(login_url='/cibusapp1/clogin/')
def cartinc(request,dishname):
	if request.user.user_type == 'R':
		return HttpResponse("You are not authorised to view this page")
	i=Cart.objects.filter(customer__username = request.user.username, dish__name=dishname ).first()
	print i 
	Cart.objects.filter(customer__username = request.user.username, dish__name=dishname ).update(qty=i.qty+1)
	# print 'Quantity is'
	# print 55
	return redirect("/cibusapp1/customer/cart")

@login_required(login_url='/cibusapp1/clogin/')
def cartdec(request,dishname):
	if request.user.user_type == 'R':
		return HttpResponse("You are not authorised to view this page")
	i=Cart.objects.filter(customer__username = request.user.username, dish__name=dishname ).first()
	if i.qty==1:
		Cart.objects.filter(customer__username = request.user.username, dish__name=dishname ).delete()
	else:
		Cart.objects.filter(customer__username = request.user.username, dish__name=dishname ).update(qty=i.qty-1)
	print 'Quantity is'
	print i
	return redirect("/cibusapp1/customer/cart")

@login_required(login_url='/cibusapp1/clogin/')
def cedit(request):
	if request.user.user_type == 'R':
		return HttpResponse("You are not authorised to view this page")
	context = RequestContext(request)
	username = request.user.username
	customer = CustomUser.objects.filter(username = username).first()
	if request.method == 'POST':
		# Attempt to grab information from the raw form information.
		# Note that we make use of both UserForm and UserProfileForm.
		print ('loda')
		user_form =CeditForm(request.POST, instance=request.user)
		if user_form.is_valid():
			# Save the user's form data to the database.
			# user_form = CeditForm(data=request.POST)
			data = user_form.cleaned_data
			# CustomUser.objects.filter(username = username).update(email = data['email'],first_name = data['first_name'],last_name = data['last_name'],contact=data['contact'],address=data['address'])
			user = user_form.save()

			# Now we hash the password with the set_password method.
			# Once hashed, we can update the user object.s
			user.set_password(data['password'])
			user.save()
			# Now we hash the password with the set_passwor	d method.
			# Once hashed, we can update the user object.
			messages.success(request, "Login again on password change")
			return redirect('/cibusapp1/customer')

		# Invalid form or forms - mistakes or something else?
		# Print problems to the terminal.
		# They'll also be shown to the user.
		else:
			return HttpResponse("Error in edit.")
			print user_form.errors

	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		user_form = CeditForm()
		user_form.fields["username"].initial = customer.username
		user_form.fields["email"].initial = customer.email
		# user_form.fields["password"].initial = "Enter New Password"
		user_form.fields["first_name"].initial = customer.first_name
		user_form.fields["last_name"].initial = customer.last_name
		user_form.fields["contact"].initial = customer.contact
		user_form.fields["address"].initial = customer.address
	# Render the template depending on the context.
	# return render_to_response(
	#         'register.html',
	#         {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
	#         context)
		return render(request, 'cibusapp1/cedit.html', {'user_form': user_form})


@login_required(login_url='/cibusapp1/rlogin/')
def redit(request):
	if request.user.user_type == 'C':
		return HttpResponse("You are not authorised to view this page")
	context = RequestContext(request)
	username = request.user.username
	customer = CustomUser.objects.filter(username = username).first()
	if request.method == 'POST':
		# Attempt to grab information from the raw form information.
		# Note that we make use of both UserForm and UserProfileForm.
		print ('loda')
		user_form = ReditForm(request.POST, instance=request.user)
		if user_form.is_valid():
			# Save the user's form data to the database.
			# user_form = CeditForm(data=request.POST)
			data = user_form.cleaned_data
			# CustomUser.objects.filter(username = username).update(email = data['email'],first_name = data['first_name'],last_name = data['last_name'],contact=data['contact'],address=data['address'])
			user = user_form.save()

			# Now we hash the password with the set_password method.
			# Once hashed, we can update the user object.s
			user.set_password(data['password'])
			user.save()
			messages.success(request, "Login again on password change")
			return redirect('/cibusapp1/restaurant')

		# Invalid form or forms - mistakes or something else?
		# Print problems to the terminal.
		# They'll also be shown to the user.
		else:
			return HttpResponse("Error in edit.")
			print user_form.errors

	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		user_form = ReditForm()
		user_form.fields["username"].initial = customer.username
		user_form.fields["email"].initial = customer.email
		# user_form.fields["password"].initial = "Enter New Password"
		user_form.fields["first_name"].initial = customer.first_name
		user_form.fields["contact"].initial = customer.contact
		user_form.fields["address"].initial = customer.address
	# Render the template depending on the context.
	# return render_to_response(
	#         'register.html',
	#         {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
	#         context)
		return render(request, 'cibusapp1/redit.html', {'user_form': user_form})


@login_required(login_url='/cibusapp1/clogin/')
def restalldishselect(request,username,name):
	if request.user.user_type == 'R':
		return HttpResponse("You are not authorised to view this page")

	if request.method == 'POST':
		cdish_form = CDishForm(data=request.POST)

		if cdish_form.is_valid():
			data = cdish_form.cleaned_data
			c = Cart()
			c.customer = request.user
			c.dish = Menu.objects.filter(restaurant__username = username, name = name).first()
			c.qty = data["qty"]
			d = Cart.objects.filter(customer__username = request.user.username)
			e = [x.dish.restaurant.username for x in d]
			print e
			if (len(e) > 0):
				if (e[0] != username):
					Cart.objects.filter(customer__username = request.user.username).delete()
			c.save()
			# cat_dishes = Menu.objects.filter(restaurant__username = username, category = category)
			# non_cat_dishes = Menu.objects.filter(restaurant__username = username).exclude(category = category)
			return redirect('/cibusapp1/customer/restdish/'+username)
		else:
			print cdish_form.errors
			return HttpResponse("Unknown Error")
	else:
		cdish_form = CDishForm()

	return render(request, 'cibusapp1/restalldishselect.html', {'cdish_form': cdish_form})

@login_required(login_url='/cibusapp1/clogin/')
def restalldish(request,username):
	if request.user.user_type == 'R':
		return HttpResponse("You are not authorised to view this page")
	dishes = Menu.objects.filter(restaurant__username = username)
	print 'loda'
	return render(request, 'cibusapp1/restalldish.html', {'dishes': dishes, 'username':username})

@login_required(login_url='/cibusapp1/clogin/')
def reslist(request):
	context = RequestContext(request)
	if request.user.user_type == 'R':
		return HttpResponse("You are not authorised to view this page")
	cursor = connection.cursor()
	cursor.execute('SELECT first_name,username,address,contact FROM cibusapp1_CustomUser WHERE user_type==%s ORDER BY %s',['R','first_name'])
	rows = cursor.fetchall()
	return render(request, 'cibusapp1/reslist.html',{'result':rows})



@login_required(login_url='/cibusapp1/rlogin/')
def restmenu(request):
	username = request.user.username
	if request.user.user_type == 'C':
		return HttpResponse("You are not authorised to view this page")

	dishes = Menu.objects.filter(restaurant__username = username)
	return render(request, 'cibusapp1/restmenu.html', {'dishes': dishes})