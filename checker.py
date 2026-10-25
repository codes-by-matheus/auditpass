import hashlib
import requests

def verificar_vazamento(senha):
    """
    Consulta a base de vazamentos do Have I Been Pwned usando o modelo k-Anonymity.
    Retorna a quantidade de vezes que a senha foi exposta em vazamentos públicos.
    """
    hash_completo = hashlib.sha1(senha.encode('utf-8')).hexdigest().upper()
    prefixo = hash_completo[:5]
    sufixo = hash_completo[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefixo}"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        raise RuntimeError("Falha ao consultar a API do Have I Been Pwned.")

    for linha in resposta.text.splitlines():
        hash_vazado, quantidade = linha.split(":")
        if hash_vazado == sufixo:
            return int(quantidade)

    return 0


if __name__ == "__main__":
    senha_digitada = input("Digite uma senha para testar: ")
    qtd_vazamentos = verificar_vazamento(senha_digitada)
    
    if qtd_vazamentos > 0:
        print(f"🚨 PERIGO! Essa senha já apareceu {qtd_vazamentos:,} vezes em vazamentos!")
    else:
        print("✅ SEGURA! Essa senha nunca foi encontrada em nenhum vazamento conhecido.")