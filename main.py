import streamlit as st
import httpx
from typing import List, Dict
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Streamlit
st.set_page_config(page_title="Research Buddy", page_icon="🔍")
st.title("🔍 Research Buddy")
st.caption("A web research agent powered by Mistral that finds and summarizes information")

# Constants
MAX_RESULTS = 5

def get_api_key():
    """Get API key from environment variables"""
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        st.error("""
            Mistral API key not configured. Please add it to your .env file with: `MISTRAL_API_KEY=your_key_here`
        """)
        st.stop()
    return api_key

def generate_research_summary(query: str, num_topics: int = MAX_RESULTS) -> List[Dict]:
    """Generate comprehensive research summaries on the query topic"""
    api_key = get_api_key()
    
    research_prompt = f"""
    You are a thorough research assistant helping with the query: "{query}"
    
    Please provide {num_topics} distinct aspects or subtopics related to this query.
    For each aspect/subtopic:
    1. Write a title for this aspect
    2. Write a 150-200 word summary covering the main points
    3. List 3-5 key facts or insights about this aspect
    4. Suggest 2-3 authoritative sources where one could learn more (with URLs)
    
    Return ONLY a JSON object with format:
    {{
      "topics": [
        {{
          "title": "Aspect/Subtopic Title",
          "summary": "Comprehensive summary...",
          "key_points": ["Point 1", "Point 2", ...],
          "suggested_sources": [
            {{"title": "Source Title", "url": "https://example.com", "description": "Brief description"}}
          ]
        }},
        ...
      ]
    }}
    """
    
    try:
        client = httpx.Client()
        response = client.post(
            "https://api.mistral.ai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "mistral-medium",
                "messages": [{"role": "user", "content": research_prompt}],
                "temperature": 0.3,
                "response_format": {"type": "json_object"},
            },
            timeout=60
        )
        response.raise_for_status()
        data = response.json()
        
        content = data['choices'][0]['message']['content']
        results = json.loads(content)
        return results.get("topics", [])
        
    except Exception as e:
        st.error(f"Error performing research: {e}")
        return []

def main():
    # This will automatically check for API key when the app starts
    _ = get_api_key()
    
    # User input
    query = st.text_input("Enter research topic:", placeholder="e.g., 'Effects of AI on education'")
    
    if st.button("Research") and query:
        with st.spinner("Generating comprehensive research..."):
            research_results = generate_research_summary(query)
            
        if not research_results:
            st.warning("No results generated. Try a different query.")
            return
            
        st.subheader(f"Research Results for: {query}")
        
        for i, topic in enumerate(research_results, 1):
            title = topic.get('title', f'Topic {i}')
            
            with st.expander(f"📚 {title}"):
                st.write("**Summary:**", topic.get('summary', ''))
                
                if 'key_points' in topic:
                    st.write("**Key Points:**")
                    for point in topic['key_points']:
                        st.write(f"- {point}")
                
                if 'suggested_sources' in topic:
                    st.write("**Suggested Sources:**")
                    for source in topic['suggested_sources']:
                        source_title = source.get('title', 'Untitled')
                        source_url = source.get('url', '#')
                        source_desc = source.get('description', '')
                        
                        st.markdown(f"- [{source_title}]({source_url}): {source_desc}")
        
        # Export functionality
        st.divider()
        st.subheader("Export Results")
        json_data = json.dumps({"query": query, "topics": research_results}, indent=2)
        st.download_button(
            label="Download as JSON",
            data=json_data,
            file_name=f"research_buddy_{query[:20]}.json",
            mime="application/json"
        )

if __name__ == "__main__":
    main()