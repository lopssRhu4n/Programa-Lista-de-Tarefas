from funções import linhaCheia, limpaTela
from controler import Controler
control = Controler()
def menu ():
        limpaTela()
        print('Menu:') 
        linhaCheia()
        print(f'{"1 - Criar nova tarefa":^50} \n{"2 - Visualizar tarefas":^50} \n{"3 - Excluir tarefa":^50} \n{"4 - Sair":^50}' )
        linhaCheia()
        escolha = input('Digite: ')
        linhaCheia()
        if escolha == '4':
            return print(f'{"Obrigado por usar nosso programa!":^50}')
        if escolha == '1':
            control.criaTarefa()
        if escolha == '2':
            control.mostraTodasAsTarefas()
        if escolha == '3':
            control.excluiTarefas()        
        
        
        
        linhaCheia()
        menu()

limpaTela()
control.lerTarefas()
menu()
control.salvaDadosTar()
