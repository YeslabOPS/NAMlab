import uvicorn
from file_loader import *
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# 初始化RAG系统
rag = RagHand()
app = FastAPI()

# 初始化AI客户端
ai_client, ai_model = choice_ai(use_deepseek=True)

# 核心功能函数
def search(query_text, book_file, top_k):
    """在FAISS索引中搜索与查询最相关的文档片段
    
    Args:
        query_text: 查询文本
        book_file: FAISS索引文件名
        top_k: 返回前k个最相关的结果
    
    Returns:
        tuple: (distances, indices) 相似度距离和对应的文档索引
    """
    query_embedding = get_text_embedding(query_text)
    distances, indices = rag.kw_index[book_file].search(query_embedding, top_k)
    return distances, indices

def generate_answer(query_text, relevant_docs):
    """基于相关文档生成答案
    
    Args:
        query_text: 用户的问题
        relevant_docs: 相关的文档片段列表
    
    Returns:
        str: AI生成的答案
    """
    context = "\n".join(relevant_docs)
    prompt = f'''
    See below info as reference:\n{context}.
    Please answer the question:\n{query_text}.'''
    response = ai_client.chat(model=ollama_model, messages=[{"role": "user", "content": prompt}])
    return response.message.content

# 定义请求数据模型
class SavePDFRequest(BaseModel):
    """保存PDF文件的请求模型
    
    Attributes:
        pdf_path: PDF文件的路径
        faiss_index_name: FAISS索引文件的名称
    """
    pdf_path: str
    faiss_index_name: str

class AskRequest(BaseModel):
    """问答请求的数据模型
    
    Attributes:
        query_text: 用户的问题文本
        faiss_index_name: 要查询的FAISS索引文件名
        top_k: 返回最相关的前k个文档片段，默认为3
    """
    query_text: str
    faiss_index_name: str
    top_k: int = 3  

# API端点定义
@app.post("/api/savepdf")
def do_save_pdf(request: SavePDFRequest):
    """处理PDF保存请求的API端点
    
    将PDF文件处理并保存为FAISS索引
    """
    try:
        rag.save_pdf(request.pdf_path, request.faiss_index_name)
        return {"message": "PDF saved and FAISS index updated successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/ask")
def do_ask(request: AskRequest):
    """处理问答请求的API端点
    
    基于用户问题，检索相关文档并生成答案
    """
    try:
        # 重置数据库状态
        rag.new_db()
        rag.load_book([request.book_file])

        # 获取PDF文本内容
        pdf = request.faiss_index_name.split('.')[0] + '.pdf'
        pdf_text = extract_text_from_pdf(pdf)

        # 执行相似度搜索
        distances, indices = search(request.query_text, request.faiss_index_name, request.top_k)
        relevant_docs = [pdf_text[i] for i in indices[0]]

        # 生成并返回答案
        answer = generate_answer(request.query_text, relevant_docs)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
