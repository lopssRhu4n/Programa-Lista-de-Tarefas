from datetime import date
from operator import indexOf
from classeTarefa import Tarefa
import func

funcao = func
class model:
    def __init__(self):
        self.listaTarefa = []
        self.nomesEDatasDasTarefas =[]
            
    def criaTarefa(self):
        tar = Tarefa()
        nome = (input('Nome da tarefa: '))
        data = input('Data final(YYYY-MM-DD): ')
        tar.setNomeTar(nome)  
        tar.setPrazo(data)
        input('\nAperte qualquer tecla para voltar ao menu.')
        self.listaTarefa.append(tar)
        funcao.limpaTela()
        
    def excluiTarefas(self):
        indice = int(input('Qual tarefa você deseja excluir? \n'))
        funcao.linhaCheia()
        print(f'Você excluiu a tarefa {self.listaTarefa[indice].getNomeTar()}')
        del(self.listaTarefa[indice])
        print('-'*50, '\n')    
        input('\nAperte qualquer tecla para voltar ao menu.')   
        funcao.limpaTela() 
 
           
    def salvaDadosTar(self):
        with open('arquivo_listas.txt', 'w') as arquivo:           
            for tar in self.listaTarefa:    
                arquivo.write(tar.getNomeTar() + ';')
                arquivo.write(tar.getPrazo() + '\n')
    
    def lerTarefas(self):   
        with open('arquivo_listas.txt', 'r') as arquivo:
            dadosDasTarefas = arquivo.readlines()
            for linha in dadosDasTarefas:  
                if linha != '\n':
                    tar = Tarefa()
                    linha = linha.split(';')
                    nomeDaTarefa = linha[0]
                    dataFdaTarefa = linha[1].replace('\n','')
                    tar.setNomeTar(nomeDaTarefa)
                    tar.setPrazo(dataFdaTarefa)
                    self.listaTarefa.append(tar)
        
    
    def mostraTodasAsTarefas(self):
        funcao.limpaTela()    
        print(f'{"Índice:":<0}{"Nome:":>27}')
        for tar in self.listaTarefa:
            print(f'{self.listaTarefa.index(tar)}  {"-"*25} {tar.getNomeTar()}')
        return self.menuDaVisualizaçãoDeTarefas() 
    
    def menuDaVisualizaçãoDeTarefas(self):
        escolha = input('\n \n1 - editar tarefa\n2 - Ordernar alfabeticamente\n3 - Ordenar por data\n4 - voltar ao menu \n')
        if escolha == '1':
            self.editaTarefas()
        if escolha == '2':
            self.ordenaTarefaAlfabeticamente()
        if escolha == '3':
            self.ordenaTarefaPorData()    
        if escolha == '4':
            return 
        
    def editaTarefas(self):
    
            selecionaTarefa = int(input('Digite o índice da tarefa.\n'))
            tarefaEscolhida = self.listaTarefa[selecionaTarefa]
            funcao.linhaCheia()
            print(f'Nome: {tarefaEscolhida.getNomeTar()}')
            print(f'Data Final: {tarefaEscolhida.getPrazo()}')
            funcao.linhaCheia()
            novoNome = input('Digite o novo nome da tarefa.\n')
            tarefaEscolhida.setNomeTar(novoNome) 
            novaData = input('Digite a nova data final(YYYY-MM-DD)\n')
            tarefaEscolhida.setPrazo(novaData)

    def ordenaTarefaPorData(self):
        dataAnterior = date.max
        for tar in self.listaTarefa:
            dataAtual = tar.getPrazoAsData()
            if dataAtual < dataAnterior:
                self.listaTarefa.remove(tar)
                self.listaTarefa.insert(0, tar)
            dataAnterior = dataAtual
        return self.mostraTodasAsTarefas()
               
    def ordenaTarefaAlfabeticamente(self):
        nomeAnterior = 'zzzzzzzzzzzzzzzzzzzzz'
        for tar in self.listaTarefa:
            nomeAtual = tar.getNomeTar()
            if nomeAtual < nomeAnterior:
                self.listaTarefa.remove(tar)
                self.listaTarefa.insert(0, tar)
                for i in self.listaTarefa:
                    print(i.getNomeTar())    
            nomeAnterior = nomeAtual
        input()    
        return self.mostraTodasAsTarefas()
            
        
        
#Função para imprimir em formato de tabela        
    # def tabelaTarefas(self):
    #     funcao.limpaTela()
    #     print(self.listaTarefa)
    #     print('Array com as tarefas do programa ^')
    #     for cadaTarefa in self.listaTarefa:
    #         nomeDaTarefa = cadaTarefa.getNomeTar()
    #         prazoDaTarefa = cadaTarefa.getDataF()
    #         d = []
    #         d.append((nomeDaTarefa,prazoDaTarefa))
    
    #     print(d, 'array criado na função')
    #     #print(tabulate(d, headers=("Nome:","Prazo:"), tablefmt="fancy_grid"))
    #     input('Pressione qualquer tecla para voltar ao menu.')
    