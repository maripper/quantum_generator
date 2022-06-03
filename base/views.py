from django.shortcuts import render

import requests as req

from django.http import JsonResponse,HttpResponse  

import random

from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

import json

import ast

# perform business logic

@csrf_exempt

def quantum_computer(request):

    return render(request,"home.html",{})

    # perform business logic

 

@csrf_exempt  

def start(request):

    n = request.POST

    n = 100

    # response= req.post('https://qubit-operators.herokuapp.com/qubit_operators/receiver/',data={'size':n})

    # response= req.post('https://qubit-operators.herokuapp.com/qubit_operators/safe_poc/',data={'size':n})

    response= req.post('https://qubit-operators.herokuapp.com/qubit_operators/safe_poc/',data={'size':n}).json()['context']

    # response = response.replace("'", '"')

    response = json.loads(response)

    # response = ast.literal_eval(response)

    print('RESPONSE: -------------------------------------\n',response)

 

    return JsonResponse({'status':response['status'],'sender_key':response['sender_key'],'sender_sample':response['sender_sample'],'receiver_key':response['receiver_key'],'receiver_sample':response['receiver_sample'],'receiver_results':response['receiver_results'],'sender_bits':response['sender_bits'],'sender_base':response['sender_base'],'n':response['n']})

 

# @csrf_exempt

# def start(request):

#     n=0

#     sender= req.post('http://127.0.0.1:8000/qubit_operators/restart/',data={ })

#     while(n<32):

#         Q = [0, 1]

#         print(random.choice(Q))

#         Q = random.choice(Q)

#         sender= req.post('http://127.0.0.1:8000/qubit_operators/receiver/',data={'bit':Q})

#         receiver= req.post('http://127.0.0.1:8000/qubit_operators/sender/',data={'bit':Q})

#         print(sender,receiver)

#         n = n+1

#         print(Q,n)

#     dict = req.post('http://127.0.0.1:8000/qubit_operators/compare/',data={'size':32})

#     # print(type(dict))  

 

#     return JsonResponse(dict.json())
