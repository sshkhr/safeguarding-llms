import urllib.request
from urllib.parse import quote
import xml.etree.ElementTree as ET
import requests

from nemoguardrails.actions import action

@action(is_system_action=True)
async def extract_key_topic(question):
    
    API_URL = "https://m8n2zftqn1ursd42.us-east-1.aws.endpoints.huggingface.cloud"
    headers = {
        "Accept" : "application/json",
        "Content-Type": "application/json" 
    }

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": "Question: What is the key query topic in this question in under 5 words? Context: {}".format(question),
        "parameters": {}
    })

    return output[0]['generated_text']


@action(is_system_action=True)
async def fetch_arxiv_papers(query):
    base_url = 'http://export.arxiv.org/api/query?'
    query_params = {
        'search_query': 'all:' + quote(query),
        'start': 0,
        'max_results': 10
    }
    
    # Construct the full URL with encoded parameters
    url = base_url + urllib.parse.urlencode(query_params)
    
    # Fetch data from the URL
    try:
        with urllib.request.urlopen(url) as f:
            response = f.read().decode('utf-8')
            
            # Parse XML response
            root = ET.fromstring(response)
            
            papers_text = ""
            
            # Iterate over each entry (paper)
            for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
                title = entry.find('{http://www.w3.org/2005/Atom}title').text
                published = entry.find('{http://www.w3.org/2005/Atom}published').text
                author = entry.find('{http://www.w3.org/2005/Atom}author/{http://www.w3.org/2005/Atom}name').text
                
                # Extracting the year from published date
                year = published[:4]
                
                # Format paper information as plain text
                paper_info = f"Title: {title}\nYear: {year}\nFirst Author: {author}\n\n"
                
                # Append to the papers_text
                papers_text += paper_info
            return papers_text
    except urllib.error.URLError as e:
        print(f"Error fetching data from Arxiv API: {e}")
        return None