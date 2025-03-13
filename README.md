# AI Hedge Fund Analysis Tool

## Overview

The **AI Hedge Fund Analysis Tool** is a Python-based application that leverages language models to perform comprehensive financial analysis and trading strategy development for a given stock ticker. Built with LangChain and powered by the Perplexity API, this tool simulates a team of specialized AI agents working together to analyze market data, sentiment, macro-economic conditions, trading strategies, and risks.

### Agents
The tool consists of five sequential agents:
1. **Market Data Analyst**: Retrieves up-to-date financial data (e.g., stock price, volume, P/E ratio).
2. **Sentiment Analyst**: Analyzes news, social media, and expert commentary for market sentiment.
3. **Macro-Economic Analyst**: Evaluates broader economic indicators (e.g., GDP, inflation, interest rates).
4. **Quantitative Strategist**: Develops a trading strategy based on prior analyses.
5. **Risk Manager**: Assesses the strategy’s risks and acceptability.

The output is a detailed report covering all aspects of the analysis, printed to the console.

## Prerequisites

- Python 3.8 or higher
- [uv](https://github.com/astral-sh/uv) installed (e.g., via `pip install uv` or your package manager)
- A Perplexity API key (sign up at [Perplexity.ai](https://www.perplexity.ai) to obtain one)

## Installation

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd ai-hedge-fund-analysis
   ```

2. **Set Up a Virtual Environment with uv**:
   Create and activate a virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   The project uses a `pyproject.toml` file to manage dependencies. Sync the environment with `uv`:
   ```bash
   uv sync
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the project root and add your Perplexity API key:
   ```
   PPLX_API_KEY=your-perplexity-api-key-here
   ```

## Usage

1. **Run the Script**:
   Modify the ticker symbol in the `main()` function (e.g., `"TSLA"`) or pass a custom ticker to `run_ai_hedge_fund()`. Then execute:
   ```bash
   python script.py
   ```

2. **Example Output**:
   The tool will generate a detailed analysis like this:
   ```
   ======== AI Hedge Fund Analysis Results ========
   📈 Market Data Retrieved:
   --------------------------------------------------
   [Stock price, volume, ratios, etc.]

   📰 Market Sentiment Analysis:
   --------------------------------------------------
   [Sentiment summary, key events, trends]

   🌐 Macro-Economic Analysis:
   --------------------------------------------------
   [GDP, inflation, interest rates, etc.]

   📊 Developed Trading Strategy:
   --------------------------------------------------
   [Strategy details, entry/exit points, etc.]

   ⚠️ Risk Assessment:
   --------------------------------------------------
   [Risks and tolerance assessment]
   ==============================================
   ```

3. **Customization**:
   - Change the ticker in `run_ai_hedge_fund("YOUR_TICKER")`.

## Code Structure

- **Libraries**: Uses `langchain_core`, `langchain_community`, and `dotenv` for configuration.
- **Initialization**: Sets up the Perplexity model with an API key from `.env`.
- **Chains**: Defines five `LLMChain` instances for each agent, orchestrated via `SequentialChain`.
- **Execution**: The `run_ai_hedge_fund` function processes the ticker and displays results.

## Dependencies

Dependencies are managed in `pyproject.toml`. Here’s the relevant section:

```toml
[project]
dependencies = [
    "langchain==0.3.19",
    "langchain-community==0.3.18",
    "langchain-core==0.3.44",
    "python-dotenv"
]
```

Install them with:
```bash
uv sync
```

## Limitations

- Requires a valid Perplexity API key with sufficient quota.
- Outputs are generated based on the model’s knowledge and may not reflect real-time market data unless explicitly supported by the API.
- Designed for console output; no GUI or file export is currently implemented.

## Contributing

Feel free to fork this repository, submit issues, or create pull requests. Potential enhancements could include:
- Real-time data integration (e.g., Yahoo Finance API).
- Exporting results to CSV/PDF.
- Adding a web interface.

## License

This project is unlicensed and provided as-is for educational purposes. Use at your own risk.

## Acknowledgments

- Built with [LangChain](https://github.com/langchain-ai/langchain) and [Perplexity](https://www.perplexity.ai).
- Inspired by AI-driven financial analysis concepts.

---

### Corresponding `pyproject.toml`
Here’s the updated `pyproject.toml` without `httpx` and `ruff>=0.3.0`:

```toml
[project]
name = "ai-hedge-fund-analysis"
version = "0.1.0"
dependencies = [
    "langchain==0.3.19",
    "langchain-community==0.3.18",
    "langchain-core==0.3.44",
    "python-dotenv"
]

[tool.uv]
# Optional: Specify Python version compatibility
python = ">=3.8"
```