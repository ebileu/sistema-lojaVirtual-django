<h1>Sobre o Projeto</h1>
<p>Você foi contratado pela "TechStore", uma empresa fictícia que deseja criar um sistema de gerenciamento de produtos, para a sua loja virtual. A TechStore deseja uma aplicação web onde eles possam adicionar, editar, excluir e visualizar produtos que estão disponíveis para a venda em seu site.</p>

<h1>Objetivo</h1>
<p>Desenvolver um sistema de gerenciamento de produtos utilizando programação back-end, onde será possível realizar as operações básicas de CRUD (Create, Read, Update, Delete) em relação aos produtos da loja virtual.</p>

<h2>Requisitos Técnicos</h2>
<p>Tecnologias utilizadas:</p>
<ul>
  <li><strong>Python com Django</strong></li>
  <li><strong>Bootstrap</strong></li>
  <li><strong>SQLITE3</strong></li>
</ul>

<h2>Funcionalidades</h2>
<ul>
  <li>Cadastro de novos produtos com os seguintes campos: nome, descrição, preço e quantidade em estoque;</li>
  <li>Listagem de todos os produtos cadastrados, exibindo todas as informações;</li>
  <li>Edição dos dados de um produto existente;</li>
  <li>Exclusão de um produto;</li>
  <li>Implementar validações necessárias nos formulários para garantir a integridade dos dados (por exemplo, campos obrigatórios, formatos válidos, etc.)</li>
  <li>Criar uma interface amigável para facilitar a interação com o sistema</li>
</ul>

<h2>Instruções para iniciar o projeto</h2>
Após salvar o projeto, no terminal do VS Code, será necessário inicializar o ambiente virtual que está instalado o framework.
Para inicializar o ambiente virtual, é necessário digitar o comando: venv\Scripts\Activate. Logo após iniciar o ambiente virtual, será necessário inicializar o servidor usando o comando: python manage.py runserver e vai ser gerado um link no terminal, onde poderá acessar a aplicação.

<h2>Sobre as tecnologias utilizadas</h2>
Utilizei o Django, framework do Python, para a criação do sistema. Eu escolhi o Django por ser um framework de uma linguagem na qual eu mais tenho estudado nos últimos tempos e gostaria de me aprofundar mais. 

Usei do Bootstrap para a estilização dos templates do programa, deixando a estilização, na minha visão, mais simples e até mais organizado e bonito de ver em código.

O banco de dados utilizado foi o que está configurado como padrão no Django, que é o SQLITE3, e foi o que utilizei para criar a tabela e os atributos da entidade. A tabela foi criada no arquivo models.py e a visualização da tabela se encontra no arquivo db.sqlite3 (para ser possível ver a tabela no VS Code, é recomendável baixar a extensão SQLite Viewer). 

<h2>Melhorias para o futuro</h2>
<ul>
  <li>Adicionar um método de verificação para caso tenha um produto cadastrado com o mesmo nome no banco e avisar ao usuário sobre (talvez até mesmo perguntar qual dos dois cadastros o usuário deseja manter no banco);</li>
  <li>Melhorar o design do template (deixando inclusive responsivo), pois como minha intenção foi mais focar no CRUD, acabei deixando o design da página mais simples e funcional;</li>
  <li>Aumentar a quantidade de cadastros do sistema, quis limitar o sistema para até 12 cadastros, para não ficar algo muito extenso ou com muita informação, então preferir deixar um pouco mais simples, novamente, focando mais no processo de CRUD;</li>
  <li>Adicionar um campo no cadastro do produto, onde poderia ser possível adicionar o tipo do produto, se é consumível, material, ferramenta e etc... e aproveitando esse gancho, também seria interessante adicionar uma opção de filtragem de tipo do produto, onde o   usuário poderia visualizar apenas os produto do tipo que ele filtrou;</li>
  <li>Ainda no cadastro do produto, seria interessante poder adicionar uma foto do produto para identificação e até mesmo colocar uma data em que o produto foi cadastrado, para afins de consulta.</li>
</ul>

<h2></h2>
<p>Esta atividade foi proposta pela UNIFAN (Centro Universitário Nobre) de Feira de Santana</p>
