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
    vazamentos_123456 = verificar_vazamento("123456")
    print(f"A senha '123456' vazou: {vazamentos_123456:,} vezes!")

    senha_segura = "M@th3us#AuditPass_2026_Ultra"
    vazamentos_segura = verificar_vazamento(senha_segura)
    print(f"A senha '{senha_segura}' vazou: {vazamentos_segura} vezes!")