import string

def avaliar_forca(senha):
    pontos = 0
    feedback = []
    if len(senha) >= 8:
        pontos += 1
        if len(senha) >= 12:
            pontos += 1
        else:
            feedback.append("Recomendado: use 12 ou mais caracteres para segurança máxima.")
    else:
        feedback.append("A senha deve conter pelo menos 8 caracteres.")
    
    if any(c.isupper() for c in senha):
        pontos += 1
    else:
        feedback.append("A senha deve conter pelo menos uma letra maiúscula.")

    if any(c.islower() for c in senha):
        pontos += 1
    else:
        feedback.append("A senha deve conter pelo menos uma letra minúscula.")

    if any(c.isdigit() for c in senha):
        pontos += 1
    else:
        feedback.append("A senha deve conter pelo menos um número.")

    if any(c in string.punctuation for c in senha):
        pontos += 1
    else:
        feedback.append("A senha deve conter pelo menos um caractere especial.")

    nivel = ""

    if pontos <= 2:
        nivel = "Muito fraca"
    elif pontos == 3:
        nivel = "Fraca"
    elif pontos == 4:
        nivel = "Média"
    elif pontos == 5:
        nivel = "Forte"
    elif pontos == 6:
        nivel = "Excelente"

    return { "pontos": pontos, "nivel": nivel, "feedback": feedback }

if __name__ == "__main__":
    print("Teste 1 (Senha Fraca):", avaliar_forca("123"))
    print("Teste 2 (Senha Média):", avaliar_forca("senha123"))
    print("Teste 3 (Senha Top):", avaliar_forca("SenhaSuperForte!2024"))