from __future__ import annotations
from time import sleep

from pyrsistent import b


contato = {
    'nome': "",
    'telefone':"",
    'cidade': "",
    'estado':"",
    'status':""
}


sair = int(6)
aux = 0
opcao = 0
listaContatos = []




def menuInicial():
    print('************************************')
    print('                MENU                ')
    print('************************************')
    print('1. Cadastrar Pessoa na Agenda\n') #ok
    print('2. Alterar dados da Pessoa\n') #ok
    print('3. Listar Agenda\n') #ok
    print('4. Procurar pessoa na Agenda\n')#ok
    print('5. Excluir Pessoa da Agenda\n')
    print('6. Sair do sistema\n') #ok
    print('************************************')
    opcao = int(input('Selecione a opção desejada: \n ->'))
    return opcao


def cadastrar ():
    ctt = {
    'nome': "",
    'telefone':"",
    'cidade': "",
    'estado':"",
    'status':""
}
    print('************************************')
    print('             CADASTRAR              ')
    print('************************************')

    ctt['nome'] = str.upper(input('Digite o nome do contato: \n'))
    ctt['telefone'] = str.upper(input('Digite o telefone do contato: \n'))
    ctt['cidade'] = str.upper(input('Digite a cidade: \n'))
    ctt['estado'] = str.upper(input('Digite o estado: \n'))
    ctt['status'] = str.upper(input('Digite *P* para pessol e *C* para comercial: \n'))
    return(ctt)
    

def listar ():
    print('************************************')
    print('               LISTAR               ')
    print('************************************')
    if(listaContatos == []):
        print("Agenda Vazia")
    for i in range(len(listaContatos)):
        print('NOME: ',listaContatos[i]['nome'],' - ' , 'TELEFONE: ',listaContatos[i]['telefone'],' - ','CIDADE: ',listaContatos[i]['cidade'],
         ' - ', 'ESTADO: ',listaContatos[i]['estado'],' - ','STATUS: ',listaContatos[i]['status'],'\n')
    pause=input('Aperte enter para prosseguir.')
        

def imprimirContato(i):
    print('NOME: ',listaContatos[i]['nome'],' - ' , 'TELEFONE: ',listaContatos[i]['telefone'])
    print('\nCIDADE: ',listaContatos[i]['cidade'], ' - ', 'ESTADO: ',listaContatos[i]['estado'])
    print('\nSTATUS: ',listaContatos[i]['status'])
    print('\n')
    pause=input('Aperte enter para prosseguir.')

def pesquisa():
    achei=False
    print('************************************')
    print('                PESQUISAR           ')
    print('************************************')
    if(listaContatos== []):
        print('A agenda está vazia.')
        pause=input('Aperte enter para prosseguir.')
    else:
        pesquisar = str.upper(input('Informe o nome do contato: \n'))
        for i in range(len(listaContatos)):
            if (pesquisar == listaContatos[i]['nome']):
                imprimirContato(i)
                achei = True
        if(achei==False):
            print('Pessoa com o nome',pesquisar, 'não localizado')
            pause=input('Aperte enter para prosseguir.')
    

def altera():
    achei = False
    print('************************************')
    print('                 ALTERAR            ')
    print('************************************')
    if(listaContatos== []):
        print('Agenda Vazia')
        pause=input('Aperte enter para prosseguir.')
    else:
        pesquisar = str.upper(input('Informe o nome do contato a ser alterado: \n'))
        for i in range(len(listaContatos)):
            if (pesquisar == listaContatos[i]['nome']):
                listaContatos[i]=cadastrar()
                achei = True
        if(achei==False):               
            print('Pessoa com o nome',pesquisar, 'não localizado')
            pause=input('Aperte enter para prosseguir.')
    
def excluir():
    achei = False
    print('************************************')
    print('                 EXCLUIR            ')
    print('************************************')
    
    if(listaContatos == []):
            print("Agenda Vazia.")
            pause=input('Aperte enter para prosseguir.')
    else:
        pesquisar = str.upper(input('Informe o nome do contato: \n'))
        for i in range (len(listaContatos)):
            if(listaContatos[i]['nome'] == pesquisar):
                listaContatos.pop()
                print('Exclusão Realizada com Sucesso!') 
                achei=True
                pause=input('Aperte enter para prosseguir.')
        if(achei == False):
                print( pesquisar, 'não localizado')
                pause=input('Aperte enter para prosseguir.')
while(aux != sair):
    aux = int(menuInicial())
    if(aux == 1):
        listaContatos.append(cadastrar())
    elif(aux == 2):
        altera()
    elif(aux == 3):
        listar()
    elif(aux == 4):
        pesquisa()
    elif(aux == 5):
        excluir()
    elif(aux > 6):
        print('Escolha uma opção válida.')

        

