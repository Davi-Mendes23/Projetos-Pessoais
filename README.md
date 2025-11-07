# Projetos Pessoais - Portfólio de Desenvolvimento

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/Status-Em%20Desenvolvimento-brightgreen)
![GitHub](https://img.shields.io/badge/License-MIT-blue)

## 📋 Sobre o Repositório

Este repositório contém uma coleção de projetos pessoais desenvolvidos para praticar e demonstrar habilidades em programação e desenvolvimento de software. Os projetos abrangem diversas tecnologias e áreas do desenvolvimento web e mobile.

# 🚀 Projetos Destacados
## **IFMG**

### 1. **Agenda de contatos**
- **Descrição:** Aplicação CLI para gerenciar uma agenda simples usando classes
- **Funcionalidades:**
  - Inclusão de novo contato (valida nome obrigatório).
  - Alteração de contato: edição campo-a-campo (enter em branco mantém valor).
  - Exclusão de contato por código (índice).
  - Salvamento e carregamento de contatos em arquivo CSV (escrita com cabeçalho, leitura com tratamento de arquivo vazio).
  - Tratamento básico de entrada inválida (evita crash ao converter código não numérico).
  - Estrutura orientada a objetos (separa responsabilidades: Contato, Arquivo, Agenda).

### 2. **Arvore genealógica**
- **Descrição:** Aplicação em Python para gerenciar uma árvore genealógica
- **Funcionalidades:**
  - Inclusão de pessoas na árvore (com verificação de duplicidade e nome obrigatório).
  - Edição de parentescos: definição e alteração de pai e mãe com validação de existência.
  - Listagem ordenada de todas as pessoas e seus parentes diretos.
  - Exclusão de pessoas (somente se não forem pai ou mãe de ninguém).
  - Visualização recursiva da árvore de ancestrais e árvore de descendentes.
  - Salvamento automático dos dados em arquivo JSON com UTF-8 e formatação indentada.
  - Interface de menu interativo em terminal, com opções para incluir, excluir, consultar, salvar e sair.
  - Estrutura orientada a objetos (classe Arvore) com persistência de estado e validações robustas.


### 3. **Jogo da Velha**
- **Descrição:** Versão interativa do clássico Jogo da Velha, jogado no terminal contra uma inteligência artificial básica
- **Funcionalidades:**
  - Interface em texto com coordenadas no formato “1A”, “2B”, etc.
  - Modo single player: jogador humano (X) contra IA (O).
  - IA inteligente:
    - Tenta vencer se possível na jogada atual.
    - Bloqueia vitória iminente do jogador humano.
    - Escolhe uma jogada aleatória quando não há jogadas críticas.
  - Detecção automática de vitória e empate.
  - Atualização visual do tabuleiro a cada jogada.
 
## **Projeto Tupan**

### 4. Tupan — Analisadora Inteligente de Dados
- **Descrição:** Aplicação desenvolvida em Jupyter Notebook que utiliza a API da OpenAI para criar uma IA analítica (E.V.I.) capaz de interpretar e responder perguntas sobre dados de planilhas CSV. O sistema combina pandas para processamento de dados e modelos de linguagem para gerar insights textuais automáticos.
- **Funcionalidades:**
  - Leitura e análise automática de arquivos CSV com o pandas.
  - Geração de resumo estatístico completo dos dados (describe).
  - Exibição controlada de tabelas parciais para bases muito grandes.
  - Integração com a API da OpenAI via cliente Python (OpenAI).
  - Construção de prompt contextual combinando os dados e o resumo para a IA responder perguntas.
  - Interface interativa em notebook (Jupyter) para experimentação direta.
  - Estrutura modular com funções reutilizáveis (resumo_dados, tabela_completa_str).
  - Configuração de API Key e endpoint personalizável (compatível com OpenRouter).

### 5. Oráculo — Assistente de Conhecimento com IA
- **Descrição:** Notebook em Python que implementa um sistema de perguntas e respostas inteligente, utilizando embeddings semânticos e modelos de linguagem da OpenAI para responder com base em informações de um banco de dados CSV. O projeto integra LangChain, FAISS e HuggingFace Transformers para criar um fluxo completo de RAG (Retrieval-Augmented Generation).
- **Funcionalidades:**
  - Leitura e indexação de dados a partir de um arquivo CSV (knowledge_base.csv).
  - Criação de vetores semânticos com HuggingFaceEmbeddings.
  - Armazenamento e busca vetorial eficiente via FAISS.
  - Integração com LangChain para orquestrar a busca e geração de respostas.
  - Uso da API da OpenAI (compatível com OpenRouter) para gerar respostas contextuais e explicativas.
  - Pipeline modular para carregar dados, buscar similaridades e responder perguntas.
  - Interface interativa via Jupyter Notebook, ideal para testes e demonstrações.
  -  Estrutura flexível para expansão com outras fontes de dados ou formatos (JSON, PDFs etc.).

### Ferramentas de Desenvolvimento

![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![VSCode](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## 🎯 Objetivos do Desenvolvimento

- **Prática:** Aplicar conceitos de programação em projetos reais
- **Aprendizado:** Explorar novas tecnologias e frameworks
- **Portfólio:** Demonstrar habilidades para oportunidades profissionais
- **Evolução:** Melhorar constantemente a qualidade do código

## 📈 Próximos Passos

- [ ] Adicionar mais projetos com diferentes tecnologias
- [ ] Implementar testes automatizados
- [ ] Adicionar documentação detalhada para cada projeto
- [ ] Criar versões responsivas para mobile
- [ ] Adicionar integração com APIs

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Enviar pull requests
- Compartilhar ideias para novos projetos

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<div align="center">

⭐ **Se este repositório foi útil, considere dar uma estrela!** ⭐

</div>





