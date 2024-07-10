class Torre:
    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def cadastrar(self):
        pass

    def imprimir(self):
        print(f"Torre ID: {self.id}, Nome: {self.nome}, Endereço: {self.endereco}")


class Apartamento:
    def __init__(self, id, numero, vaga, torre):
        self.id = id
        self.numero = numero
        self.vaga = vaga
        self.torre = torre
        self.proximo = None

    def cadastrar(self):
        pass

    def imprimir(self):
        print(f"Apartamento ID: {self.id}, Número: {self.numero}, Vaga: {self.vaga}, Torre: {self.torre.nome if self.torre else 'Nenhuma'}")


class FilaDeEspera:
    def __init__(self):
        self.fila = []

    def adicionar_apartamento(self, apartamento):
        self.fila.append(apartamento)

    def retirar_apartamento(self, vaga):
        if self.fila:
            apartamento = self.fila.pop(0)
            apartamento.vaga = vaga
            return apartamento
        else:
            return None

    def imprimir_fila(self):
        print("Fila de espera:")
        for apt in self.fila:
            apt.imprimir()


class ListaEncadeadaApartamentos:
    def __init__(self):
        self.head = None

    def adicionar_apartamento(self, apartamento):
        if self.head is None or apartamento.vaga < self.head.vaga:
            apartamento.proximo = self.head
            self.head = apartamento
        else:
            atual = self.head
            while atual.proximo is not None and atual.proximo.vaga < apartamento.vaga:
                atual = atual.proximo
            apartamento.proximo = atual.proximo
            atual.proximo = apartamento

    def liberar_vaga(self, vaga):
        atual = self.head
        anterior = None
        while atual is not None and atual.vaga != vaga:
            anterior = atual
            atual = atual.proximo
        if atual is not None:
            if anterior is None:
                self.head = atual.proximo
            else:
                anterior.proximo = atual.proximo
            return atual
        return None

    def imprimir_lista(self):
        print("Apartamentos com vaga:")
        atual = self.head
        while atual is not None:
            atual.imprimir()
            atual = atual.proximo


class Condominio:
    def __init__(self):
        self.torre = None
        self.lista_apartamentos = ListaEncadeadaApartamentos()
        self.fila_espera = FilaDeEspera()
        self.vagas_disponiveis = 10

    def cadastrar_torre(self, id, nome, endereco):
        self.torre = Torre(id, nome, endereco)

    def cadastrar_apartamento(self, id, numero, vaga=None):
        apartamento = Apartamento(id, numero, vaga, self.torre)
        if vaga is not None and self.vagas_disponiveis > 0:
            self.lista_apartamentos.adicionar_apartamento(apartamento)
            self.vagas_disponiveis -= 1
        else:
            self.fila_espera.adicionar_apartamento(apartamento)

    def liberar_vaga(self, vaga):
        apt = self.lista_apartamentos.liberar_vaga(vaga)
        if apt is not None:
            self.fila_espera.adicionar_apartamento(apt)
        apt_na_fila = self.fila_espera.retirar_apartamento(vaga)
        if apt_na_fila is not None:
            self.lista_apartamentos.adicionar_apartamento(apt_na_fila)

    def imprimir_lista_apartamentos(self):
        self.lista_apartamentos.imprimir_lista()

    def imprimir_fila_espera(self):
        self.fila_espera.imprimir_fila()

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Cadastrar Torre")
            print("2. Cadastrar Apartamento")
            print("3. Liberar Vaga")
            print("4. Imprimir Lista de Apartamentos com Vaga")
            print("5. Imprimir Fila de Espera")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                id = int(input("ID da Torre: "))
                nome = input("Nome da Torre: ")
                endereco = input("Endereço da Torre: ")
                self.cadastrar_torre(id, nome, endereco)
            elif opcao == "2":
                if self.torre is None:
                    print("Primeiro, cadastre a torre.")
                    continue
                id = int(input("ID do Apartamento: "))
                numero = input("Número do Apartamento: ")
                if self.vagas_disponiveis > 0:
                    vaga = int(input("Número da Vaga: "))
                    self.cadastrar_apartamento(id, numero, vaga)
                else:
                    print("Todas as vagas estão ocupadas. Apartamento será adicionado à fila de espera.")
                    self.cadastrar_apartamento(id, numero)
            elif opcao == "3":
                vaga = int(input("Número da Vaga a ser liberada: "))
                self.liberar_vaga(vaga)
            elif opcao == "4":
                self.imprimir_lista_apartamentos()
            elif opcao == "5":
                self.imprimir_fila_espera()
            elif opcao == "0":
                break
            else:
                print("Opção inválida. Tente novamente.")


condominio = Condominio()
condominio.cadastrar_torre(1, "Torre A", "Rua 1")

condominio.cadastrar_apartamento(1, "101", 1)
condominio.cadastrar_apartamento(2, "102", 2)
condominio.cadastrar_apartamento(3, "103", 3)
condominio.cadastrar_apartamento(4, "104", 4)
condominio.cadastrar_apartamento(5, "105", 5)
condominio.cadastrar_apartamento(6, "106", 6)
condominio.cadastrar_apartamento(7, "107", 7)
condominio.cadastrar_apartamento(8, "108", 8)
condominio.cadastrar_apartamento(9, "109", 9)
condominio.cadastrar_apartamento(10, "110", 10)

condominio.cadastrar_apartamento(11, "111")
condominio.cadastrar_apartamento(12, "112")

condominio.menu()





#Classes Principais:

#Torre: A torre do condomínio com atributos como ID, nome e endereço.
#Apartamento: O apartamento com atributos como ID, número, vaga de garagem e referência à torre.
#FilaDeEspera: Implementa uma fila para apartamentos que aguardam uma vaga de garagem.
#ListaEncadeadaApartamentos: Implementa uma lista encadeada para gerenciar os apartamentos que possuem vaga,
# ordenados pelo número da vaga.
#Condominio: Coordena o cadastro de torres e apartamentos, além de gerenciar a fila de espera
# e a lista de apartamentos com vaga.

#Funcionalidades:

#Cadastro de Torre e Apartamentos: Permite cadastrar uma única torre e vários apartamentos.
# Se não houver vagas disponíveis, os apartamentos são adicionados à fila de espera.

#Liberação de Vaga: Permite liberar uma vaga de garagem. O apartamento que estava na vaga
# é movido para o fim da fila de espera, e o próximo da fila é alocado na vaga liberada.

#Impressão de Listas: Permite imprimir a lista de apartamentos com vaga e a fila de espera.
#Menu Interativo:

#Oferece um menu que permite ao usuário escolher opções para cadastrar torre e apartamentos, liberar vagas, e imprimir listas.
