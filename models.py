from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(r'sqlite:///colaboradores.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Colaboradores(Base):
    __tablename__='colaboradores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)
    email = Column(String(40))
    area_de_atuacao = Column(String(10))
    tipo_contratacao = Column(String(10))
    cargo = Column(String(50))


    def __repr__(self):
        return f'<Colaboradores {self.nome}>'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()
    
class Tarefas(Base):
    __tablename__ = 'tarefas'
    id = Column(Integer, primary_key=True)
    tarefa = Column(String(50))
    colaborador_id = Column(Integer, ForeignKey('colaboradores.id'))
    colaborador = relationship("Colaboradores")

    def __repr__(self):
        return f'<Tarefas {self.tarefa}>'

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
