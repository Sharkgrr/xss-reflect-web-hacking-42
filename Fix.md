# Como prevenir ataques XSS Reflected

## Enconding 

Uma das formas mais eficientes de prevenir é utilizando o método "Enconding" que tem como principio a validação e sanitização dos caracteres inseridos no input e output. Transformar toda entrada de dados em texto, como exemplo: converter  `<`  para  `&lt;` ou `>`  converter para `&gt;` com objetivo de anular qualquer script malicioso.

## Whitelisting 
Listas de permissões são efetivas para bloquear tentativas de ataque com valores inválidos. Para realiza-lo basta criar uma lista de protocolos e então a aplicação aplicará a regra se deve ou não requisitar.

Referências
* https://evernow.com.br/como-proteger-sua-empresa-de-ataques-xss-e-assegurar-seus-dados/
* https://portswigger.net/web-security/cross-site-scripting/preventing


