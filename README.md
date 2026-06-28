# Projeto de Implantação de API com Fluxo DevOps - Pequeno Marketplace

Este repositório contém o Trabalho Final da disciplina de Cloud Computing do curso de Bacharelado em Sistemas de Informação da UNIDAVI (junho de 2026). O objetivo do projeto é demonstrar a construção de uma API REST funcional integrada a um pipeline de Integração Contínua (CI) via GitHub Actions.

* **Estudante:** [Seu Nome Completo Aqui]
* **Professor:** Prof. Esp. Ademar Perfoll Junior
* **Tema Atribuído:** Infraestrutura para um Pequeno Marketplace
* **Recurso Central:** Produtos (`/produtos`)

---

## 📂 Estrutura de Diretórios do Repositório

```text
marketplace-api/
 ├── .github/
 │    └── workflows/
 │         └── ci.yml          # Configuração do Pipeline CI (GitHub Actions)
 ├── api/
 │    ├── app.py               # Código-fonte principal da API Flask
 │    ├── data/
 │    │    └── produtos.json   # Base de dados simulada externa (JSON)
 │    └── tests/
 │         └── test_api.py     # Scripts de Testes Unitários (Pytest)
 └── README.md                 # Documentação de instrução do projeto
