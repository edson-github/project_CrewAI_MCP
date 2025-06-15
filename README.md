# CrewAI MCP (Market Analysis Crew Project)

Este projeto utiliza o framework CrewAI para criar uma equipe automatizada de análise de mercado e planejamento estratégico.

## Estrutura do Projeto

```
project_crewai_mcp/
├── agents.yml         # Definição dos agentes
├── tasks.yml          # Definição das tarefas
├── crew.yaml          # Configuração do crew
├── .env               # Variáveis de ambiente
└── requirements.txt   # Dependências
```

## Pré-requisitos

- Python 3.9 ou superior
- Pip (gerenciador de pacotes Python)
- Chave de API da OpenAI

## Instalação

1. Clone o repositório:
```bash
git clone [url-do-repositorio]
cd project_crewai_mcp
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
- Copie o arquivo `.env.example` para `.env`
- Adicione sua chave da API da OpenAI no arquivo `.env`

## Configuração

### Agentes
Os agentes são definidos no arquivo `agents.yml`. O projeto inclui três agentes principais:
- Pesquisador de Mercado
- Analista de Dados
- Estrategista de Negócios

### Tarefas
As tarefas são definidas no arquivo `tasks.yml` e incluem:
- Pesquisa de mercado
- Análise de dados
- Desenvolvimento de estratégia
- Planejamento de implementação

### Configurações do Crew
As configurações gerais do crew estão no arquivo `crew.yaml`, incluindo:
- Configurações de modelo de linguagem
- Parâmetros de execução
- Configurações de logging
- Formato de saída

## Uso

1. Configure os agentes no arquivo `agents.yml`
2. Defina as tarefas no arquivo `tasks.yml`
3. Ajuste as configurações no arquivo `crew.yaml`
4. Execute o projeto

## Contribuição

Contribuições são bem-vindas! Por favor, siga estas etapas:
1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.# project_CrewAI_MCP
