import boto3
import json
from typing import Optional, Dict, Any
import config

class NovaClient:
    """Client for interacting with Amazon Nova models via Bedrock"""
    
    def __init__(self):
        self.bedrock_runtime = boto3.client(
            service_name='bedrock-runtime',
            region_name=config.AWS_REGION,
            aws_access_key_id=config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY
        )
    
    def generate_text(
        self, 
        prompt: str, 
        model_id: str = config.NOVA_MODEL_ID,
        max_tokens: int = 2000,
        temperature: float = 0.7,
        system_prompt: Optional[str] = None
    ) -> str:
        """Generate text using Amazon Nova model with error handling"""
        
        messages = []
        
        if system_prompt:
            messages.append({
                "role": "user",
                "content": [{"text": system_prompt}]
            })
        
        messages.append({
            "role": "user",
            "content": [{"text": prompt}]
        })
        
        request_body = {
            "messages": messages,
            "inferenceConfig": {
                "max_new_tokens": max_tokens,
                "temperature": temperature,
            }
        }
        
        try:
            response = self.bedrock_runtime.converse(
                modelId=model_id,
                messages=messages,
                inferenceConfig=request_body["inferenceConfig"]
            )
            
            return response['output']['message']['content'][0]['text']
        
        except Exception as e:
            error_msg = str(e)
            
            # Provide helpful error messages
            if "AccessDeniedException" in error_msg:
                return "⚠️ AWS Access Error: Please check your credentials and Bedrock permissions in .env file."
            elif "ResourceNotFoundException" in error_msg:
                return "⚠️ Model Access Error: Please enable Nova model access in AWS Bedrock console."
            elif "ThrottlingException" in error_msg:
                return "⚠️ Rate Limit: Too many requests. Please wait a moment and try again."
            elif "ValidationException" in error_msg:
                return f"⚠️ Invalid Request: {error_msg}"
            else:
                return f"⚠️ Error calling Nova model: {error_msg}\n\nPlease check:\n1. AWS credentials in .env\n2. Bedrock access enabled\n3. Nova model access granted"
    
    def summarize_content(self, content: str, focus: Optional[str] = None) -> str:
        """Summarize content using Nova"""
        
        system_prompt = "You are a research assistant that creates concise, accurate summaries."
        
        if focus:
            prompt = f"Summarize the following content, focusing on: {focus}\n\nContent:\n{content}"
        else:
            prompt = f"Summarize the following content:\n\n{content}"
        
        return self.generate_text(
            prompt=prompt,
            system_prompt=system_prompt,
            temperature=0.3
        )
    
    def synthesize_research(self, sources: list, query: str) -> str:
        """Synthesize information from multiple sources"""
        
        system_prompt = """You are an expert research analyst. Synthesize information from multiple sources into a comprehensive, well-structured research summary. 
        Include citations using [Source N] format. Be objective and accurate."""
        
        sources_text = "\n\n".join([
            f"Source {i+1} ({source['url']}):\n{source['content']}"
            for i, source in enumerate(sources)
        ])
        
        prompt = f"""Research Query: {query}

Sources:
{sources_text}

Please provide a comprehensive research summary that:
1. Answers the research query
2. Synthesizes information across all sources
3. Includes proper citations [Source N]
4. Highlights key findings
5. Notes any conflicting information"""
        
        return self.generate_text(
            prompt=prompt,
            system_prompt=system_prompt,
            max_tokens=3000,
            temperature=0.5
        )
    
    def answer_question(self, question: str, context: str) -> str:
        """Answer a question based on research context"""
        
        system_prompt = "You are a helpful research assistant. Answer questions accurately based on the provided context."
        
        prompt = f"""Context:
{context}

Question: {question}

Answer:"""
        
        return self.generate_text(
            prompt=prompt,
            system_prompt=system_prompt,
            temperature=0.4
        )
    
    def extract_insights(self, synthesis: str) -> str:
        """Extract key insights from research synthesis"""
        
        system_prompt = "You are an expert at identifying key insights. Extract the most important findings."
        
        prompt = f"""From the following research summary, extract 3-5 key insights or findings. 
Make each insight concise (one sentence) and impactful.

Research Summary:
{synthesis}

Key Insights (one per line):"""
        
        return self.generate_text(
            prompt=prompt,
            system_prompt=system_prompt,
            max_tokens=500,
            temperature=0.3
        )
