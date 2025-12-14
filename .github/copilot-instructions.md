# Copilot Instructions for MATIČÁK Chatbot Codebase

## Project Overview
- **Purpose:** School chatbot for Matiční gymnázium Ostrava, with RAG-based AI, contact info, menu scraping, and modern UI.
- **Main Components:**
  - `app/core/`: Data management, orchestration, rule-based logic
  - `app/llm/`: LLM client integration
  - `app/rag/`: Embeddings, indexing, retrieval for RAG
  - `app/jidelna/`, `app/kontakty/`, `app/rozvrh/`: Scrapers and info modules
  - `app/ui/`: Frontend HTML/JS for chat widget
  - `web-integration/`, `docs/`, `wordpress-plugin/`: Deployment and integration targets

## Key Workflows
- **Local Development:**
  - Activate venv: `source .venv/bin/activate`
  - Start backend: `uvicorn main:app --reload --port 8000`
  - Open UI: `open app/ui/chat.html`
- **Testing:**
  - Run tests: `pytest` or `python -m unittest discover`
  - Test scripts: see `scripts/README.md` for PDF/data extraction
- **Deployment:**
  - GitHub Pages: see `GITHUB_PAGES_QUICKSTART.md`, use `./deploy_to_pages.sh`
  - Backend: see `DEPLOYMENT.md`, use `deploy_backend.sh` or `deploy_complete.sh`

## Project Conventions
- **Data:**
  - Documents for RAG in `data/documents/`, organized by topic
  - Scrapers output to `data/skolni_data.json` and related files
- **Frontend:**
  - Chat widget JS: `app/ui/config.js`, `app/ui/chat.html`, `web-integration/chatbot-widget.js`
  - For web/WordPress integration, copy widget files as described in respective READMEs
- **Backend:**
  - Main entry: `main.py` (FastAPI/Uvicorn)
  - Modular logic: each domain (contacts, menu, schedule) in its own subpackage
  - RAG pipeline: `app/rag/` for embeddings/indexing, `app/llm/` for LLM calls

## Patterns & Integration
- **RAG System:**
  - Documents ingested from `data/documents/`, indexed via `app/rag/indexer.py`
  - Retrieval and embedding logic in `app/rag/` and `app/llm/`
- **Scraping:**
  - Each info type (contacts, menu, schedule) has a dedicated scraper in its submodule
- **Deployment:**
  - Static frontend for GitHub Pages in `docs/`
  - Backend can be deployed separately for full AI features

## Examples
- To add a new data source, create a new submodule in `app/`, add a scraper, and update data outputs.
- To update chatbot UI, edit `app/ui/chat.html` and sync to `docs/chat.html` for deployment.

## References
- See `README.md` (root), `docs/README.md`, and `scripts/README.md` for more details.
- For integration, see `web-integration/README.md` and `wordpress-plugin/README.md`.

---

*Update this file if project structure or workflows change. Focus on actionable, codebase-specific guidance for AI agents.*
