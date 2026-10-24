import secrets
import string

def gerar_senha(tamanho=12, usar_maiusculas=True, usar_numeros=True, usar_simbolos=True):
    caracteres = string.ascii_lowercase
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    senha = ""

    for _ in range(tamanho):
        senha += secrets.choice(caracteres)
    return senha

if __name__ == "__main__":
    print (gerar_senha())
    print(gerar_senha(tamanho=20, usar_simbolos=False))