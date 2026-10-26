import streamlit as st
from generator import gerar_senha
from validator import avaliar_forca
from checker import verificar_vazamento

st.set_page_config(page_title = "AuditPass — Segurança de Senhas", page_icon = "🔒", layout = "wide")
st.title("🛡️ AuditPass — Central de Segurança de Senhas")
st.markdown("Verifique vazamentos na internet, meça a força e gere senhas seguras.")
st.divider()

aba_auditoria, aba_gerador = st.tabs(["🔍 Auditar Senha", "⚡ Gerador de Senhas"])

with aba_auditoria:
    st.subheader("🔍 Auditar Senha")

    with st.form("form_auditoria"):
        caixa_senha = st.text_input(("Digite sua senha: "), type = "password")
        click_button = st.form_submit_button("Verificar", type="primary")

    if click_button and caixa_senha:
        vazamentos = verificar_vazamento(caixa_senha)
        analise = avaliar_forca(caixa_senha)
        if vazamentos > 0:
            st.error(f"🚨 PERIGO! Essa senha já apareceu {vazamentos:,} vezes em vazamentos!")
        else:
            st.success("✅ SEGURA! Essa senha nunca foi encontrada em nenhum vazamento conhecido.")
        st.metric("Nível de Força", analise["nivel"], f"{analise['pontos']}/6 pontos")
        for dica in analise["feedback"]:
            st.warning(dica)
            
with aba_gerador: 
    st.subheader("⚡ Gerador de Senhas")
    
    tamanho_escolhido = st.slider("Comprimento da Senha", 8, 32, 16)
    com_maiusculas = st.checkbox("Letra Maiúscula", value=True)
    com_numeros = st.checkbox("Números", value=True)
    com_simbolos = st.checkbox("Símbolos", value=True)

    botao_gerar = st.button("Gerar Senha Segura", type="primary")
    if botao_gerar:
        senha_gerada = gerar_senha(tamanho=tamanho_escolhido, usar_maiusculas=com_maiusculas, usar_numeros=com_numeros, usar_simbolos=com_simbolos)
        st.code(senha_gerada)
        st.success("Senha gerada com sucesso!")