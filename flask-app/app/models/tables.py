from app import db

class Cliente(db.Model):
    __tablename__= 'cliente'
    id = db.Collum(db.Integer,primery_key=True,unique=True)
    nome= db.Collum(db.String(20),unique=True)
    endereco= db.Collum(db.String(12))
    
    def __init__(self, nome,endereco):
        self.nome = nome
        self.endereco = endereco          
        

    def __repr__(self):
        return '<Cliente %r>' % self.nome

class User(db.Model):
    __tablename__= 'users'
    id = db.Collum(db.Integer,primery_key=True,unique=True)
    username= db.Collum(db.String(20),unique=True)
    senha= db.Collum(db.String(12))
    nome= db.Collum(db.String(20))

    def __init__(self, nome,username,senha):
        self.nome = nome
        self.username = username
        self.senha = senha           
        

    def __repr__(self):
        return '<User %r>' % self.username   
    
class Especialidade(db.Model):
    __tablename__= 'especialidades'
    id = db.Collum(db.Integer,primery_key=True,unique=True)
    nome= db.Collum(db.String(20),unique=True)
    
    def __init__(self, nome):
        self.nome = nome 

    def __repr__(self):
        return '<Especialidade %r>' % self.nome   

class Tecnico(db.Model):
    __tablename__= 'tecnicos'
    id = db.Collum(db.Integer,primery_key=True,unique=True)    
    userid = db.Collum(db.Integer, db.ForeignKey(User.id))
    especialidade = db.Collum(db.Integer, db.ForeignKey(Especialidade.id))
    
    def __init__(self, nome,endereco):
        self.nome = nome
        self.endereco = endereco          
        

    def __repr__(self):
        return '<Tecnico %r>' % self.nome
    
class Servico(db.Model):
    __tablename__= 'servicos'
    id = db.Collum(db.Integer,primery_key=True,unique=True)
    nome= db.Collum(db.String(20),unique=True)
    userid = db.Collum(db.Integer, db.ForeignKey(User.id))
    descricao = db.Collum(db.String(60))
    
    def __init__(self, nome,userid,descricao):
        self.nome = nome
        self.userid = userid
        self.descricao = descricao 

    def __repr__(self):
        return '<Servico: %r>' % self.nome
    
class Fotos(db.Model):
    __tablename__= 'fotos'
    id = db.Collum(db.Integer,primery_key=True,unique=True)
    nome= db.Collum(db.String(20),unique=True)
    servicoid = db.Collum(db.Integer, db.ForeignKey(Servico.id))
    descricao = db.Collum(db.String(60))
    
    def __init__(self, nome,servicoid,descricao):
        self.nome = nome
        self.servicoid = servicoid
        self.descricao = descricao 

    def __repr__(self):
        return '<Foto: %r>' % self.servicoid

class Videos(db.Model):
    __tablename__= 'videos'
    id = db.Collum(db.Integer,primery_key=True,unique=True)
    nome= db.Collum(db.String(20),unique=True)
    servicoid = db.Collum(db.Integer, db.ForeignKey(Servico.id))
    descricao = db.Collum(db.String(60))
    
    def __init__(self, nome,servicoid,descricao):
        self.nome = nome
        self.servicoid = servicoid
        self.descricao = descricao 

    def __repr__(self):
        return '<Video: %r>' % self.servicoid