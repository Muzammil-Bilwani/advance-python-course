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