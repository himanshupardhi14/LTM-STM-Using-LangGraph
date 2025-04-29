
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langgraph.graph import StateGraph
from typing import TypedDict
import os 

os.environ["GOOGLE_API_KEY"] = "Insert your API key here"  

#  Initialize LLM (Gemini) 
llm = GoogleGenerativeAI(model="gemini-2.0-flash")  

# Initialize Short-Term Memory 
short_term_memory = ConversationBufferMemory(memory_key="chat_history")

# Initialize Long-Term Memory (VectorStore) 
embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Dummy init for FAISS
vectorstore = FAISS.from_texts(
    texts=["initial dummy memory"],
    embedding=embedding_model
)

# Define Graph State Schema 
class GraphState(TypedDict):
    chat_history: str  # Storing conversation history

#  Create LangGraph 
graph = StateGraph(GraphState)

#  Define Node Functions 

# Short-term memory node (enhanced with retrieval)
def short_term_memory_node(state: GraphState) -> GraphState:
    user_input = state.get("chat_history", "")
    
    if not user_input.strip():
        user_input = "Heyy! How can I assist you today?"
    
    # Retrieve related memories from FAISS
    retrieved_docs = vectorstore.similarity_search(user_input, k=3)  
    retrieved_memory = "\n".join([doc.page_content for doc in retrieved_docs])
    
    if retrieved_memory:
        prompt = f"Previously, these were discussed:\n{retrieved_memory}\nNow, user says: {user_input}"
    else:
        prompt = f"User says: {user_input}"
    
    # Get response from Gemini
    response = llm.invoke(prompt)
    
    # Save to short-term memory
    short_term_memory.save_context({"input": user_input}, {"output": response})
    
    # Save to long-term memory (vector db)
    vectorstore.add_texts([f"User: {user_input}\nBot: {response}"])
    
    # Load updated short-term memory
    updated_history = short_term_memory.load_memory_variables({})["chat_history"]
    
    return {"chat_history": updated_history}

# Dummy long-term node (not needed much now, handled inside)
def long_term_memory_node(state: GraphState) -> GraphState:
    return state

#  Add Nodes 
graph.add_node("short_term_memory", short_term_memory_node)
graph.add_node("long_term_memory", long_term_memory_node)

#  Define Edges 
graph.set_entry_point("short_term_memory")
graph.add_edge("short_term_memory", "long_term_memory")

#  Compile 
runnable_graph = graph.compile()

#  Run 
conversations = [
    {"chat_history": "Hi, I have a pet cat."},
    {"chat_history": "Tell me an interesting fact about cats."},
    {"chat_history": "What did I tell you about my pet 2 minutes ago?"}
]

for idx, conv in enumerate(conversations):
    print(f"\n--- Step {idx+1}--- ")
    output = runnable_graph.invoke(conv)
    print(output)
