# controle_trem.py

class TremAutonomo:
    def __init__(self):
        self.posicao = 0
        self.movimentos_totais = 0
        self.movimentos_consecutivos = 0
        self.direcao_atual = None

    def mover(self, comandos):
        for comando in comandos:
            if comando not in ["ESQUERDA", "DIREITA"]:
                return "Erro: Comando inválido."

            if self.movimentos_totais >= 50:
                return f"Limite de movimentos atingido. Posição final: {self.posicao}"

            if comando == self.direcao_atual:
                self.movimentos_consecutivos += 1
            else:
                self.movimentos_consecutivos = 1
                self.direcao_atual = comando

            if self.movimentos_consecutivos > 20:
                return f"Erro: Mais de 20 movimentos consecutivos na mesma direção. Posição final: {self.posicao}"

            if comando == "DIREITA":
                self.posicao += 1
            elif comando == "ESQUERDA":
                self.posicao -= 1

            self.movimentos_totais += 1

        return f"Movimento concluído. Posição final: {self.posicao}"
