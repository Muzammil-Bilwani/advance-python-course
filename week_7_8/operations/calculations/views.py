from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def sum_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        numbers = data.get('numbers', [])
        total_sum = sum(numbers)  # Sum of a list
        return JsonResponse({'sum': total_sum})


@csrf_exempt
def average_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        numbers = data.get('numbers', [])
            
        if numbers:
            average = sum(numbers) / len(numbers)
        return JsonResponse({'average': average})
        
@csrf_exempt
def product_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        numbers = data.get('numbers', [])
        product = 1
        for number in numbers:
            product *= number
        return JsonResponse({'Product': product})
    
@csrf_exempt
def split_evenly(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        total = data.get('total', 0)
        numberOfPersons = data.get('numberOfPersons', 0)
        split = total / numberOfPersons
        return JsonResponse({'split_per_person': split})
    
@csrf_exempt
def split_unevenly(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        total = data.get('total', 0)
        people = data.get('people',[])
        evenSplit = total / len(people)
        split = {}
        for person in people:
            print(person)
            split[person["name"]] = evenSplit - person["contribution"]
        print(split)
        return JsonResponse({'split': split})

def split_evenly_with_tax_tip(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        total = data.get('total', 0)
        numberOfPersons = data.get('numberOfPersons', 0)
        tax = data.get('tax', 0)
        tip = data.get('tip', 0)
        total += tax + tip
        split = total / numberOfPersons
        return JsonResponse({'split_per_person': split})     

def split_evenly_with_discount(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        total = data.get('total', 0)
        numberOfPersons = data.get('numberOfPersons', 0)
        discount = data.get('discount', 0)
        total -= discount
        split = total / numberOfPersons
        return JsonResponse({'split_per_person': split})