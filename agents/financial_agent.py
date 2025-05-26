from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

# define yo search agent
websearch_agent = Agent(
    name = "websearch_agent",
    role = "search web for the information",
    model = Groq(id = "llama-3.1-8b-instant"),
    tools=[DuckDuckGo()],
    instructions=["always include sources"],
    show_tool_calls=True,
    markdown=True
)

#define yo financial agent
financial_agent = Agent(
    name = "financial_agent",
    model = Groq(id = "llama-3.1-8b-instant"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    show_tool_calls=True,
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
    markdown=True
)

# define the almighty ochestrator 
orchestrator_agent = Agent(
    team=[websearch_agent, financial_agent],
    model=Groq(id="llama-3.1-8b-instant"),
    instructions=["You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.Always include sources, and use table to display data"],
    show_tool_calls= True,
    markdown=True
)

orchestrator_agent.print_response("give me details about hdfc stock last week ", stream=True)

#___________________ PLEASE DON'T LAUGH LOOKING AT MY CODE __________UwU_____________#