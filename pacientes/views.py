from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Pacientes, Tarefas, Consultas, Visualizacoes
from django.contrib import messages
from django.contrib.messages import constants


def pacientes(request):
    if request.method == 'GET':
        pacientes = Pacientes.objects.all()
        
        return render(request, 'pacientes.html', {'reasons': Pacientes.reason_choices, 'pacientes': pacientes})
    
    elif request.method == 'POST':
        name = request.POST.get('nome')
        email = request.POST.get('email')
        tel = request.POST.get('telefone')
        reason = request.POST.get('queixa')
        photo = request.FILES.get('foto')
        
        if len(name.strip()) == 0 or not photo:
            messages.add_message(request, constants.ERROR, 'O campo nome e foto são obrigatórios')
            return redirect('pacientes')
            
        paciente = Pacientes(
            name=name,
            email=email,
            tel=tel,
            reason_for_visit=reason,
            photo=photo
        )
        
        paciente.save()
        messages.add_message(request, constants.SUCCESS, 'Paciente adicionado com sucesso')
        
        return redirect('pacientes')


def paciente_view(request, id):
    paciente = Pacientes.objects.get(id=id)
    if request.method == 'GET':
        tarefas = Tarefas.objects.all()
        consultas = Consultas.objects.filter(paciente=paciente)
        
        tuple_grafico = ([str(i.data) for i in consultas], [str(i.humor) for i in consultas])
        
        return render(request, 'paciente.html', {'paciente': paciente, 'tarefas': tarefas, 'consultas': consultas, 'tuple_grafico': tuple_grafico})
    
    elif request.method == 'POST':
        humor = request.POST.get('humor')
        registro_geral = request.POST.get('registro_geral')
        video = request.FILES.get('video')
        tarefas = request.POST.getlist('tarefas')
        
        consultas = Consultas(
            humor=int(humor),
            registro_geral=registro_geral,
            video=video,
            paciente=paciente,
        )
        consultas.save()
        
        for id in tarefas:
            tarefa = Tarefas.objects.get(id=id)
            consultas.tarefas.add(tarefa)
            
        consultas.save()
        print(f'Id do paciente {id}')
        messages.add_message(request, constants.SUCCESS, 'Registro de consulta adicionado com sucesso.')
        return redirect(f'/pacientes/{id}')


def atualizar_paciente(request, id):
    payment_up_to_date = request.POST.get('payment_up_to_date')
    paciente = Pacientes.objects.get(id=id)
    
    status = True if payment_up_to_date == 'ativo' else False
    paciente.payment_up_to_date = status
    paciente.save()
    
    return redirect(f'/pacientes/{id}')


def excluir_consulta(request, id):
    consulta = Consultas.objects.get(id=id)
    consulta.delete()
    
    return redirect(f'/pacientes/{consulta.paciente.id}')


def consulta_publica(request, id):
    consulta = Consultas.objects.get(id=id)
    
    if not consulta.paciente.payment_up_to_date:
        raise Http404()
    
    view = Visualizacoes(
        consulta=consulta,
        ip=request.META['REMOTE_ADDR']
    )
    view.save()
    
    return render(request, 'consulta_publica.html', {'consulta': consulta})