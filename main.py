from crewai import Agent, Task, Crew, tool
from crewai_tools import SerperDevTool
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Ferramenta customizada
@tool("Buscador Simulado")
def search_web(query: str) -> str:
    """Realiza uma busca simulada na web para informações atualizadas."""
    return f"Resultado simulado da busca por: {query}"

# Ferramenta real de busca (opcional)
search_tool = SerperDevTool()

# Definir agente
researcher = Agent(
    role="Pesquisador",
    goal="Obter informações relevantes e atualizadas.",
    backstory="Especialista em buscas online e coleta de dados.",
    tools=[search_tool, search_web],
    llm="gpt-4o"  # Use gpt-3.5-turbo se quiser reduzir custos
)

# Definir tarefa
task = Task(
    description="Pesquisar sobre os impactos da inteligência artificial na saúde.",
    agent=researcher,
    expected_output="Um resumo claro e bem estruturado dos impactos da IA na saúde."
)

# Definir crew
crew = Crew(
    agents=[researcher],
    tasks=[task],
    verbose=True
)

# Executar
result = crew.run()
print(result)
