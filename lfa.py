class RegularGrammar:
    def __init__(self, terminals, non_terminals, productions, start_symbol):
        self.terminals = terminals
        self.non_terminals = non_terminals
        self.productions = productions
        self.start_symbol = start_symbol

    def generate_fa(self):
        fa = FiniteAutomaton()

        # Adiciona estados ao FA
        for non_terminal in self.non_terminals:
            fa.add_state(non_terminal)

        # Adiciona transições ao FA com base nas produções
        for production in self.productions:
            fa.add_transition(production['from'], production['to'], production['symbol'])

       # Define os estados inicial e final
        fa.set_start_state(self.start_symbol)
        fa.add_final_state(self.start_symbol)  # Supondo que o símbolo inicial também seja um estado final

        return fa


class FiniteAutomaton:
    def __init__(self):
        self.states = []
        self.transitions = []
        self.start_state = None
        self.final_states = []

    def add_state(self, state):
           # Adiciona um estado
        self.states.append(state)

    def add_transition(self, from_state, to_state, symbol):
         # Adiciona uma transição
        self.transitions.append({'from': from_state, 'to': to_state, 'symbol': symbol})

    def set_start_state(self, start_state):
        # Define o estado inicial
        self.start_state = start_state

    def add_final_state(self, final_state):
        # Adiciona um estado final
        self.final_states.append(final_state)

    def is_valid_string(self, input_string):
        current_state = self.start_state

        for symbol in input_string:
            valid_transition = False
            for transition in self.transitions:
                if transition['from'] == current_state and transition['symbol'] == symbol:
                    current_state = transition['to']
                    valid_transition = True
                    break

            if not valid_transition:
                return False  # Transição inválida para o símbolo atual

        return current_state in self.final_states


# Solicita ao usuário que insira os terminais, separados por vírgulas
rg_terminals = input("Insira os terminais, separados por vírgulas: ").split(',')

# Solicita ao usuário que insira os não-terminais, separados por vírgulas
rg_non_terminals = input("Insira os não-terminais, separados por vírgulas: ").split(',')

# Solicita ao usuário que insira as produções
print("Insira as produções no formato 'de,para,símbolo', uma por linha. Digite 'fim' para terminar.")
rg_productions = []
while True:
    production = input()
    if production.lower() == 'fim':
        break
    from_state, to_state, symbol = production.split(',')
    rg_productions.append({'from': from_state, 'to': to_state, 'symbol': symbol})

# Solicita ao usuário que insira o símbolo inicial
rg_start_symbol = input("Insira o símbolo inicial: ")

rg = RegularGrammar(rg_terminals, rg_non_terminals, rg_productions, rg_start_symbol)

# Gera Autômato Finito a partir da Gramática Regular
fa = rg.generate_fa()

# Solicita ao usuário que insira as strings de teste
print("Insira as strings de teste, uma por linha. Digite 'fim' para terminar.")
test_strings = []
while True:
    test_string = input()
    if test_string.lower() == 'fim':
        break
    test_strings.append(test_string)

# Verifica se as strings são válidas para a linguagem regular
for string in test_strings:
    is_valid = fa.is_valid_string(string)
    print(f"A string '{string}' é {'válida' if is_valid else 'inválida'} para a linguagem regular.")
