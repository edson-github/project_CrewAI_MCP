from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente
load_dotenv()

# Ferramentas disponíveis
search_tool = DuckDuckGoSearchRun()

# Criação dos agentes especializados em IA
ai_researcher = Agent(
    role="Pesquisador de Mercado de IA",
    goal="Analisar tendências e oportunidades no mercado de Inteligência Artificial",
    backstory="""Especialista em pesquisa de mercado com foco em tecnologias emergentes e IA. 
    Possui vasta experiência em identificar tendências tecnológicas e seu impacto nos negócios.""",
    verbose=True,
    allow_delegation=True,
    tools=[search_tool]
)

ai_analyst = Agent(
    role="Analista de Dados de IA",
    goal="Processar e interpretar dados sobre o mercado de IA",
    backstory="""Analista especializado em métricas de mercado de tecnologia e IA. 
    Experiente em identificar padrões e insights em dados complexos do setor tecnológico.""",
    verbose=True,
    allow_delegation=True
)

ai_strategist = Agent(
    role="Estrategista de Negócios em IA",
    goal="Desenvolver estratégias para aproveitamento de oportunidades em IA",
    backstory="""Estrategista com profundo conhecimento em implementação de soluções de IA. 
    Especialista em identificar oportunidades de negócios e criar planos de ação efetivos.""",
    verbose=True,
    allow_delegation=True
)

# Tarefas específicas para análise do mercado de IA
market_research_task = Task(
    description="""Realize uma pesquisa abrangente sobre o mercado atual de IA:
    1. Identifique as principais tendências em IA para 2024
    2. Analise os principais players do mercado
    3. Identifique nichos emergentes e oportunidades
    4. Avalie o impacto da IA generativa no mercado""",
    agent=ai_researcher,
    expected_output="Relatório detalhado sobre o estado atual e tendências do mercado de IA"
)

data_analysis_task = Task(
    description="""Analise os dados coletados sobre o mercado de IA:
    1. Avalie o tamanho do mercado e projeções de crescimento
    2. Identifique setores com maior adoção de IA
    3. Analise investimentos e financiamentos em IA
    4. Compare diferentes segmentos do mercado de IA""",
    agent=ai_analyst,
    expected_output="Análise quantitativa e qualitativa do mercado de IA com insights principais"
)

strategy_task = Task(
    description="""Desenvolva uma estratégia baseada nas análises:
    1. Identifique oportunidades prioritárias
    2. Avalie riscos e desafios
    3. Proponha abordagens de diferenciação
    4. Sugira modelos de negócios viáveis""",
    agent=ai_strategist,
    expected_output="Estratégia detalhada para exploração do mercado de IA"
)

# Criação do crew especializado em IA
ai_crew = Crew(
    agents=[ai_researcher, ai_analyst, ai_strategist],
    tasks=[market_research_task, data_analysis_task, strategy_task],
    verbose=2,
    process=Process.sequential
)

# Execução do crew
result = ai_crew.kickoff()

# Salva o resultado
os.makedirs("outputs", exist_ok=True)
with open("outputs/analise_mercado_ia.md", "w") as f:
    f.write(result)

print("\nAnálise do mercado de IA completa! Resultados salvos em outputs/analise_mercado_ia.md")