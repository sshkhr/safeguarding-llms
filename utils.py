import urllib.request
from urllib.parse import quote
import xml.etree.ElementTree as ET
from openai import OpenAI
import os
from dotenv import load_dotenv


def extract_key_topic():
    load_dotenv()

    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "You are a helpful assistant that extracts key topics from sentences."},
        {"role": "user", "content": "What are some latest papers on key value caching in machine learning?"}, # TODO: Extract user message from Colang and pass to function
        {"role": "assistant", "content": "Give me ONLY the name of the research topic from this sentence (just the named entity, strictly under 5 words):"}
    ])

    return response.choices[0].message.content


# Example usage
# sentence = "What are some latest papers on key value caching?"
# key_topic = extract_key_topic(sentence)
# print(key_topic)


def fetch_arxiv_papers(query):
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


# Example usage:
# query = 'KV caching'
# papers = fetch_arxiv_papers(query)
# if papers:
#     print(papers)
