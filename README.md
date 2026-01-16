# 🐍 Curso Backend Python & Django | Bolsa Futuro Digital (UEPA)

Bem-vindo ao repositório oficial da turma de **Backend Python & Django** do programa **Bolsa Futuro Digital**, realizado na **Universidade do Estado do Pará (UEPA)**.

Este repositório contém todos os códigos, exercícios e projetos desenvolvidos durante as aulas práticas e mentorias, servindo como portfólio de aprendizado e base de consulta para os alunos.

---

## 📂 Estrutura do Repositório

A organização das pastas segue a temática da **Ementa Oficial**

### 🔹 `/lppy` - Lógica de Programação com Python
Refere-se à disciplina introdutória **Lógica de Programação com Python (LPPY)**.
* **Conteúdo:** Algoritmos, variáveis, tipos de dados, estruturas de controle (if/else, loops), funções e modularização.
* **Foco:** Desenvolvimento do pensamento computacional e sintaxe básica da linguagem.

### 🔹 `/poo` - Programação Orientada a Objetos
Refere-se à disciplina **Python e Orientação a Objetos (POB)**.
* **Conteúdo:** Classes, objetos, atributos, métodos, herança, polimorfismo, encapsulamento e tratamento de exceções.
* **Foco:** Estruturação de código moderno e reutilizável.

### 🔹 `/db` - Banco de Dados
Refere-se à disciplina **Noções de Banco de Dados (NBD)**.
* **Conteúdo:** Scripts SQL e consultas básicas.
* **Foco:** Persistência de dados e preparação para o uso de ORMs.

### 🔹 `/html` - Tecnologias Web (Front-end Básico)
Material de apoio para a compreensão da arquitetura cliente-servidor.
* **Conteúdo:** Estrutura básica de HTML5 e introdução ao funcionamento da Web (HTTP, Requisição/Resposta).
* **Objetivo:** Dar base para a construção dos *Templates* no Django.

### 🔹 `/django` - Framework Web
Refere-se à disciplina central **Django (DJ)**.
* **Conteúdo:** Configuração de ambiente, padrão MTV (Model-Template-View), rotas (URLs), Views, Forms e Admin.
* **Foco:** Criação de aplicações web dinâmicas.

### 🔹 `/mentoria` - Atividades de Mentoria
Códigos desenvolvidos durante as sessões de **Mentoria Remota**.
* **Conteúdo:** Resolução de dúvidas específicas, desafios extras, *Code Reviews* e aprofundamento de tópicos complexos.

---

## 🛠️ Configuração do Ambiente

Para executar os códigos deste repositório, recomenda-se o uso de um ambiente virtual (`virtualenv`).

### Pré-requisitos

* Python 3.10+
* Git

### Passo a passo

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/CURSO-BACKEND-PYTHON.git](https://github.com/SEU_USUARIO/CURSO-BACKEND-PYTHON.git)
    cd CURSO-BACKEND-PYTHON
    ```

2.  **Crie e ative o ambiente virtual:**
    * *Windows:*
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * *Linux/Mac:*
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Instale as dependências (para projetos Django):**
    ```bash
    pip install django
    Instale as outras dependência no ambiente virtual criado
    ```

*Projeto realizado com apoio do Ministério da Ciência, Tecnologia e Inovação (MCTI) e Softex Pernambuco.*
