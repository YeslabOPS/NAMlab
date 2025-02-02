import fitz  # PyMuPDF
import faiss
import ollama
import numpy as np
from tqdm import tqdm

# Ollama配置常量
ollama_url = 'http://192.168.0.150:11434'
ollama_model = 'llama3.2:3b'
llama3_2_vec_len = 3072  # llama3.2模型的向量维度

# Deepseek配置常量
deepseek_url = 'https://api.deepseek.com'
deepseek_token = 'sk-925cb978631646fd8b315bde217e46d9'
deepseek_model = 'deepseek-chat'

def init_ollama():
    """初始化Ollama客户端
    
    Returns:
        ollama.Client: 配置好的Ollama客户端实例
    """
    client = ollama.Client(
        host=ollama_url,
        headers={'x-some-header': 'some-value'}
    )
    model = ollama_model
    return client, model

def init_deepseek():
    """初始化Deepseek客户端
    
    Returns:
        ollama.Client: 配置好的Deepseek客户端实例
    """
    client = ollama.Client(
        host=deepseek_url,
        headers={
            'Authorization': f'Bearer {deepseek_token}',
            'Content-Type': 'application/json'
        }
    )
    model = deepseek_model
    return client, model

def choice_ai(use_deepseek: bool = False):
    if use_deepseek:
        return init_deepseek()
    else:
        return init_ollama()  

def extract_text_from_pdf(pdf_path, all_imgs=False):
    """从PDF文件中提取文本内容
    
    Args:
        pdf_path: PDF文件路径
    
    Returns:
        list: 每页文本内容的列表
    """
    doc = fitz.open(pdf_path)
    text_list = []
    for page in doc:
        page = page.get_text().strip()
        if page != '':
            text_list.append(page)
    return text_list

def get_text_embedding(text, client, model):
    """获取文本的向量嵌入表示
    
    Args:
        text: 输入文本
        use_deepseek: 是否使用Deepseek模型（默认False，使用Ollama）
    
    Returns:
        np.array: 文本的向量嵌入
    """ 
    response = client.embed(model=model, input=text)
    return np.array(response['embeddings'], dtype=np.float32)


class RagHand:
    """RAG（检索增强生成）系统的核心处理类
    处理PDF文档的向量化存储和检索功能
    """
    
    def __init__(self):
        """初始化RAG处理器，创建空的索引字典和数据库"""
        self.kw_index = {}
        self.new_db()

    def new_db(self):
        """创建新的FAISS索引实例"""
        self.index = faiss.IndexFlatL2(llama3_2_vec_len)

    def save_pdf(self, pdf_path, file_name):
        """处理PDF文件并保存为FAISS索引
        
        Args:
            pdf_path: PDF文件路径
            file_name: 保存的索引文件名
        """
        pdf_text = extract_text_from_pdf(pdf_path)
        embeddings = []
        seg_num = 0

        # 使用tqdm显示处理进度
        segments = [seg for seg in pdf_text]
        for seg in tqdm(segments, desc="Processing PDF to Faiss Index: "):
            embedding = get_text_embedding(seg).flatten()
            seg_num += 1
            embeddings.append(embedding)

        # 批量添加向量到索引以提高效率
        embed_matrix = np.array(embeddings, dtype=np.float32)
        self.index.add(embed_matrix)
        faiss.write_index(self.index, file_name)

    def load_book(self, book_list):
        """加载FAISS索引文件
        
        Args:
            book_list: 索引文件路径列表
        """
        for book in book_list:
            self.kw_index[book] = faiss.read_index(book)

