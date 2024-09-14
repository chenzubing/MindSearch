# MindSearch with Tavily
简体中文 |[English](README.md) 



## ✨ MindSearch with Tavily: a Powerful Deep AI Searcher

- MindSearch 是一个开源的 AI 搜索引擎框架，可以使用开源 LLM（[InternLM2.5 系列模型](https://huggingface.co/internlm/internlm2_5-7b-chat)），经过专门优化，能够在 MindSearch 框架中提供卓越的性能。
- 可以使用DuckDuckGo、Bing、Brave和Google等搜索引擎API
- 本项目在这里增加了TavilySearch搜索引擎，可以使用Tavily API来进行搜索
- Tavily在学术界有很高的声誉，可以提供更加准确的搜索结果


## ⚽️ 构建您自己的 MindSearch with Tavily

### 🐞 本地调试Tavily Api

- 首先到 https://app.tavily.com/sign-in 注册新账号， 设置好免费的 Tavily Api Key,
- 进入mindsearch/agent文件夹,打开test_tavily.py 文件，将Tavily Api Key 填入，运行以下命令测试Tavily Api是否正常

```bash
python test_tavily.py
```

### 🐞 获取硅基流动 API Key

- 随着硅基流动提供了免费的 InternLM2.5-7B-Chat 服务，可以通过API的方式来获取服务，降低了部署MindSearch 门槛。
- 要使用硅基流动的 API Key，首先打开 https://account.siliconflow.cn/login 来注册硅基流动的账号（如果注册过，则直接登录即可）。

- 在完成注册后，打开 https://cloud.siliconflow.cn/account/ak 来准备 API Key。首先创建新 API 密钥，然后点击密钥进行复制，以备后续使用。

### 步骤1: 依赖安装

```bash
git clone https://githubfast.com/chenzubing/MindSearch.git
cd MindSearch
pip install -r requirements.txt
```

### 步骤2: 启动 MindSearch API

启动 FastAPI 服务器

```bash
python -m mindsearch.app --lang en --model_format internlm_silicon --search_engine TavilySearch
```

- `--lang`: 模型的语言，`en` 为英语。
- `--model_format`: 模型的格式。
  - `internlm_silicon` 为 InternLM2.5-7b-chat 本地服务器。
  - `--search_engine`: 搜索引擎。
  - `TavilySearch` 为 TavilySearch 搜索引擎。
  
 
### 步骤3: 启动 MindSearch 前端

提供以下几种前端界面：

- Gradio

```bash
python frontend/mindsearch_gradio.py
```

- Streamlit 提供较稳定的结果，推荐使用

```bash
streamlit run frontend/mindsearch_streamlit.py
```



## 📝 许可证

该项目按照 [Apache 2.0 许可证](LICENSE) 发行。

## 学术引用

如果此项目对您的研究有帮助，请参考如下方式进行引用：

```
@article{chen2024mindsearch,
  title={MindSearch: Mimicking Human Minds Elicits Deep AI Searcher},
  author={Chen, Zehui and Liu, Kuikun and Wang, Qiuchen and Liu, Jiangning and Zhang, Wenwei and Chen, Kai and Zhao, Feng},
  journal={arXiv preprint arXiv:2407.20183},
  year={2024}
}
```