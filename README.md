# 🛠️ Simulador de Triagem de Suporte Técnico (CLI)

Este é um projeto interativo em Python desenvolvido para simular o atendimento automático de primeiro nível (N1) em um help desk de TI. O programa guia o usuário por uma árvore de decisões lógica e interativa para diagnosticar e oferecer soluções práticas para os problemas mais comuns de suporte técnico.

O projeto une a minha bagagem prática em atendimento de TI e hardware com os conceitos de lógica de programação que estou aprendendo na faculdade.

---

## 🚀 Funcionalidades Práticas

O simulador cobre as três maiores demandas de um suporte de TI real:
* **[1] Problema com Internet:** Triagem de energia (modem/tomada) e diagnóstico de sinal físico através da análise das luzes do roteador.
* **[2] Computador Não Liga:** Análise detalhada de hardware (cabos de força, chave da fonte I/O, identificação de bipes de erro da Memória RAM e conexões de vídeo/monitor).
* **[3] Lentidão no Sistema:** Diagnóstico focado em software (gargalo de programas em segundo plano/inicialização) e hardware (gargalo de HD antigo vs upgrade para SSD, superaquecimento e thermal throttling).
* **Sistema de Avaliação:** Pesquisa de satisfação integrada com nota de 1 a 5 ao encerrar o suporte.

---

## 🧠 Conceitos de Engenharia de Software Aplicados

Como estudante de Engenharia de Software, fiz questão de estruturar o código seguindo boas práticas de desenvolvimento:

* **Modularização:** Divisão do código em funções independentes com responsabilidades únicas (`limpar_tela()`, `menu()`, `chamado()`, etc.), facilitando a leitura e manutenção.
* **Estruturas de Repetição Controladas (`while True`):** Loop contínuo para manter o sistema ativo, permitindo que o usuário navegue por múltiplos chamados sem que o programa feche sozinho.
* **Árvores de Decisão Aninhadas (`if/elif/else`):** Lógica complexa de tomada de decisões para guiar o usuário de forma precisa dependendo das respostas.
* **Blindagem do Código (Tratamento de Inputs):** Uso de `.lower()` para padronizar respostas de texto e leitura de opções de menu como strings, evitando que o programa sofra um *crash* (ValueError) caso o usuário digite uma letra por engano.
* **Preocupação com a Experiência do Usuário (UX):** Uso da biblioteca `os` para limpar o terminal dinamicamente e da biblioteca `time` (`sleep`) para simular o tempo de processamento dos testes técnicos, tornando a interface CLI mais limpa e intuitiva.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* Biblioteca nativa `os` (Manipulação e limpeza do terminal)
* Biblioteca nativa `time` (Controle de pausas e experiência de uso)

---

## 💻 Como Executar o Projeto

Para rodar o simulador na sua máquina, você só precisa ter o Python instalado.

1. Baixe o arquivo `main.py` deste repositório.
2. Abra o terminal (Prompt de Comando ou VS Code) na pasta onde salvou o arquivo.
3. Execute o comando:
   ```bash
   python main.py
