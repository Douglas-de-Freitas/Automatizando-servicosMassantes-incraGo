Estes dois programas foram feitos em Python com o objetivo de facilitar dois dos serviços massantes que existem dentro do INCRA-GO em relação ao sistema Sipra.

1 - Para executar estes programas você precisará estar dentro da Rede, (trabalhando no incra, ter acesso e estar autenticado no Sipra, e possuir um conhecimento de Python

com o sistema atual em 12/2018 não é possível retirar vários relatórios de tela. (RB e ESPELHO)

Exemplo Espelho:

Os técnicos do Incra precisam retirar vários espelhos de um assentamento x para leva-los em sua viagem ao assentamento, ou para fazer um serviço de notificação.
No sistema atual eles precisam:

Digitar o CPF,
Aguardar uma busca do beneficiário que não é nada otimizada, 
assim que a busca retornar sucesso
Entrar em beneficiário --> espelho do beneficiário
e por fim mandar imprimir aquele espelho x

e geralmente eles precisam de todos os espelhos de um assentamento x, então se o assentamento possui 500 famílias, eles precisam fazer o procedimento acima para tirar os 500 espelhos. 

viu como é massante? você precisaria ver pessoalmente :(

Com o arquivo que eu fiz em Python na pasta Imprimir Espelho, você que trabalha no Incra só precisará de jogar no (arquivo.txt) os códigos dos beneficiários que deseja imprimir.
Obs: cada código em uma linha do arquivo.

Depois de que jogar os códigos no arquivo, basta executar o programa e pode ir almoçar que quando voltar estará tudo pronto.

Obs: O sleep deve ser alterado de acordo com sua conexão, para que não ocorra erros, se sua conexão estiver ruim aumente os sleeps, se estiver rápida pode diminuir ou deixar como está.

No caso Das RB's o serviço também é muito massante, pois, somente existe a possibilidade no sistema de retirar uma por uma.

Então nesse caso faça o mesmo com o (arquivo.txt) da pasta Imprimir RB, basta colocar os códigos dos assentamentos que deseja imprimir, e ir almoçar.

Obs: não se esqueça dos sleeps se sua conexão não estiver boa.

Espero ter ajudado :)
 