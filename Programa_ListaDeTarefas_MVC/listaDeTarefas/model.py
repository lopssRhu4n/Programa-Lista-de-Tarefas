from datetime import date
from re import A
from classeTarefa import Tarefa
from tabulate import tabulate
import func

funcao = func
class model:
    def __init__(self):
        self.listaTarefa = []
        self.nomesEDatasDasTarefas =[]

           
    def salvaDadosTar(self):
        with open('arquivo_listas.txt', 'w') as arquivo:           
            for tar in self.listaTarefa:    
                arquivo.write(tar.getNomeTar() + ';')
                arquivo.write(tar.getPrazo() + ';')
                arquivo.write(tar.getStatus() + '\n')
                
    def lerTarefas(self):   
        with open('arquivo_listas.txt', 'r') as arquivo:
            dadosDasTarefas = arquivo.readlines()
            for linha in dadosDasTarefas:  
                if linha != '\n':
                    tar = Tarefa()
                    linha = linha.split(';')
                    nomeDaTarefa = linha[0]
                    dataFdaTarefa = linha[1]
                    statusDaTarefa = linha[2].replace('\n', '')
                    tar.setNomeTar(nomeDaTarefa)
                    tar.setPrazo(dataFdaTarefa)
                    tar.setStatus(statusDaTarefa)
                    self.listaTarefa.append(tar)
        
    def transformaListaDeObjEmArray(self):  
        for tar in self.listaTarefa:
            nomeTar = tar.getNomeTar()
            dataTar = tar.getPrazoAsData()
            status = tar.getStatus()
            self.nomesEDatasDasTarefas.append([nomeTar, dataTar, status])    
            
    def limpaArrayComDados(self):
        self.nomesEDatasDasTarefas.clear()
                
    def criaTarefa(self):
        tar = Tarefa()
        try:
            nome = input('Nome da tarefa: ')
            data = input('Data final(YYYY-MM-DD): ')
            tar.setNomeTar(nome)  
            tar.setPrazo(data)
        except ValueError:
            print('Você inseriu dados incorretamente')
            input('Tente novamente')
            return self.criaTarefa()    
        input('\nAperte qualquer tecla para voltar ao menu.')
        self.listaTarefa.append(tar)
        data = tar.getPrazoAsData()
        self.nomesEDatasDasTarefas.append([nome, data])
        funcao.limpaTela()

    def getIndexTarefa(self):
        indice = int(input('Digite o índice da tarefa.'))
        return indice
        
    def excluiTarefas(self):
        try:
            indice = self.getIndexTarefa()
            funcao.linhaCheia()
            print(f'Você excluiu a tarefa {self.listaTarefa[indice].getNomeTar()}')
            del(self.listaTarefa[indice])
            print('-'*50, '\n')    
            input('\nAperte qualquer tecla para voltar ao menu.')   
            funcao.limpaTela() 
        except IndexError:
            input('Você digitou um índice que não existe. Tente novamente.')
            return self.excluiTarefas() 
    
    def menuDaVisualizaçãoDeTarefas(self):
        escolha = input('\n \n1 - editar tarefa\n2 - Concluir Tarefa\n3 - Ordernar alfabeticamente\n4 - Ordenar por data\n5 - voltar ao menu \n')
        if escolha == '1':
            self.editaTarefas()
        if escolha == '2':
            self.concluiTarefa() 
        if escolha == '3':
            self.ordenaNomeDasTarefas()
        if escolha == '4':
            self.ordenaTarefaPorData()    
        if escolha == '5':
            return 
        
    def concluiTarefa(self):
        indiceTarefa = self.getIndexTarefa()
        input()
        tarefa = self.listaTarefa[indiceTarefa]
        tarefa.setStatus("True")
        self.limpaArrayComDados()
        self.transformaListaDeObjEmArray()
        return self.tabelaTarefas()
        
    def editaTarefas(self):
        try:
            selecionaTarefa = self.getIndexTarefa()
            tarefaEscolhida = self.listaTarefa[selecionaTarefa]
            funcao.linhaCheia()
            print(f'Nome: {tarefaEscolhida.getNomeTar()}')
            print(f'Data Final: {tarefaEscolhida.getPrazo()}')
            funcao.linhaCheia()
            novoNome = input('Digite o novo nome da tarefa.\n')
            tarefaEscolhida.setNomeTar(novoNome) 
            novaData = input('Digite a nova data final(YYYY-MM-DD)\n')
            tarefaEscolhida.setPrazo(novaData)
        except ValueError:
            print('Você inseriu dados incorretos.')
            input('Tente novamente')
            return self.editaTarefas()
        except IndexError:
            print('Você digitou um índice inexistente.')
            input('Tente novamente.')
            return self.editaTarefas()
            

    def ordenaNomeDasTarefas(self):
        alist = self.nomesEDatasDasTarefas
        print(alist)
        for numero in range(len(alist)-1, 0, -1):      
                 for linha in range(numero):
                    nomeAtual = alist[linha][0].lower()
                    proximoNome = alist[linha+1][0].lower()   
                    if nomeAtual > proximoNome:
                          alist[linha], alist[linha+1] = alist[linha+1], alist[linha]
        self.nomesEDatasDasTarefas = alist                  
        return self.tabelaTarefas()                
        

    def ordenaTarefaPorData(self):  
        alist = self.nomesEDatasDasTarefas
        print(alist)
        for numero in range(len(alist)-1, 0, -1):      
                 for linha in range(numero): 
                    if alist[linha][1] > alist[linha+1][1]:
                          alist[linha], alist[linha+1] = alist[linha+1], alist[linha]
        self.nomesEDatasDasTarefas = alist       
        return self.tabelaTarefas()                
        
           
    def tabelaTarefas(self):
        func.limpaTela()
        print(tabulate(self.nomesEDatasDasTarefas, headers=("Índice:","Nome:","Prazo:", "Status:"), tablefmt="fancy_grid", showindex="always"))        
        return self.menuDaVisualizaçãoDeTarefas()
    

    
   

   
    
    