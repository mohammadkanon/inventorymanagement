from django.shortcuts import render, redirect, get_object_or_404
from inventory.models import Laptop, Desktop, Mobile
from inventory.forms import LaptopForm, DesktopForm, MobileForm

# Create your views here.
def index(request):
	return render(request, 'inventory/index.html')

def display_laptops(request):
	items = Laptop.objects.all()

	context = {
		'items': items,
		'header': 'Laptops',
	}

	return render(request, 'inventory/index.html', context)

def display_desktops(request):
	items = Desktop.objects.all()

	context = {
		'items': items,
		'header': 'Desktops',
	}

	return render(request, 'inventory/index.html', context)

def display_mobiles(request):
	items = Mobile.objects.all()

	context = {
		'items': items,
		'header': 'Mobiles',
	}

	return render(request, 'inventory/index.html', context)



# def add_laptop(request):
# 	if request.method == 'POST':
# 		form = LaptopForm(request.POST)

# 		if form.is_valid():
# 			form.save()
# 			return redirect('index')

# 	else:
# 		form = LaptopForm()

# 		return render(request, 'inventory/add-new.html', {'form': form})



# def add_desktop(request):
# 	if request.method == 'POST':
# 		form = DesktopForm(request.POST)

# 		if form.is_valid():
# 			form.save()
# 			return redirect('index')

# 	else:
# 		form = DesktopForm()

# 		return render(request, 'inventory/add-new.html', {'form': form})




# def add_mobile(request):
# 	if request.method == 'POST':
# 		form = MobileForm(request.POST)

# 		if form.is_valid():
# 			form.save()
# 			return redirect('index')

# 	else:
# 		form = MobileForm()

# 		return render(request, 'inventory/add-new.html', {'form': form})


def add_device(request, cls):

	if request.method == 'POST':
		form = cls(request.POST)

		if form.is_valid():
			form.save()
			return redirect('index')

	else:
		form = cls()

		return render(request, 'inventory/add-new.html', {'form': form})



def add_laptop(request):

	return add_device(request, LaptopForm)

def add_desktop(request):
	return add_device(request, DesktopForm)

def add_mobile(request):
	return add_device(request, MobileForm)




# def edit_laptop(request, pk):
# 	item = get_object_or_404(Laptop, pk=pk)

# 	if request.method == 'POST':
# 		form = LaptopForm(request.POST, instance=item)

# 		if form.is_valid():
# 			form.save()
# 			return redirect('index')

# 	else:
# 		form = LaptopForm(instance=item)

# 		return render(request, 'inventory/edit-item.html', {'form': form})



def edit_device(request, pk, model, cls):
	item = get_object_or_404(model, pk=pk)

	if request.method == 'POST':
		form = cls(request.POST, instance=item)

		if form.is_valid():
			form.save()
			return redirect('index')

	else:
		form = cls(instance=item)

		return render(request, 'inventory/edit-item.html', {'form': form})

def edit_laptop(request, pk):
	return edit_device(request, pk, Laptop, LaptopForm)

def edit_desktop(request, pk):
	return edit_device(request, pk, Desktop, DesktopForm)

def edit_mobile(request, pk):
	return edit_device(request, pk, Mobile, MobileForm)



def delete_laptop(request, pk):

	if request.method == 'POST':

		Laptop.objects.filter(id=request.POST['item_id']).delete()
	

	items = Laptop.objects.all()

	context = {
		'items': items,
	}

	return render(request, 'inventory/index.html', context)

def delete_desktop(request, pk):

	Desktop.objects.filter(id=pk).delete()

	items = Desktop.objects.all()

	context = {
		'items': items,
	}

	return render(request, 'inventory/index.html', context)

def delete_mobile(request, pk):
	Mobile.objects.filter(id=pk).delete()

	items = Mobile.objects.all()

	context = {
		'items': items,
	}

	return render(request, 'inventory/index.html', context)