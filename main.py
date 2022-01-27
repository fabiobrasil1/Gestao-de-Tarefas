from flask import Flask, request
from flask_restful import Resource, Api
from models import Colaboradores, Tarefas

app = Flask(__name__)
api = Api(app)

class Colaborador(Resource):
    def get(self,nome):
        colaborador = Colaboradores.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome':colaborador.nome, 
                'idade':colaborador.idade,
                'email': colaborador.email,
                'area_de_atuacao': colaborador.area_de_atuacao,
                'tipo_de_contratacao': colaborador.tipo_contratacao,
                'cargo': colaborador.cargo
            }
        except AttributeError:
            response = {
                'status': 'erro',
                'message': 'Colaborador não Encontrado'
            }

        return response

    def put(self, nome):
        colaborador = Colaboradores.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            colaborador.nome = dados['nome']
        if 'idade' in dados:
            colaborador.idade = dados['idade']
        if 'email' in dados:
            colaborador.email = dados['email']
        if 'area_de_atuacao' in dados:
            colaborador.area_de_atuacao = dados['area_de_atuacao']
        if 'tipo_contratacao' in dados:
            colaborador.tipo_contratacao = dados['tipo_contratacao']
        if 'cargo' in dados:
            colaborador.cargo = dados['cargo']
            
        colaborador.save()

        response = {'nome': colaborador.nome, 
            'idade': colaborador.idade,
            'email': colaborador.email,
            'area_de_atuacao': colaborador.area_de_atuacao,
            'tipo_contratacao': colaborador.tipo_contratacao,
            'cargo': colaborador.cargo
        }

        return response 
    
    def delete(self, nome):
        colaborador = Colaboradores.query.filter_by(nome=nome).first()
        colaborador.delete()
        mensagem = f'Colaborador {colaborador.nome} excluido do banco de dados.'

        return {'status': 'Sucesso', 'messagem': mensagem}
    
class ListaColaboradores(Resource):
    def get(self):
        colaboradores = Colaboradores.query.all()
        response = [{
            'id': i.id,
            'nome':i.nome,
            'idade':i.idade,
            'email': i.email,
            'area_de_atuacao':i.area_de_atuacao,
            'tipo_contratacao': i.tipo_contratacao,
            'cargo': i.cargo
        }  for i in colaboradores]
        
        return response
    
    def post(self):
        dados = request.json
        colaborador = Colaboradores(
            nome=dados['nome'], 
            idade=dados['idade'],
            email=dados['email'],
            area_de_atuacao=dados['area_de_atuacao'],
            tipo_contratacao=dados['tipo_contratacao'],
            cargo=dados['cargo']
        )

        colaborador.save()

        response = {
            'id': colaborador.id,
            'nome': colaborador.nome,
            'idade': colaborador.idade,
            'email': colaborador.email,
            'area_de_atuacao': colaborador.area_de_atuacao,
            'tipo_contratacao': colaborador.tipo_contratacao,
            'cargo': colaborador.cargo
        }

        return response

class ListaTarefas(Resource):
    def get(self):
        tarefas = Tarefas.query.all()
        response = [{
            'id':i.id, 
            'tarefa': i.tarefa, 
            'colaborador': i.colaborador.nome} 
            for i in tarefas]
    
        return response

    def post(self): 
        dados = request.json
        colaborador = Colaboradores.query.filter_by(nome=dados['colaborador']).first()
        tarefa = Tarefas(tarefa=dados['tarefa'], colaborador = colaborador)
        tarefa.save()

        response = {
            'colaborador':tarefa.colaborador.nome,
            'tarefa': tarefa.tarefa,
            'id': tarefa.id
        }

        return response

api.add_resource(Colaborador, '/colaborador/<string:nome>/')
api.add_resource(ListaColaboradores, '/lista_colaboradores/')
api.add_resource(ListaTarefas, '/lista_tarefas/')

if __name__ == '__main__':
    app.run(debug=True)
