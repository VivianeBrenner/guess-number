# **Guess Number**

Bem-vindo ao **Guess Number**, um jogo simples de adivinhação de números escrito em Python. O objetivo do jogo é adivinhar um número aleatório dentro de um intervalo definido pelo usuário.  

---

## **Descrição do Projeto**

Este projeto é ideal para iniciantes que desejam praticar:
- Entrada e saída de dados com `input` e `print`.
- Condicionais (`if`, `elif`, `else`).
- Estruturas de repetição (`while`).
- Manipulação de números aleatórios com o módulo `random`.

O código implementa a lógica do jogo com tratamento de erros e feedback interativo para o usuário.

---

## **Como Funciona:**

1. O usuário define o número máximo (teto) para o desafio.
2. O programa escolhe um número aleatório entre 0 e o número definido.
3. O usuário tenta adivinhar o número.
4. A cada tentativa, o programa informa se o palpite está **muito alto** ou **muito baixo**.
5. O jogo termina quando o número é acertado, exibindo o total de tentativas realizadas.

---

## **Requisitos:**

- Python 3.x instalado no sistema.
- Nenhuma dependência externa é necessária.

---

## **Como Executar:**

1. Clone ou baixe este repositório:
   ```bash
   git clone https://github.com/SeuUsuario/guess-number.git
    ```
2. Navegue até o diretório do projeto:
    ```bash 
    cd guess-number
    ```
3. Execute o programa:
    ```bash
    python main.py
    ```
4. Exemplo de Execução
    ```plaintext
    Bem-vindo ao Guess Number!
    Digite o número teto do desafio: 50
    Adivinhe o número: 25
    Chutou baixo! O número é maior que isso...
    Adivinhe o número: 40
    Acertou!
    Número de tentativas: 2
    ```