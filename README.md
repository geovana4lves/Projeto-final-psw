# SEGA — Sistema de Gestão Acadêmica

Sistema web desenvolvido com Django para gerenciamento de informações acadêmicas, permitindo o controle de cursos, pessoas, professores, turmas, disciplinas e matrículas.

O projeto possui uma área pública e uma área administrativa protegida por autenticação e permissões de usuário.

## Funcionalidades

### Área pública

- Página inicial;
- Cadastro de usuário;
- Login;
- Logout;
- Interface responsiva.

### Área administrativa

- Dashboard com dados reais do banco;
- Controle de acesso por permissões;
- Mensagens de feedback;
- Página personalizada de acesso negado;
- Tema claro e escuro;
- Interface responsiva.

### Gerenciamento acadêmico

O sistema possui operações de:

- criação;
- listagem;
- visualização de detalhes;
- edição;
- exclusão;
- pesquisa.

Essas operações estão disponíveis para:

- Cursos;
- Pessoas;
- Professores;
- Turmas;
- Disciplinas;
- Matrículas.

---

## Relacionamentos

O projeto utiliza relacionamentos entre os diferentes módulos acadêmicos.

### Curso e Turma

Uma turma pertence a um curso.

```text
Curso
  └── Turma
```

### Professor, Turma e Disciplina

Uma disciplina está relacionada a um professor e a uma turma.

```text
Professor
    └── Disciplina
            └── Turma
```

### Pessoa e Matrícula

Uma matrícula relaciona uma pessoa a uma turma.

```text
Pessoa
   └── Matrícula
           └── Turma
                 └── Curso
```

---

## Autenticação e permissões

A autenticação é realizada utilizando o sistema nativo do Django.

O projeto utiliza:

- `django.contrib.auth`;
- login;
- logout;
- usuário personalizado;
- `login_required`;
- `permission_required`;
- permissões de visualização;
- permissões de criação;
- permissões de edição;
- permissões de exclusão.

Usuários comuns podem acessar o sistema, mas somente visualizam os recursos para os quais possuem permissão.

Tentativas de acesso direto a uma área não autorizada retornam uma página personalizada de erro **403 — Acesso negado**.

---

## Dashboard

O painel administrativo apresenta informações obtidas diretamente do banco de dados, incluindo a quantidade de:

- cursos;
- pessoas;
- professores;
- turmas;
- disciplinas;
- matrículas.

Os cards também respeitam as permissões do usuário autenticado.

---

## Pesquisa

As páginas de listagem possuem pesquisa integrada ao banco de dados.

É possível pesquisar informações como:

- nome do curso;
- tipo do curso;
- nome da pessoa;
- usuário;
- CPF;
- cidade;
- professor;
- formação;
- titulação;
- turma;
- disciplina;
- curso relacionado à matrícula.

---

## Tecnologias utilizadas

- Python
- Django
- HTML5
- CSS3
- JavaScript
- Bootstrap
- SQLite
- Bootstrap Icons
- Git
- GitHub

---

## Templates utilizados

### Área pública

A interface pública utiliza como base o tema **Edulab / Eduleb**, disponibilizado pelo ThemeWagon.

### Área administrativa

A interface interna utiliza como base o tema **AdminHMD**, disponibilizado pelo ThemeWagon.

Os templates foram adaptados para integração com Django e com o Sistema de Gestão Acadêmica.

---

## Estrutura principal

```text
djangotutorial/
│
├── curso/
├── disciplina/
├── matricula/
├── pessoa/
├── professor/
├── turma/
│
├── mysite/
│
├── static/
│   ├── adminhmd/
│   └── eduleb/
│
├── templates/
│   ├── components/
│   ├── registration/
│   ├── 403.html
│   ├── base_admin.html
│   ├── base_public.html
│   ├── home.html
│   └── painel.html
│
└── manage.py
```

---

## Executando o projeto

Entre na pasta que contém o arquivo `manage.py`:

```bash
cd djangotutorial
```

Execute as migrations:

```bash
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

Depois acesse:

```text
http://127.0.0.1:8000/
```

---

## Criando um superusuário

Caso seja necessário criar um administrador:

```bash
python manage.py createsuperuser
```

Depois, faça login no sistema com a conta criada.

---

## Verificação do projeto

Para verificar possíveis erros de configuração:

```bash
python manage.py check
```

Para conferir se existem alterações de models ainda não registradas:

```bash
python manage.py makemigrations --check --dry-run
```

O resultado esperado, caso esteja tudo correto, é:

```text
System check identified no issues (0 silenced).
```

e:

```text
No changes detected
```

---

## Módulos

### Curso

Gerenciamento dos cursos disponíveis no sistema.

### Pessoa

Cadastro e gerenciamento dos usuários/pessoas do sistema.

### Professor

Gerenciamento dos professores e suas informações acadêmicas.

### Turma

Gerenciamento das turmas vinculadas aos cursos.

### Disciplina

Gerenciamento das disciplinas vinculadas a professores e turmas.

### Matrícula

Gerenciamento da relação entre pessoas e turmas.

---

## Segurança

As operações administrativas são protegidas por autenticação e permissões do Django.

A interface esconder um recurso não é utilizada como única forma de segurança: as próprias views também verificam as permissões antes de permitir acesso às operações.

---

## Status

Projeto funcional com:

- CRUD completo;
- autenticação;
- autorização;
- pesquisa;
- dashboard;
- mensagens de feedback;
- interface responsiva;
- tratamento de acesso negado;
- integração entre os principais módulos acadêmicos.

---

## Créditos

Interfaces adaptadas a partir dos templates gratuitos disponibilizados pelo **ThemeWagon**:

- Edulab / Eduleb;
- AdminHMD.
