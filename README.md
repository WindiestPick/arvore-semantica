# Árvore-Semântica

Algoritmo de árvore semântica capaz de testar todas as possibilidades possíveis para a dinâmica dos vasos
infelizmente não consegui representar a árvore na saída do algoritmo mas tentei representar da forma
mais simples possível para compreensão.

Para cada possibilidade ainda não existente o algoritmo verifica todas as 6 possibilidades que ele tem
disponível até que todas as possibilidades possíveis sejam encontradas.

## Estrutura do codigo

O primeiro foram criada duas classes (Vaso e Regras)

### Vaso
> A classe vaso é feita para criar o objeto vaso, ele tem 2 atributos e 1 metodo alem dos geters e os seters.
> 
> Seus atributos são:
> - volume: responsável por definir a quantidade de litros existente dentro do vaso.
> - limite: define a quantidade máxima de litros que cabe no vaso.
> 
> O metodo é o:
> - despejaNoOutro: esse metodo é feito para despejar o volume de um vaso no outro respeitando o limite do obijeto.

### Regras
> A classe regras define as açoes possíveis para o algoritimo, além de manipular os jarros para que não haja inter
> ferencia direta no volume dos vasos. A classe possui dois atributos e 6 metodos (sendo cada um uma ação) além dos
> geters e seters.
>
> Seus atributos são:
> - vaso1: onde irá receber o primeiro objeto da classe vaso.
> - vaso2: onde ira receber o segundo objeto da classe vaso.
> 
> E os metodos são:
