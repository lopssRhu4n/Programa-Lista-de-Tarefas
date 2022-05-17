from func import linhaCheia, limpaTela
class view:
        def start(self):
             return self.menu()   
        
        def menu (self):
                limpaTela()
                print('Menu:') 
                linhaCheia()
                print(f'{"1 - Criar nova tarefa":^50} \n{"2 - Visualizar tarefas":^50} \n{"3 - Excluir tarefa":^50} \n{"4 - Sair":^50}' )
                linhaCheia()
                escolha = input('Digite:')
                linhaCheia()
        
                linhaCheia()
                return escolha
