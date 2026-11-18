# Instruções do repositório

## Descrição do projeto

Este projeto é um site educacional para compartilhar tarefas e exercícios de programação. Os alunos podem navegar pelo portal, visualizar os enunciados e baixar arquivos de apoio. A página principal é um portal estático implementado com HTML, CSS e JavaScript, sem framework.

## Estrutura do projeto

- `assignments/` contém uma subpasta por tarefa, com os enunciados e arquivos de apoio.
- `templates/` contém modelos reutilizáveis para criar conteúdo.
- `assets/` contém CSS, JavaScript, imagens e materiais de apoio do site.
- `index.html` é a página principal do portal.
- `config.json`, na raiz do repositório, define as informações do curso e a lista de tarefas usada para gerar dinamicamente as listas e os detalhes no portal.
- Mantenha nomes de arquivos e pastas descritivos e organizados, e preserve o estilo consistente entre as páginas.
- Mantenha o `id` e o caminho de cada tarefa em `config.json` coerentes com a subpasta correspondente em `assignments/`.
- Use `templates/assignment-template.md` como base ao criar ou reorganizar enunciados. Nas pastas de tarefas, siga a convenção documentada de usar `README.md`, `starter-code.py` e, quando necessário, `data.csv`. Não crie arquivos de solução sem solicitação explícita.
- Hooks e materiais de apoio ao exercício sobre personalização do Copilot estão em `assets/extra/`; não os mova para `.github/` sem necessidade.

## Padrões educacionais

- Defina objetivos de aprendizado claros e adeque o nível de dificuldade ao público da tarefa.
- Use linguagem clara e encorajadora, amigável ao aluno.
- Preserve requisitos e exemplos didáticos existentes ao modificar uma atividade.

## Alterações e validação

- Faça mudanças pequenas e consistentes com os arquivos próximos; não introduza dependências ou ferramentas de build sem necessidade.
- Ao adicionar uma tarefa, atualize `config.json` e confira se os caminhos e anexos apontam para arquivos existentes.
- Ao alterar HTML, CSS ou JavaScript, preserve o funcionamento em navegador e as referências relativas entre páginas e arquivos.
- Não há configuração de testes ou build indicada na raiz. Para mudanças em dados estruturados, valide o JSON; para código Python alterado, execute verificações pertinentes quando disponíveis.