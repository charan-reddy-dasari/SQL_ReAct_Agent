
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_agent

from sqlalchemy.exc import SQLAlchemyError
from openai import AuthenticationError, RateLimitError, APIConnectionError

load_dotenv()


def initialize_agent():

    try:
        # Database connection
        db = SQLDatabase.from_uri("sqlite:///employees.db")

        # Initialize LLM
        llm = ChatOpenAI(
            model="gpt-4.1-mini",
            temperature=0
        )

        # SQL Toolkit
        toolkit = SQLDatabaseToolkit(
            db=db,
            llm=llm
        )

        tools = toolkit.get_tools()

        system_prompt = """
        You are an intelligent SQL database assistant.

        Instructions:
        1. Inspect available tables.
        2. Inspect relevant schemas.
        3. Generate SQL queries.
        4. Execute queries using available tools.
        5. Correct SQL errors when necessary.
        6. Never invent database information.
        7. Only execute read-only SQL queries.
        8. Return clear and concise answers.
        """

        agent = create_agent(
            model=llm,
            tools=tools,
            system_prompt=system_prompt
        )

        return agent

    except SQLAlchemyError as e:
        raise RuntimeError(f"Database initialization failed: {e}") from e

    except AuthenticationError as e:
        raise RuntimeError("Invalid OpenAI API key. Check your .env file.") from e

    except RateLimitError as e:
        raise RuntimeError("OpenAI API rate limit exceeded.") from e

    except APIConnectionError as e:
        raise RuntimeError("Unable to connect to OpenAI API.") from e

    except Exception as e:
        raise RuntimeError(f"Agent initialization failed: {e}") from e


def ask_agent(agent, question):

    try:
        response = agent.invoke(
            {
                "messages": [
                    {"role": "user", "content": question}
                ]
            }
        )

        return response["messages"][-1].content

    except AuthenticationError as e:
        raise RuntimeError("OpenAI authentication failed. Check your API key.") from e

    except RateLimitError as e:
        raise RuntimeError("OpenAI rate limit exceeded. Please try again later.") from e

    except APIConnectionError as e:
        raise RuntimeError("Unable to connect to OpenAI.") from e

    except SQLAlchemyError as e:
        raise RuntimeError("A database error occurred.") from e

    except Exception as e:
        raise RuntimeError(f"Unable to process your question: {e}") from e
