openai_key= "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"

from typing import List
from langchain.embeddings.base import Embeddings
import openai
openai.api_key = openai_key
import json
class MyEmbedding(Embeddings):
    

    #engine = "text-embedding-ada-002"

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        response = openai.Embedding.create(input=texts,model="text-embedding-ada-002")
        
        json_response = {
            "result" : json.dumps(response["data"])
            }
        result = json.loads(json_response["result"])        
        embeddings : list[list[float]] = [data["embedding"] for data in result]
        print("embeddings done")
        return embeddings
        """Embed search docs."""
       

    def embed_query(self, text: str) -> List[float]:
        response = openai.Embedding.create(input=text,model="text-embedding-ada-002")
        json_response = {
            "result" : json.dumps(response["data"])
            }
        result = json.loads(json_response["result"])        
        embeddings : list[list[float]] = [data["embedding"] for data in result]
        print("equery mbeddings done")
        """Embed query text."""
        return embeddings[0]