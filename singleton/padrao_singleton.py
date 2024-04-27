# O Singleton proporciona uma forma de ter um, somente um, objeto
# de determinado tipo, além de um ponto de acesso global à este objeto.

### ? ONDE USAR O SINGLETON ? ###
# -> Logging (logs) ou operações de bancos de dados;
# -> Spoolers de impressões;
# E muitos outros cenários em que seja necessário que haja apenas uma única instância
# de determinado objeto disponível para toda aplicação.
# OBS: Isso para evitar requisições conflitantes para o mesmo recurso.

class Singleton(object):

    def __new__(cls): #Criação de um novo objeto

        if not hasattr(cls, 'instance'): #Verificando se há um atributo instance no objeto da classe.

            cls.instance = super(Singleton, cls).__new__(cls) #Criando a instância no objeto de classe.
            print(f'Criando o objeto {cls.instance}')

        return cls.instance

s1 = Singleton()
print(f"Instância 1: {id(s1)}")

s2 = Singleton()
print(f"Instância 2: {id(s2)}")