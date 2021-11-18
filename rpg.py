import time
print ('Olá, você acabou de acordar em uma cadeia de segurança máxima no Rio de Janeiro.')
time.sleep(3)
print ('Você tem que fugir a qualquer custo dessa cadeia, pois pelo mesmo motivo que você foi parar aí, tem pessoas que querem seu fim..')
time.sleep(7)
print ('Você tem 3 opções de personagem para fugir...')
time.sleep(4)
print ('1 = Cláudio')
print ('2 = Damélio')
print ('3 = Paulo')
time.sleep(4)
escolhadopersonagem = float(input('Digite o número do personagem escolhido:'))
time.sleep(2)

if escolhadopersonagem == 1:
    print ('Você escolheu Cláudio')
    time.sleep(3)
    print ('Cláudio é um jovem forte porém não tem muitos conhecimentos, ele não age pensando nas suas consequências, porém sua força o ajuda.')
    time.sleep(6)
    print('A seguir você terá duas opções para fuga:')
    time.sleep(4)
    print ('Opção 1 com sua força você consegue entortar as barras da cela para iniciar a fuga.')
    time.sleep(4)
    print ('ou')
    time.sleep(2)
    print ('Opção 2 você começa a cavar um buraco para a cela vazia ao lado, já que celas vazias ficam abertas de noite.')
    time.sleep(5)
    escolhadafuga = float(input('De qual jeito você pretende continuar? Digite o número da opção:'))
    time.sleep(2)

    if escolhadafuga == 1:
        print ('Você escolheu a opção 1')
        time.sleep(2)
        print ('Cláudio então começa a fazer força para conseguir entortar as barras da cela...')
        time.sleep(5)
        print ('Infelizmente você desmaia e bate a cabeça, gerando um traumatismo craniano e vindo à falência. Então a caminho do céu você lembra que não é nenhum super herói e que não deveria ter feito isso')
        time.sleep(9)
        print ('É... Game over pra você...')

    if escolhadafuga == 2:
        print ('Você escolheu a opção 2')
        time.sleep(4)
        print('Você começa então a cavar e depois de algum tempo consegue chegar a cela vazia. E por sorte a porta da cela está aberta e com acesso ao pátio de detentos, você vai para o pátio...')
        time.sleep(12)
        print ('A seguir ouve passos no pátio, deve ser algum dos guardas do plantão da noite. Você então pode tomar duas decisões:')
        time.sleep(6)
        print ('Decisão 1 é se esconder e esperar o guarda passar para acertar a cabeça dele com um soco bem dado')
        time.sleep(5)
        print ('ou')
        time.sleep(2)
        print ('Decisão 2 é se esconder e esperar o guarda passar, e quando ele estiver longe você volta a correr pelo pátio em direção à saída')
        time.sleep(6)
        escolhadoataque = float(input('Oque você pretende fazer? Digite o número da opção:'))
        time.sleep(2)

        if escolhadoataque == 1:
            print ('Você escolheu a opção 1')
            time.sleep(2)
            print ('Então você espera o guarda passar e o ataca com um golpe certeiro na cabeça, porém você não esperava que havia mais um guarda com ele... Infelizmente você leva 3 tiros e vai para o beleléu...')
            time.sleep(10)
            print ('Game over colega...')

        if escolhadoataque == 2: 
            print ('Você escolheu a opção 2')
            time.sleep(2)
            print('Por sorte você vê que eram dois guardas e conseguiu passar por eles sem levantar suspeitas. Então vê a porta da sala de armamentos aberta e decide ir ate lá para pegar algo que possa usar para se defender.')
            time.sleep(11)
            print (' Chegando lá você se depara com as seguintes coisas:')
            time.sleep(4)
            print ('Objeto 1, uma banana')
            print ('Objeto 2, um fuzil')
            time.sleep(6)
            armaescolhida = float(input('Qual objeto você pretende usar? Digite o número do objeto:'))

            if armaescolhida ==1:
                print('Você escolheu uma banana mesmo??? tem certeza???')
                time.sleep(4)
                print ('Depois de pegar a banana você sai correndo em direção a porta de saída')
                time.sleep(6)
                print ('Você se depara com um guarda armado que está apontando um fuzil pra você')
                time.sleep(5)
                print ('Então você pega a banana e a descasca, joga a casca no pé dele e ele escorrega, você pega o fuzil dele e sai correndo da cadeia.')
                time.sleep(10)
                print ('Parabéns você conseguiu fugir da prisão!!!!!!!!!!!!!!!!!!!!!!!!!')

            if armaescolhida == 2:
                print ('Você escolheu o fuzil, agora não tem como dar errado né??')
                time.sleep(5)
                print ('Você se depara com um guarda armado que está apontando um fuzil pra você')
                time.sleep(6)
                print ('Então você pega o fuzil e mira pra ele, o guarda da risada da sua cara e você fica sem entender. Tenta disparar porém aquele fuzil estava sem  o pente com balas, o guarda atira em você...')
                time.sleep(12)
                print ('Game over... Perdeu playboy...')










if escolhadopersonagem == 2: 
    print ('Você escolheu Damélio')
    time.sleep(3)
    print ('Damélio é um senhor sábio, sempre pensa bem antes de agir ou de tomar qualquer decisão, porém pela sua idade não tem a mesma força e o mesmo condicionamento de um jovem.')
    time.sleep(5)
    print ('Você tem 2 escolhas para iniciar a fuga')
    time.sleep(3)
    print ('Opção número 1: Chamar seu irmão gêmeo para uma visita e trocar de lugar com ele, para ser livre novamente')
    time.sleep(4)
    print ('Ou')
    time.sleep(2)
    print ('Opção número 2: Fingir que está doente e pedir uma solicitação para ir para enfermaria ')
    time.sleep(4)
    escolhadafuga = float(input('De qual jeito você pretende continuar? Digite o número da opção:'))
    time.sleep(2)

    if escolhadafuga == 1:
        print ('Você escolheu a opção 1')
        time.sleep(2)
        print ('Você então marca a visita para seu irmão gêmeo vir...')
        time.sleep(4)
        print ('Chegando lá, ele se depara com seu irmão. Seu plano entra em ação, eles trocam de roupa sem ninguém perceber.')
        time.sleep(6)
        print ('Quase perto da porta da saída dois guardas o aborda e diz que precisa colocar a digital para autentificar a saída do mesmo.')
        time.sleep(7)
        print ('Então descobrem que ele estava tentando fugir da cadeia. Além de apanhar ele teve sua pena aumentada em 10 anos pela tentativa de fuga... Game Over.')
        time.sleep(8)

    if escolhadafuga == 2:
        print ('Você escolheu a opção 2')
        time.sleep(2)
        print ('Então você finge um desmaio e seu companheiro de cela chama os guardas... ')
        time.sleep(4)
        print ('Os guardas então o levam na enfermaria da prisão na qual, você conhecia o médico e havia subornado para fazer oque ele pedisse')
        time.sleep(6)
        print ('Então você tem dois planos para fuga:')
        time.sleep(3)
        print ('Plano 1: pedir para o médico gerar uma certidão de óbito e consequentemente você ser encaminhado para o necrotério')
        time.sleep(5)
        print ('ou')
        time.sleep(2)
        print ('Plano 2: falar para o médico colocar você em um saco de lixo para sair junto com o resto do lixo da cadeia, assim sendo livre novamente. ')
        time.sleep(6)
        escolhadoplano = float(input('Digite o número do plano escolhido para continuar:'))
        time.sleep(2)

        if escolhadoplano == 1:
            print ('Você escolheu o plano 1')
            time.sleep(2)
            print ('Então o médico faz oque você pediu e aciona a sollicitação para o necrotério. Lá fora ao invés da van que era pra ir retirar "seu corpo", está outra van que você contratou...')
            time.sleep(6)
            print ('Assim você acaba saindo da cadeia, mas você não contava que um guarda iria acompanhar o trajeto')
            time.sleep(5)
            print (' Você tem duas opções:')
            time.sleep(2)
            print ('Opção 1: Dar um susto no guarda pra ver se ele desmaia')
            time.sleep(3)
            print ('ou')
            time.sleep(2)
            print ('Opção 2: esperar até que chegue no lugar que você tinha combinado com o motorista e esperar até que ele mate o guarda que veio junto')
            escolhadoproblema = float(input('Digite o número da opção escolhida'))
            time.sleep(2)

            if escolhadoproblema == 1:
                print ('Você escolheu a opção 1')
                time.sleep(2)
                print ('O guarda se assusta, mas não o sulficiente para desmaiar e te da um tiro no meio da cara... Game Over.')
                time.sleep(3)

            if escolhadoproblema == 2:
                print ('Você escolheu a opção 2')
                time.sleep(2)
                print ('Então você espera e chegando no destino o motorista que você contratou da um fim no guarda quando ele estava destraído. É isso aí, você venceu e conseguiu escapar.')

        if escolhadoplano == 2:
            print ('Você escolheu o plano 2')
            time.sleep(2)
            print ('Então você sai da cadeia num saco de lixo, porém o caminhão veio bem na hora que você foi descartado. O caminhão começa a processar o lixo que está lá, você morre esmagado no caminhão... Game Over.')
            time.sleep(4)










if escolhadopersonagem == 3:
    print ('Você escolheu Paulo')
    time.sleep(3)
    print ('Paulo tem um corpo muito atlético, perfeito para poder correr, escalar e nadar. Porém não tem nenhuma habilidade além disso.')
    time.sleep(3)
    print ('Você tem 2 escolhas para iniciar a fuga:')
    time.sleep(3)
    print ('Opção número 1: Se aproveitar da hora de tomar banho de sol e tentar escalar a parede da prisão.')
    time.sleep(4)
    print ('Ou')
    time.sleep(2)
    print ('Opção número 2: Se inscrever para oficina de esportes da cadeia para poder competir, e quem sabe até poder ir em competições lá fora. ')
    time.sleep(5)
    escolhadafuga = float(input('De qual jeito você pretende continuar? Digite o número da opção:'))
    time.sleep(2)

    if escolhadafuga == 1:
        print ('Você escolheu a opção 1')
        time.sleep(2)
        print ('Então você começa a escalar a parede do pátio de fora...')
        time.sleep(4)
        print ('Graças ao seu corpo atlético e forte você consegue chegar lá encima na divisória do muro.')
        time.sleep(4)
        print ('Porém os guardas estavam te esperando lá, porque te viram subir.')
        time.sleep(4)
        print ('Então eles te jogam la de cima, você cai e morre ali mesmo... Game Over.')
        time.sleep(5)

    if escolhadafuga == 2:
        print ('Você escolheu a opção 2')
        time.sleep(2)
        print ('Então você se inscreve para competir nas oficinas da cadeia. ')
        time.sleep(4)
        print ('Você foi aceito, então já começa a preparar alguns planos para poder fugir')
        time.sleep(5)
        print ('Então você tem dois planos para fuga:')
        time.sleep(3)
        print ('Plano 1:Treinar antes das competiçoes para poder melhorar mais ainda seu condicionamento.')#############
        time.sleep(4)
        print ('ou')
        time.sleep(2)
        print ('Plano 2:Já começar a competir com os outros presos.')
        time.sleep(3)
        escolhadoplano = float(input('Digite o número do plano escolhido para continuar:'))
        time.sleep(2)

        if escolhadoplano == 1:
            print ('Você escolheu o plano 1')
            time.sleep(2)
            print ('Então você começa a treinar e consegue melhorar mais ainda seu condicionamento, assim ficando mais forte e mais resistente para as provas.')
            time.sleep(6)
            print ('Você se destaca, e consequentemente a diretoria da cadeia organiza uma competição entre presos de outras cadeias e querem que você participe.')
            time.sleep(6)
            print (' Você tem duas opções:')
            time.sleep(2)
            print ('Opção 1:ir para uma competição de atletismo, apesar de não ser sua melhor modalidade, tem uma campo aberto onde a segurança é reduzida.')#######
            time.sleep(3)
            print ('ou')
            time.sleep(2)
            print ('Opção 2:ir para uma competição de natação já que é a modalidade que você mais se destaca.')
            escolhadoproblema = float(input('Digite o número da opção escolhida:'))
            time.sleep(2)

            if escolhadoproblema == 1:
                print ('Você escolheu a opção 1')
                time.sleep(2)
                print ('Então você vai para a competição no campo aberto, e pra sua sorte quase não tem guardas para monitorar os presos, então você se esconde no vestiário e espera todos irem lá fora, assim você volta por onde entrou e sai ali daquele campo, então ficando livre. Você conseguiu!!!')
                time.sleep(11)

            if escolhadoproblema == 2:
                print ('Você escolheu a opção 2')
                time.sleep(2)
                print ('Para o seu azar, a segurança está bem reforçada e ali não tem nenhum jeito de escapar, então você desiste de tentar fugir e acaba perdendo a chance... Game Over.')
                time.sleep(6)

        if escolhadoplano == 2:
            print ('Você escolheu o plano 2')
            time.sleep(2)
            print ('Você então começa a competir com os outros presos, porém sem nenhum treino e nem preparo antes, você não ganha reconhecimento nenhum e assim levando seu plano para o lixo... Game Over.')
            time.sleep(4) 



































































































