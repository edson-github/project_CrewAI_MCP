from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente
load_dotenv()

# Ferramentas disponíveis
search_tool = DuckDuckGoSearchRun()

# Criação dos agentes especializados em análise de startups
startup_researcher = Agent(
    role="Pesquisador de Mercado de Startups",
    goal="Analisar o ecossistema de startups e identificar tendências promissoras",
    backstory="""Especialista em pesquisa de mercado com foco em startups e inovação. 
    Possui experiência em identificar tendências emergentes e avaliar potencial de mercado.""",
    verbose=True,
    allow_delegation=True,
    tools=[search_tool]
)

startup_analyst = Agent(
    role="Analista de Dados de Startups",
    goal="Avaliar métricas e indicadores de performance de startups",
    backstory="""Analista especializado em métricas de startups e venture capital. 
    Experiente em análise de KPIs, valuation e potencial de crescimento.""",
    verbose=True,
    allow_delegation=True
)

startup_advisor = Agent(
    role="Consultor Estratégico de Startups",
    goal="Desenvolver recomendações estratégicas para startups",
    backstory="""Consultor experiente em desenvolvimento de startups. 
    Especialista em estratégias de crescimento, captação de recursos e posicionamento de mercado.""",
    verbose=True,
    allow_delegation=True
)

# Tarefas específicas para análise de startups
market_research_task = Task(
    description="""Realize uma análise do ecossistema de startups:
    1. Identifique setores mais promissores
    2. Analise tendências de investimento
    3. Avalie o cenário competitivo
    4. Identifique oportunidades inexploradas""",
    agent=startup_researcher,
    expected_output="Relatório detalhado sobre o ecossistema de startups e oportunidades"
)

metrics_analysis_task = Task(
    description="""Analise as métricas-chave de startups bem-sucedidas:
    1. Avalie indicadores de crescimento
    2. Analise métricas de captação
    3. Compare modelos de receita
    4. Identifique fatores de sucesso""",
    agent=startup_analyst,
    expected_output="Análise aprofundada de métricas e indicadores de sucesso"
)

strategy_task = Task(
    description="""Desenvolva recomendações estratégicas:
    1. Crie estratégias de entrada no mercado
    2. Sugira modelos de monetização
    3. Proponha estratégias de crescimento
    4. Identifique potenciais riscos e mitigações""",
    agent=startup_advisor,
    expected_output="Plano estratégico detalhado com recomendações práticas"
)

# Criação do crew especializado em startups
startup_crew = Crew(
    agents=[startup_researcher, startup_analyst, startup_advisor],
    tasks=[market_research_task, metrics_analysis_task, strategy_task],
    verbose=2,
    process=Process.sequential
)

# Execução do crew
result = startup_crew.kickoff()

# Salva o resultado
os.makedirs("outputs", exist_ok=True)
with open("outputs/analise_startups.md", "w") as f:
    f.write(result)

print("\nAnálise de startups completa! Resultados salvos em outputs/analise_startups.md")