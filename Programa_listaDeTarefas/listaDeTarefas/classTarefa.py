from datetime import date
class Tarefa:
    def __init__(self):
        self.nomeTar = 'nomeTar'
        self.prazo = 'dataF'
        self.concluida = False
    
    def getNomeTar(self):
        return self.nomeTar
    
    def setNomeTar(self, nome):
        self.nomeTar = nome        
    
    def getPrazo(self):
        data =date.isoformat(self.prazo)
        return data
    
    def getPrazoAsData(self):
        return self.prazo
    
    def setPrazo(self, data):
        data = date.fromisoformat(data)        
        self.prazo = data
        
    def getConcluida(self):
        return self.concluida    
    
    def setConcluida(self, conclusao):
        self.concluida = conclusao