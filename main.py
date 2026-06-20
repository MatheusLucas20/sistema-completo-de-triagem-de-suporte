from time import sleep
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    print("--- Simulador de Triagem de Suporte ---")
    print("    [1] Problema com Internet")
    print("    [2] Computador Não Liga")
    print("    [3] Lentidão no Sistema")
    print("    [4] Sair")
        
def problema_internet():
    limpar_tela()
    print("Você escolheu [1] Problema com internet.\n")
    print("Você já tirou da tomada e aguardou 40s? ")

    opcao1 = input("Insira [S] Sim / [N] Não: ").lower()

    if opcao1 == 's':
        limpar_tela()
        print("Aguade um instante....")
        sleep(1)
        print("Dê uma olhada no seu roteador, verifique se ele está com luz vermelha piscando!")

        opcao_luz = input("\nInsira [S] Sim / [N] Não: ").lower()
        
        if opcao_luz == 's':
            limpar_tela()
            print("Isso indica uma instabilidade no sinal.")
            print("Nossa equipe já identificou a instabilidade na sua região")
            print("Já temos uma equipe a caminho para manutenção.\n")
        else:
            print("\nAguarde um instante, enquanto tentaremos retornar seu sinal...")
            sleep(2)
            print("Pronto; Seu sinal foi reestabelecido e voltou com força total.\n")

    elif opcao1 == 'n':
        limpar_tela()
        print("Instrução de Suporte:")
        print("Por Favor; Retire-o da tomada o seu roteador.")
        print("Aguarde 40 segundos, e insira na tomada novamente.")
        print("Se o problema persistir, reinicie o atendimento.\n")     

    else:
        print("\nOpção Invalida, Somente S/N!\n")
    
    input("Aperte Enter para o menu...")
    limpar_tela()

def computador_nao_liga():
    
    limpar_tela()
    print("Você escolheu [2] Computador Não Liga\n")
    
    print("Escolha [S] Sim / [N] Não")
    opcao = input("O computador acende alguma luz?  ").lower()
    
    if opcao == 's':
        limpar_tela()
        
        print("Escolha [S] Sim / [N] Não")
        situacao = input("O computador faz algum som/barulho? ").lower()
        
        if situacao == 's':
            limpar_tela()
            print("Diagnóstico: Bipes sequenciais ao ligar  geralmente indicam mau contato ou falha na mémoria RAM.")
            print("Carregando instruções; aguarde...\n")
            sleep(2)
            print("\nInstruções:\nSe você tiver conhecimento técnico, desligue o PC da tomada, abra a lateral.")
            print("Remova os pentes de memória e limpe os contatos dourados com uma borracha escolar branca e macia. Recoloque e teste novamente.")

        elif situacao == 'n':
            limpar_tela()
            print("Diagnóstico: O computador está processando, mas o sinal não chega à tela.")
            print("Carregando instruções; aguarde...\n")
            sleep(2)            
            print("Instruções:\nVerifique se o cabo de vídeo (HDMI, VGA ou DisplayPort).")
            print("Está conectado na saída correta (de preferência direto na placa de vídeo, se houver).")
            print("Certifique-se também de que o monitor está ligado na tomada e na entrada correta (Input Source).")        

    elif opcao == 'n':
        print("\nDiagnóstico: Falta de energia elétrica chegando aos componentes.")    
        print("Carregando instruções; aguarde...\n")
        sleep(2)
        print("Instruções:")
        print("Verifique se o cabo de força está bem firme na parte de trás do computador e na tomada.")
        print("Se estiver usando filtro de linha ou estabilizador, veja se ele está ligado.")
        print("Verifique se a chave liga/desliga atrás da fonte (botão I/O) está na posição 'I' (Ligado).")
    
    else:
        print("\nOpção Invalida! Digite somente [S]/[N]")
    
    input("\nAperte Enter para o menu...")
    limpar_tela()
  
def lentidao_sistema():
    limpar_tela()
    print("Você escolheu [3] Lentidão no Sistema.\n")
    
    print("Escolha uma Opção: [1] O tempo todo / [2] Só ao abrir muitos programas\n")
    opcao = input("A lentidão acontece o tempo todo (desde o momento em que liga o PC)\nou apenas quando você abre o navegador de internet e muitos programas ao mesmo tempo?: ")
    
    if opcao == '1':
        limpar_tela()
        print("Escolha uma Opção: [S] Sim, tem espaço / [N] Não tem espaço / Disco 100%: \n")
        situacao = input("O computador possui mais de 10% de espaço livre no armazenamento principal (Disco C:)?\nO uso de disco fica travado em 100%? ").lower()
        
        if situacao == 's':
            limpar_tela()
            print("Diagnóstico: Pode ser superaquecimento do processador ou thermal throttling.")
            print("Carregando instruções; aguarde...\n")
            sleep(2)
            print("Verifique se as saídas de ar do computador ou notebook não estão obstruídas por poeira.\nSe o computador tiver mais de 2 anos sem manutenção, pode ser necessário realizar uma\nlimpeza interna e a troca da pasta térmica do processador.\n")
                    
        elif situacao == 'n':
            limpar_tela()
            print("Diagnóstico: Armazenamento sobrecarregado ou gargalo de HD antigo.")
            print("Carregando instruções; aguarde...\n")
            sleep(2)
            print("Instruções:\n1. Desinstale programas que você não usa mais para liberar espaço.")
            print("2. Execute a ferramenta 'Limpeza de Disco' nativa do Windows.")
            print("3. Dica Tech: Se a máquina usa um HD tradicional, a melhor solução de hardware é fazer um upgrade para um SSD, o que deixa o computador até 10x mais rápido\n")
        
        else:
            print("\n❌ Opção Inválida! Digite apenas S ou N.")
            
    elif opcao == '2':
        limpar_tela()
        print("Diagnóstico: Consumo excessivo de Memória RAM ou processamento em segundo plano.")
        print("Carregando instruções; aguarde...\n")
        sleep(2)
        print("Instruções passo a passo na tela:\n")
        print("Pressione as teclas Ctrl + Shift + Esc para abrir o Gerenciador de Tarefas.")
        print("Vá até a aba 'Inicializar' (Startup) e desabilite programas desnecessários que ligam junto com o Windows (como Spotify, Discord, etc).")
        print("Feche as abas do navegador que não estiver utilizando (navegadores como o Chrome consomem muita memória RAM)\n")
        
    else:
        print("Opção Invalida!!!") 
    input("Aperte Enter para voltar ao menu...")
    limpar_tela()        
def chamado():
    while True:

        menu()
        opcao = input("Digite uma número: ")
        
        if opcao == '1':
            problema_internet()
        elif opcao == '2':
            computador_nao_liga()
        elif opcao == '3':
            lentidao_sistema()
        elif opcao == '4':
            limpar_tela()
            print("Suporte Encerrando...")
            print("Avalie nosso atendimento!")

            atendimento = input("Insira de [1 a 5], sendo 5 [muito bom]: ")

            if atendimento == '5':
                print("Agradecemos pela avaliação!")
            else:
                print("Agradecemos pela avaliação, iremos melhorar nosso atendimento!")
            break

def mostrar_dados():
    chamado()

if __name__ == "__main__":
    mostrar_dados()
