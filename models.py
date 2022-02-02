import sqlalchemy as sa
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = sa.create_engine(r'sqlite:///colaboradores.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Tarefas(Base):
    __tablename__ = 'tb_tarefas'
    id = sa.Column(Integer, primary_key=True, autoincrement=True)
    titulo_tarefa = sa.Column(String(50))
    descricao = sa.Column(sa.String(50))
    co_nome_fk = sa.Column(sa.Integer, sa.ForeignKey("tb_colaboradores.id"))
    # co_nome_fk = sa.Column(sa.Integer, sa.ForeignKey("tb_colaboradores.id"))
    solicitante_da_demanda = sa.Column(String(50))
    # solicitante_da_demanda = sa.Column(Integer, sa.ForeignKey("tb_colaboradores.id"))

    def __repr__(self):
        # return f"<Tarefas(id = {self.id}, titulo_tarefa='{self.titulo_tarefa}'>)"
        return f"<Tarefas(nome = {self.co_nome_fk}, titulo_tarefa='{self.titulo_tarefa}'>)"

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Colaboradores(Base):
    __tablename__='tb_colaboradores'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome = sa.Column(sa.String(50), index=True)
    idade = sa.Column(sa.Integer)
    email = sa.Column(sa.String(40))
    area_de_atuacao = sa.Column(String(10))
    tipo_contratacao = sa.Column(String(10))
    cargo = sa.Column(sa.String(50))
    cria_tarefa = relationship(
        Tarefas,
        primaryjoin= "Colaborador.nome == Tarefas.co_nome_fk",
        backref= "Tarefas_criadas_pelo_colaborador"
        
    )
    # tarefas_atribuidas = relationship(
    #     Tarefas,
    #     primaryjoin= "Colaborador.id == Tarefas.solicitante_da_demanda",
    #     backref= "Tarefas_atribuidas_pelos_colaborador",
    # )

    def __repr__(self):
        return f"<Colaboradores(id={self.id}, nome='{self.nome}')>"

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()
    

def init_bd():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_bd()
