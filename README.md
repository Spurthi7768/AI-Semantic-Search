# AI-Semantic-Search
A webapp which can perform AI Semantic Search on the document provided by the user

## Prerequisite
Please keep the API Key for your OpenAI account handy. Instructions can be found [here](https://platform.openai.com/account/api-keys)

## Instructions to use
* Create a virtual environment in python
* Activate the virtual environment
* Install the packages from requirements.txt file
* Run the command : streamlit run app.py

## Data 
The data used is LIVING PLANET REPORT 2022 : https://wwfint.awsassets.panda.org/downloads/embargo_13_10_2022_lpr_2022_full_report_single_page_1.pdf

## Libraries
* Frontend: Streamlit
* Backend: LangChain, OpenAI and FAISS

** Note: I couldn't use PineCone due to issues in the environment for the PineCone and due to heavy traffic on the website. 
 The issue can be found [here](https://community.pinecone.io/t/receiving-403-for-all-requests-to-pinecone-http-header-error-server-envoy/1426/5)
 Hence, I decided to go with FAISS (Facebook AI Similarity Search) which is a library and works similar to a vector database and can be used for indexing.
 
 ## Demo Link
 
