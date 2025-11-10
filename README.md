Angevane Dutra dos Santos
07 RJ - C1
Exercício Prático: Comandos Básicos de SQL com SQLite e Python



Explicando os códigos.

Usamos o import sqlite3 para importá-lo no script Python.
Em seguida temos: executar = sqlite3.connect. Que usamos para criar ou conectar-se a um banco de dados.
O cursor desempenha a execução da consulta.
já o cur.executemany é uma extensão lógica de exigir um único argumento para os valores.
con.commit() sinaliza o fim de uma transação e a salva permanentemente.
con.close() é uma boa prática para a liberação de recursos, evitando uma sobrecarga nas conexões.

Após a criação e ativação do anbiente virtual, gerou-se um arquivo chamado: requirements.txt. Também foi criado um banco de dados chamado Livro.db, com a utilização da biblioteca sqlite3. A conexão e o cursor foram estabelecidos para permitir a execução dos comandos SQL.
Logo então, crio-se a tabela Livros contendo ID, TITULO, AUTOR, ANO, GENERO e DISPONIVEL. Foram adicionandas cinco livros fictícios na tabela, contendo as informções acima, listadas.
Depois, foi realizada uma consulta para exibir todos os livros atualmente disponíveis. Seguido  da disponibilidade atualizado de um dos livros. Após, segue o comando de ordenação, dos recentes aos mais antigos, com base no campo ano. Foi executada uma exclusão de livro mais antigo.
Por fim, foi criada uma nova tabela chamada Usuario, repetindo o comando de criação de tabela descrito acima. Com a estrutura de campos: id e nome. Foi adicionada uma alteração usando o comando ALTER TABLE, para obter uma nova coluna denomida IDADE. Foram inseridos cinco registros aos campos NOME e IDADE.
E, terminando, foi excutado o comando DROP TABLE para excluir a tabela Usuario.


 Tabela LIVROS:

ID  TÍTULO                   AUTOR                    ANO    GÊNERO               DISPONÍVEL
------------------------------------------------------------------------------------------
1   A Sombra do Vento        Carlos Ruiz Zafón        2001   Mistério             Sim       
2   1984                     George Orwell            1949   Ficção Científica    Não       
3   O Senhor dos Anéis       J.R.R. Tolkien           1954   Fantasia             Sim       
4   Dom Quixote              Miguel de Cervantes      1605   Romance              Sim       
5   Cem Anos de Solidão      Gabriel García Márquez   1967   Realismo Mágico      Não  


TABELA USUARIOS:

ID  NOME                 IDADE
-----------------------------------
1   Alice                25
2   Bruno                30
3   Carla                22
4   Diego                28
5   Elisa                35



Fundamentos de Bancos de Dados

1- Por que os bancos de dados são essenciais em aplicações modernas?

> Um banco de dados tem a função de armazenar, organizar e gerenciar informações essenciais para garantir o funcionamento e a eficiência de diversas operações. Sem ele, perdemos a capacidade para guardar informações, ou seja, não teria backups de dados que são essenciais em caso de falhas no sistema, corrupção de dados ou desastres naturais.
https://barrazacarlos.com/pt-br/vantagens-e-desvantagens-dos-bancos-de-dados/


2- Quais são as duas principais categotias de banco de dados existentes?

> Banco de dados Relacionais> Um banco de dados relacional (ou banco de dados SQL) armazena dados em formato tabular com linhas e colunas. 
> Banco de dados Não Relacionais> Um banco de dados não relacionais (ou bancos de dados NoSQL) usam uma variedade de modelos de dados para acessar e gerenciar dados.
https://aws.amazon.com/pt/compare/the-difference-between-relational-and-non-relational-databases/


3- Em quais cenários é recomendado utilizar um banco de dados  relacional?

> Por causa da boa organização de um banco de dados SQL, temos o seguinte exemplo de cenário: se você tem um cadastro de clientes e seus pedidos, não precisa repetir os dados de cada um sempre. Basta relacionar os dados e pronto, tudo fica bem organizado.
https://mosten.com/banco-de-dados-relacional/


3- De que forma os recursos de hardware (CPU, memória, disco) afetam a  performance de um banco de dados? 

> Se a CPU for inadequada, isso pode levar à execução lenta da consulta e à degradação do desempenho do banco de dados. Em alguns casos, a atualização da CPU pode melhorar significativamente o desempenho do banco de dados.
As limitações de hardware podem ter um impacto significativo no desempenho do banco de dados. É essencial garantir que o servidor de banco de dados tenha RAM, espaço em disco rígido e CPU suficientes para suportar a carga de trabalho.
https://www.loadview-testing.com/pt-br/blog/5-problemas-e-correcoes-de-desempenho-de-banco-de-dados-mais-comuns/


5- O que significa escalabilidade no contexto de bancos de dados? 

> A escalabilidade é um aspecto crítico no desempenho de sistemas de banco de dados: 
Escalabilidade Vertical (Scale-Up)= Aumento da capacidade do mesmo servidor onde o banco de dados está instalado, por meio da adição de CPU, memória RAM, SSDs mais rápidos, etc.
Escalabilidade Horizontal (Scale-Out)= Consiste em adicionar novas instâncias ou servidores para distribuir carga e dados. É baseada na replicação e/ou particionamento (sharding).
https://blog.grancursosonline.com.br/escalabilidade-horizontal-e-vertical-em-bancos-de-dados-relacionais-e-nosql/


6- Qual a relevância de organizar corretamente os dados em bancos
relacionais?

> A normalização é uma fase do processo de projetar um banco de dados que busca eliminar redundâncias e inconsistências nos dados armazenados em um banco de dados modelo relacional, planejando a sua estrutura e o formato das tabelas.
> A estruturação refere-se a forma de como os dados são organizados em tabela. Onde cada tabela, tem suas linhas e colunas representando os seus respectivos atributos.
https://www.alura.com.br/artigos/banco-dados-relacionais-conceitos-terminologias-ferramentas


 
7- Como escolher entre SQL e NoSQL para um novo projeto?

> A escolha entre SQL e NoSQL não é uma questão de qual é "melhor", mas sim de qual é "mais adequado":
SQL: Modelo relacional com esquema fixo. Ótimo para dados bem estruturados onde as relações são cruciais. A normalização é fundamental. Ex.: Vivo:SQL Server; Itaú: MySQL; Microsoft: SQL Server. 

NOSQL: Modelos diversos (documento, chave-valor, coluna, grafo) com esquema flexível ou sem esquema. Ideal para dados não estruturados, semi-estruturados ou em constante evolução. Ex.: Twitter, GitHub, Pinterest, etc.
https://dicasdeprogramacao.com.br/sql-vs-nosql-guia-completo-para-escolher-o-banco-de-dados-certo-para-seu-projeto/




Comandos SQL

1. Qual é a finalidade do comando SELECT em SQL? 
https://www.devmedia.com.br/sql-select-guia-para-iniciantes/29530
Ele recupera dados de um objeto no banco de dados. tais como: selecionar colunas específicas, aplicar filtros, ordenar resultados e realizar operações mais complexas como junções e agrupamentos.

2. O que significam as siglas DML e DDL em bancos de dados?
https://learnsql.com.br/blog/o-que-sao-ddl-dml-dql-e-dcl-em-sql/
Data Manipulation Language (DML ): responsavável pela adição, edição ou exclusão dos dados em um banco: INSERT, UPDATE, e DELETE;
Data Definition Language (DDL ): sub-língua responsável pelas tarefas administrativas de controle do próprio banco de dados, especialmente a concessão e revogação de permissões de banco de dados para os usuários: GRANT, REVOKE, e DENY, entre outros.

3. Para que serve a cláusula WHERE em consultas SQL? 
https://www.datacamp.com/pt/doc/mysql/mysql-where
Para filtrar registros em uma instrução SQL, permitindo que você especifique condições que devem ser atendidas. É comumente usado para restringir os resultados da consulta, tornando a recuperação de dados mais eficiente e específica.

4. Por que é fundamental estabelecer uma chave primária (PRIMARY KEY)
 em tabelas?
https://www.datacamp.com/pt/tutorial/sql-primary-key
As chaves primárias são essenciais para garantir a integridade dos dados e permitir consultas eficientes, sendo de muita importância para a normalização do banco de dados e a integridade relacional.

5. Como funciona o comando UPDATE e qual sua sintaxe básica?
https://didatica.tech/tudo-sobre-o-comando-update-em-sql/
Garantir que as informações permaneçam relevantes, precisas e seguras. Seja ajustando detalhes individuais após uma entrada incorreta ou implementando atualizações em massa como parte de uma mudança maior no sistema, o comando UPDATE é essencial para a integridade dos dados.
UPDATE nome_tabela
SET coluna1 = valor1, coluna2 = valor2,...
WHERE condição;

6. Qual a função do comando DELETE em SQL?
https://blog.betrybe.com/sql/sql-delete/
Deletar os dados de uma ou mais linhas da tabela. É importante ressaltar que esse comando não exclui estruturas do banco, apenas os dados armazenados nele. 

7. Como a cláusula ORDER BY organiza os resultados de uma consulta?
https://www.datacamp.com/pt/doc/mysql/mysql-order-by
Ele permite a classificação em ordem crescente ou decrescente, o que pode ajudar a organizar os dados de forma significativa. É aplicada no final de uma instrução `SELECT` para classificar os dados recuperados. Você pode especificar a ordem crescente usando `ASC` (padrão) ou a ordem decrescente usando `DESC`.

8. Para que serve o comando LIMIT em consultas SQL? 
https://www.datacamp.com/pt/tutorial/sql-limit
É uma cláusula útil que especifica o número de registros que uma consulta deve retornar após a filtragem dos dados. Essa técnica permite que você retorne apenas um subconjunto de dados para exibição ou análise. Portanto, a cláusula LIMIT é importante para dividir dados grandes em partes menores na paginação de dados. Ele também é usado para otimizar o desempenho, a fim de evitar consultas grandes que possam reduzir o desempenho do banco de dados


Outros Conceitos


1. Por que é importante integrar o banco de dados com a camada de back
end da aplicação?
https://flammadesign.com.br/glossario/o-que-e-integracao-back-end/
Porque é crucial para o desempenho e a escalabilidade de uma aplicação. Sem uma integração eficaz, os dados podem ficar desatualizados ou inconsistentes, o que pode levar a erros e falhas na experiência do usuário. Além disso, a integração back-end permite que as empresas conectem sistemas legados com novas tecnologias, facilitando a transição e a modernização de suas infraestruturas de TI.

2. O que são views (visões) em bancos de dados e quais suas vantagens?
https://pt.wikipedia.org/wiki/Vis%C3%A3o_(banco_de_dados)
É um conjunto resultado de uma consulta armazenada sobre os dados, em que os usuários do banco de dados podem consultar simplesmente como eles fariam em um objeto de coleção de banco de dados persistente. Este comando de consulta pré-estabelecido é armazenado no dicionário de banco de dados.

3. Quais são as propriedades ACID e por que são cruciais para
 transações?
https://fabiojaniolima.gitbooks.io/banco-de-dados-modelagem-de-dados/content/capitulo-1/1.6-ACID-atomicidade-consistencia-isolamento-e-durabilidade.html
ACID é um termo utilizado em ciência da computação para descrever as 4 propriedades que garantem a integridade das transações em um banco de dados. Veja a descrição de cada uma delas:
Atomicidade:
Essa propriedade garante que todas as transações sejam atômicas (indivisíveis), ou seja, que as transações sejam executadas em sua totalidade. Se ocorrer algum erro, todas as operações que compõem a transação serão descartadas.
Consistência:
A execução de uma transação deve levar o banco de dados de um estado consistente para outro estado de consistência, ou seja, toda transação deve respeitar as regras de integridade dos dados (tipo de dado, chave primária etc).
Isolamento:
É um recurso do banco que tem como objetivo evitar que, em um sistema multiusuário, transações em paralelo interfiram umas nas outras.
Durabilidade:
Significa que os efeitos de uma transação são permanentes, podendo ser desfeitos somente como resultado de uma transação posterior e bem-sucedida.

4. O que estabelece o Princípio do Privilégio Mínimo em segurança de
 bancos de dados?
https://www.startupdefense.io/pt-br/blog/o-principio-do-menor-privilegio-na-seguranca-cibernetica
É uma prática recomendada de segurança cibernética que exige conceder aos usuários, aplicativos e sistemas o nível mínimo de acesso necessário para concluir as funções atribuídas. Essa abordagem limita os possíveis danos causados por credenciais comprometidas, erro humano ou informações internas mal-intencionadas.