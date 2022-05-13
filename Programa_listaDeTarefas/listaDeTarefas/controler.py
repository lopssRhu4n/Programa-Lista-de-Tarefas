from classTarefa import Tarefa

import funções
funcao = funções
class Controler:
    def __init__(self):
        self.listaTarefa = []
            
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
        funções.limpaTela()    
        print(f'{"Índice:":<0}{"Nome:":>27}')
        for tar in self.listaTarefa:
            print(f'{self.listaTarefa.index(tar)}  {"-"*25} {tar.getNomeTar()}')
    
        escolha = input('\n \n1 - editar tarefa\n2 - Ordernar alfabeticamente\n3 - Ordenar por data\n')
        if escolha == '1':
            self.editaTarefas()    
        
        input('Aperte qualquer tecla para voltar ao menu.')        
    
    def editaTarefas(self):
    
            selecionaTarefa = int(input('Digite o índice da tarefa.\n'))
            tarefaEscolhida = self.listaTarefa[selecionaTarefa]
            funcao.linhaCheia()
            print(f'Nome: {tarefaEscolhida.getNomeTar()}')
            print(f'Data Final: {tarefaEscolhida.getDataF()}')
            funcao.linhaCheia()
            novoNome = input('Digite o novo nome da tarefa.\n')
            tarefaEscolhida.setNomeTar(novoNome) 
            novaData = input('Digite a nova data final(YYYY-MM-DD)\n')
            tarefaEscolhida.setPrazo(novaData)

    def ordenaTarefaPorData(self):
        for tar in self.listaTarefa:
            dataAtual = tar.get
        
        print()    
#Função para imprimir em formato de tabela        
    def tabelaTarefas(self):
        funcao.limpaTela()
        print(self.listaTarefa)
        print('Array com as tarefas do programa ^')
        for cadaTarefa in self.listaTarefa:
            nomeDaTarefa = cadaTarefa.getNomeTar()
            prazoDaTarefa = cadaTarefa.getDataF()
            d = []
            d.append(([nomeDaTarefa,prazoDaTarefa]))
    
        print(d, 'array criado na função')
        #print(tabulate(d, headers=("Nome:","Prazo:"), tablefmt="fancy_grid"))
        input('Pressione qualquer tecla para voltar ao menu.')
       