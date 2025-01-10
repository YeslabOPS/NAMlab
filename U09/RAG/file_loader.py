import fitz  # PyMuPDF
import faiss
import ollama
import numpy as np
from tqdm import tqdm

ollama_url = 'http://localhost:11434'
ollama_model = 'llama3.2:3b'
llama3_2_vec_len = 3072

def init_ollama():
    client = ollama.Client(
        host=ollama_url,
        headers={'x-some-header': 'some-value'}
    )
    return client

def extract_text_from_pdf(pdf_path, all_imgs=False):
    doc = fitz.open(pdf_path)
    text_list = []
    for page in doc:
        if all_imgs:
            page = get_ocr(page)
        else:
            page = page.get_text().strip()
        if page != '':
            text_list.append(page)
    return text_list

def get_text_embedding(text):
    ollama_client = init_ollama()
    response = ollama_client.embed(model=ollama_model, input=text)
    return np.array(response['embeddings'], dtype=np.float32)


class RagHand:
    def __init__(self):
        self.index = faiss.IndexFlatL2(llama3_2_vec_len)
        self.kw_index = {}

    def save_pdf(self, pdf_path, file_name):
        pdf_text = extract_text_from_pdf(pdf_path)
        embeddings = []
        seg_num = 0

        # 分段处理时添加 tqdm 进度条
        segments = [seg for seg in pdf_text]
        for seg in tqdm(segments, desc="Processing PDF to Faiss Index: "):
            embedding = get_text_embedding(seg).flatten()
            seg_num += 1
            embeddings.append(embedding)

        # 将嵌入一次性添加到索引中，减少运行时间
        embed_matrix = np.array(embeddings, dtype=np.float32)
        self.index.add(embed_matrix)
        faiss.write_index(self.index, file_name)

    def load_book(self, book_list):
        for book in book_list:
            self.kw_index[book] = faiss.read_index(book)

