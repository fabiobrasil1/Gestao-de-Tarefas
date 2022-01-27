from models import Colaboradores

# Insere dados tabela colaboradores
def insere_colaboradores():
    colaborador = Colaboradores(nome='Fabio', idade=31, email= 'exemplo@exemplo.com', area_de_atuacao='beck-end', tipo_contratacao='SLT', cargo='Desenvolvedor Jr.')
    print([{
        'nome':colaborador.nome, 
        'idade':colaborador.idade,
        'email': colaborador.email,
        'area_de_atuacao': colaborador.area_de_atuacao,
        'tipo_de_contratacao': colaborador.tipo_contratacao,
        'cargo': colaborador.cargo
    }])
    colaborador.save()
    
#Lista todos os colaboradores cadastrados na tabela colaboradores
def consulta_colaboradores():
    colaboradores = Colaboradores.query.all()
    print(colaboradores)

# Realiza consulta dos dados do desenvolvedor na tabela colaboradores
def consulta_colaborador():
    colaborador = Colaboradores.query.filter_by(nome='Fabio').first()
    print([{'id':colaborador.id,
        'nome':colaborador.nome, 
        'idade':colaborador.idade,
        'area_de_atuacao': colaborador.area_de_atuacao,
        'tipo_de_contratacao': colaborador.tipo_contratacao,
        'cargo': colaborador.cargo
    }])

# Permite alterar dos dados do colaborador na tabela colaboirador
def atualiza_colaborador():
    colaborador = Colaboradores.query.filter_by(nome='Fabio').first()
    colaborador.nome = 'fabio'
    colaborador.idade = '31'
    colaborador.area_de_atuacao = 'backend'
    colaborador.tipo_contratacao = 'SLT'
    colaborador.cargo = 'Desenvolvedor Jr'
    
    print([{'id':colaborador.id,
        'nome':colaborador.nome, 
        'idade':colaborador.idade,
        'area_de_atuacao': colaborador.area_de_atuacao,
        'tipo_de_contratacao': colaborador.tipo_contratacao,
        'cargo': colaborador.cargo
    }])
    colaborador.save()

#Exclui o colaborador da tabela colaborador.
def excluir_colaborador():
    colaborador = Colaboradores.query.filter_by(nome='Fabio').first()
    colaborador.delete()

if __name__ == '__main__':
    # insere_colaboradores()
    # consulta_colaboradores()
    # consulta_colaborador()
    # atualiza_colaborador()
    # excluir_colaborador()