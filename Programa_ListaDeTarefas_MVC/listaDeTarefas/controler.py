from classeTarefa import Tarefa
from view import view
import func
from model import model
funcao = func

class Controler:
    def __init__(self):
        self.view = view()
        self.model = model()
        self.model.lerTarefas()
        self.model.transformaListaDeObjEmArray()
    def start(self):
        escolha = self.view.menu()
        
        if escolha == '1':
            self.model.criaTarefa()
        if escolha == '2':
            self.model.tabelaTarefas()
        if escolha == '3':
            self.model.excluiTarefas()
        if escolha == '4':
            return self.finish()        
        return self.start()
    
    def finish(self):
        self.model.salvaDadosTar()
        print('Obrigado por usar nosso programa!')
        
            
a = Controler();
a.start()    
        
                