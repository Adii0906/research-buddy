# 🔍 Research Buddy

A streamlined web research agent powered by Mistral AI that automatically finds, retrieves, and summarizes information from relevant sources based on your research queries.

## 🌟 Features

- **Intelligent Source Discovery**: Identifies the most relevant and authoritative websites for your research topic
- **Automated Content Analysis**: Fetches and processes webpage content to extract meaningful insights
- **Query-Focused Summaries**: Generates concise summaries specifically tailored to your research question
- **Key Points Extraction**: Distills the most important information into easily digestible bullet points
- **Proper Citations**: Automatically formats source citations for academic use
- **Export Functionality**: Download all research results as JSON for future reference

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Mistral AI API key ([Sign up here](https://console.mistral.ai/))

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Adii0906/research-buddy.git
cd research-buddy
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your Mistral API key:
```
MISTRAL_API_KEY=your_api_key_here
```

### Usage

1. Start the Streamlit app:
```bash
streamlit run main.py
```

2. Access the app in your browser at `http://localhost:8501`

3. Enter your research topic and click "Research"

4. Review the generated summaries and key points from each source

5. Download your research results using the "Download as JSON" button

## 📋 Project Structure

```
research-buddy/
├── main.py           # Main application code
├── requirements.txt  # Project dependencies
├── .env              # Environment variables (API keys)
└── README.md         # Project documentation
```

## 📦 Dependencies

- streamlit: Web application framework
- httpx: HTTP client for making API requests
- python-dotenv: Environment variable management
- mistralai: API integration with Mistral AI

## 🔧 Configuration

- `SUMMARY_LENGTH`: Control the length of generated summaries (default: 150 words)
- `MAX_RESULTS`: Number of sources to retrieve per query (default: 3)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [Mistral AI](https://mistral.ai/) for providing the AI capabilities
- [Streamlit](https://streamlit.io/) for the web app framework
