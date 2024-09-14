# MindSearch with Tavily

English |[简体中文](README_zh-CN.md) 

## ✨ MindSearch with Tavily: A Powerful Deep AI Searcher

- MindSearch is an open-source AI search engine framework that can use open-source LLMs ([InternLM2.5 series models](https://huggingface.co/internlm/internlm2_5-7b-chat)), specially optimized to provide excellent performance within the MindSearch framework.
- It can use search engine APIs such as DuckDuckGo, Bing, Brave, and Google.
- This project adds the TavilySearch engine, allowing the use of the Tavily API for searches.
- Tavily has a high reputation in academia and can provide more accurate search results.

## ⚽️ Build Your Own MindSearch with Tavily

### 🐞 Local Debugging of Tavily API

- First, register a new account at https://app.tavily.com/sign-in and set up a free Tavily API Key.
- Enter the mindsearch/agent folder, open the test_tavily.py file, insert your Tavily API Key, and run the following command to test if the Tavily API is working correctly:

```bash
python test_tavily.py
```

### 🐞 Get SiliconFlow API Key

- With SiliconFlow providing free InternLM2.5-7B-Chat services, you can use the API to get services, reducing the deployment MindSearch threshold.
- To use SiliconFlow's API Key, first open https://account.siliconflow.cn/login to register a SiliconFlow account (if you have already registered, log in directly).
- After completing registration, open https://cloud.siliconflow.cn/account/ak to prepare the API Key. First, create a new API key, then click the key to copy it for future use.
- After completing registration, open https://cloud.siliconflow.cn/account/ak to prepare the API Key. First, create a new API key, then click the key to copy it for future use.

### Step 1: Install Dependencies

```bash
git clone https://githubfast.com/chenzubing/MindSearch.git
cd MindSearch
pip install -r requirements.txt
```

### Step 2: Start MindSearch API

Start the FastAPI server:

```bash
python -m mindsearch.app --lang en --model_format internlm_silicon --search_engine TavilySearch
```

- `--lang`: The language of the model, `en` for English.
- `--model_format`: The format of the model.
- `internlm_silicon` for the InternLM2.5-7B-Chat silicon server.
- `--search_engine`: The search engine.
- `TavilySearch` for the TavilySearch search engine.

### Step 3: Start MindSearch Frontend

Several frontend interfaces are provided:

- Gradio

```bash
python frontend/mindsearch_gradio.py
```

- Streamlit (recommended for more stable results)

```bash
streamlit run frontend/mindsearch_streamlit.py
```


## 📝 License

This project is released under the [Apache 2.0 License](LICENSE).

## Academic Citation

If this project has been helpful for your research, please consider citing it as follows:

```
@article{chen2024mindsearch,
  title={MindSearch: Mimicking Human Minds Elicits Deep AI Searcher},
  author={Chen, Zehui and Liu, Kuikun and Wang, Qiuchen and Liu, Jiangning and Zhang, Wenwei and Chen, Kai and Zhao, Feng},
  journal={arXiv preprint arXiv:2407.20183},
  year={2024}
}
```
