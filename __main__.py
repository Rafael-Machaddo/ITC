class AFND:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais

    def executar(self, cadeia):
        estados_atuais = set([self.estado_inicial])

        for simbolo in cadeia:
            estados_proximos = set()

            for estado in estados_atuais:
                if (estado, simbolo) in self.transicoes:
                    estados_proximos.update(self.transicoes[(estado, simbolo)])

            estados_atuais = estados_proximos

        return any(estado in self.estados_finais for estado in estados_atuais)


if __name__ == '__main__':
    estados = {'q0', 'q1', 'q2'}
    alfabeto = {'0', '1'}
    transicoes = {
        ('q0', '0'): {'q0'},
        ('q0', '1'): {'q0', 'q1'},
        ('q1', '0'): {'q2'}
    }
    estado_inicial = 'q0'
    estados_finais = {'q2'}

    afnd = AFND(estados, alfabeto, transicoes, estado_inicial, estados_finais)

    cadeias = ['010', '011', '10', '11']

    for cadeia in cadeias:
        if afnd.executar(cadeia):
            print(f"A cadeia '{cadeia}' é ACEITA pelo AFND.")
        else:
            print(f"A cadeia '{cadeia}' é RECUSADA pelo AFND.")
