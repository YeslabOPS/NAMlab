import uvicorn
from file_loader import *
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

rag = RagHand()
rag.load_book(['book.index'])
pdf = "Network_Programming_with_Rust.pdf"
pdf_text = extract_text_from_pdf(pdf)
ai_client = init_ollama()

app = FastAPI()

# 数据模型
class SavePDFRequest(BaseModel):
    pdf_path: str
    faiss_index_name: str

class AskRequest(BaseModel):
    query_text: str
    book_file: str

# 功能函数
def search(query_text, book_file, top_k=5):
    query_embedding = get_text_embedding(query_text)
    distances, indices = rag.kw_index[book_file].search(query_embedding, top_k)
    return distances, indices

def generate_answer(query_text, relevant_docs):
    context = "\n".join(relevant_docs)
    prompt = f'''
    I have a exam question:\n{query_text}, 
    and you can use below info as reference:\n{context}.
    Directly give out answer with one sentence, no analysis detail.'''
    response = ai_client.chat(model=ollama_model, messages=[{"role": "user", "content": prompt}])
    return response.json()

# API部分
@app.post("/api/savepdf")
def do_save_pdf(request: SavePDFRequest):
    try:
        rag.save_pdf(request.pdf_path, request.faiss_index_name)
        return {"message": "PDF saved and FAISS index updated successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/ask")
def do_ask(request: AskRequest):
    try:
        distances, indices = search(request.query_text, request.book_file)
        relevant_docs = [pdf_text[i] for i in indices[0]]
        answer = generate_answer(request.query_text, relevant_docs)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
