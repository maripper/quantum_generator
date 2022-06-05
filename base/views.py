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

    # response= req.post('https://qubit-operators.herokuapp.com/qubit_operators/safe_poc/',data={'size':n}).json()['context']
    response= req.post('https://qubit-operators.herokuapp.com/qubit_operators/safe_poc/',data={'size':n}).json()['context']

    # response = response.replace("'", '"')

    response = json.loads(response)

    # response = ast.literal_eval(response)

    print('RESPONSE: -------------------------------------\n',response)

 

    return JsonResponse({'sender_and_receiver_comparing_sample_equivalent':response['status'],'message':response['sender_data'],'sender_key':response['sender_key'],'receiver_key':response['receiver_key'],'receiver_base':response['receiver_base'],'sender_base':response['sender_base'],'receiver_results':response['receiver_data'],'sender_results':response['sender_data'],'tests_size':response['n']})

@csrf_exempt  

def start_eve(request):

    n = request.POST

    n = 100

    # response= req.post('https://qubit-operators.herokuapp.com/qubit_operators/receiver/',data={'size':n})

    # response= req.post('https://qubit-operators.herokuapp.com/qubit_operators/safe_poc/',data={'size':n})

    # response= req.post('https://qubit-operators.herokuapp.com/qubit_operators/safe_poc/',data={'size':n}).json()['context']
    response= req.post('https://qubit-operators.herokuapp.com/qubit_operators/eve_poc/',data={'size':n}).json()['context']

    # response = response.replace("'", '"')

    response = json.loads(response)

    # response = ast.literal_eval(response)

    print('RESPONSE: -------------------------------------\n',response)

 

    return JsonResponse({'sender_and_receiver_comparing_sample_equivalent':response['status'],'sender_key':response['sender_key'],'receiver_key':response['receiver_key'],'receiver_base':response['receiver_base'],'sender_base':response['sender_base'],'tests_size':response['n'],'message':response['sender_bits'],'receiver_results':response['receiver_data'],'sender_results':response['sender_data'],'intercepted_message':response['intercepted_message']})


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
