from Dao import *

dao = DAO("Tarefa.txt")

class ToDo():    

    def AdicionarTarefa(self, tarefa):
        dao.adicionar_tarefa(tarefa) 
        return True

    def ExcluirTarefa(self, excluir):
        if excluir >= 0 and excluir < len(self.lista):
            tarefa_removida = self.lista.pop(excluir)
            dao.listar_tarefa(self.lista) 
            return tarefa_removida
        else:
            return None


    def ListarTarefas(self): 
        with open('tarefa.txt', 'r') as arquivo:
            tarefas = arquivo.readlines()
    
        tarefas = [tarefa.strip() for tarefa in tarefas]

        return tarefas
        

TODO = ToDo()