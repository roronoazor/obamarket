from django.shortcuts import render


def index(request):
    context = {
        'is_index': True,
        'is_prop': False,
        'is_cont': False,
        'is_about':False,
        'carousels': [
            ['assets/img/latest-1.jpeg', 'assets/img/latest-2.jpeg'],
            ['assets/img/latest-3.jpeg', 'assets/img/latest-4.jpeg'],
            ['assets/img/latest-5.jpeg', 'assets/img/latest-1.jpeg'],
            ['assets/img/latest-1.jpeg', 'assets/img/latest-2.jpeg'],
            ['assets/img/latest-3.jpeg', 'assets/img/latest-4.jpeg'],
            ['assets/img/latest-5.jpeg', 'assets/img/latest-1.jpeg'],
            ['assets/img/latest-1.jpeg', 'assets/img/latest-2.jpeg'],
            ['assets/img/latest-3.jpeg', 'assets/img/latest-4.jpeg'],
            ['assets/img/latest-5.jpeg', 'assets/img/latest-1.jpeg'],
        ]
    }
    return render(request, 'core/index.html', context)


def properties(request):
    context = {
        'is_index': False,
        'is_prop': True,
        'is_cont': False,
        'is_about':False,
    }
    return render(request, 'core/property-grid.html', context)

def contact_us(request):
    context = {
        'is_index': False,
        'is_prop': False,
        'is_cont': True,
        'is_about':False,
    }
    return render(request, 'core/contact.html', context)

def about_us(request):
    context = {
        'is_index': False,
        'is_prop': False,
        'is_cont': False,
        'is_about':True,
    }
    return render(request, 'core/about.html', context)