
from urllib import response
from flask import Flask, Response, request
from flask_restful import Resource, Api
from models import Colaboradores, Tarefas

app = Flask(__name__)
api = Api(app)

class CadastraColaborador(Resource):
    # Cadastra um novo colaborador
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

class VisuazilaColaborador(Resource):
    # Lista colaborador pelo nome
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

class ListaColaboradores(Resource):
    # Lista todos os colaboradores cadastrados no banco de dados
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

class AtualizaColaborador(Resource):
    # Atualiza dados de um colaborador já cadastrado no banco de dados
    def put(self, nome):
        dados = request.json
        colaborador = Colaboradores.query.filter_by(nome=nome).first()

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

class RemoveColaborador(Resource):    
    def delete(self, nome):
        colaborador = Colaboradores.query.filter_by(nome=nome).first()
        colaborador.delete()
        mensagem = f'Colaborador {colaborador.nome} excluido do banco de dados.'

        return {'status': 'Sucesso', 'messagem': mensagem}

class criatarefa(Resource):
    def post(self):
        dados = request.json
        tarefa = Tarefas(
            id = dados['id'],
            titulo_tarefa = dados['titulo_tarefa'],
            descricao = dados['descricao'],
            co_nome_fk = dados['co_nome_fk'],
            solicitante_da_demanda = dados['solicitante_da_demanda'],  
        )

        tarefa.save()

        response = {
            'id': tarefa.id,
            'titulo_tarefa': tarefa.titulo_tarefa,
            'descricao': tarefa.descricao,
            'co_nome_fk': tarefa.co_nome_fk,
            'solicitante_da_demanda': tarefa.solicitante_da_demanda
        }
        return response


class ListaTarefas(Resource):
    def get(self):
        tarefas = Tarefas.query.all()
        response = [{
            'id':i.id,
            'titulo_tarefa': i.titulo_tarefa,
            'descricao': i.descricao,
            'co_nome_fk': i.colaborador.co_nome_fk, 
            'solicitante_da_demanda': i.solicitante_da_demanda,
            }
            for i in tarefas
        ]
    
        return response

class AtualizaTarefa:
    def put(self,co_nome_fk ,titulo_tarefa):
        dados = request.json
        co_nome_fk = Tarefas.query.filter_by(co_nome_fk=co_nome_fk).first()
        tarefa = Tarefas.query.filter_by(titulo_tarefa=titulo_tarefa).first()

        if not tarefa:
            return Response("tarefa não encontrada", 404)        


        if "co_nome_fk" in dados:
            co_nome_fk.co_nome_fk = dados["co_nome_fk"]
        if  "titulo_tarefa" in dados:
            tarefa.titulo_tarefa = dados["titulo_tarefa"]
        if "descricao" in dados:
            tarefa.descricao = dados["descricao"]
        if "solicitante_da_demanda" in dados:
            tarefa.solicitante_da_demanda = dados["solicitante_da_demanda"]
               

        co_nome_fk.save()
        tarefa.save()

        response = {
            'id': tarefa.id,
            'titulo_tarefa': tarefa.titulo_tarefa,
            'descricao': tarefa.descricao,
            'co_nome_fk':tarefa.co_nome_fk,
            'solicitante_da_demanda': tarefa.solicitante_da_demanda
            }
        
        return response   


  


# def post(self): 
#         dados = request.json
#         colaborador = Colaboradores.query.filter_by(nome=dados['colaborador']).first()
#         tarefa = Tarefas(tarefa=dados['tarefa'], colaborador = colaborador)
#         tarefa.save()

#         response = {
#             'colaborador':tarefa.colaborador.nome,
#             'tarefa': tarefa.tarefa,
#             'id': tarefa.id
#         }

#         return response






api.add_resource(CadastraColaborador,'/cadastar-colaborador/')
api.add_resource(ListaColaboradores, '/lista-colaboradores/')
api.add_resource(AtualizaColaborador, '/atualiza-colaborador/<string:nome>/')
api.add_resource(VisuazilaColaborador, '/visuazila-colaborador/<string:nome>/')
api.add_resource(RemoveColaborador, '/remove-colaborador/')
api.add_resource(ListaTarefas, '/lista-tarefas/')



# api.add_resource(Colaborador, '/colaborador/<string:nome>/')
# api.add_resource(Tarefas, '/tarefas/')
# api.add_resource(Tarefa, '/tarefas/<tarefa>')
# api.add_resource(ColaboradorTarefa, '/tarefas/<colaborador>/<tarefa>')


if __name__ == '__main__':
    app.run(debug=True)
