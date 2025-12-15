# Elasticsearch Cookbook

This repository contains training exercises and practical examples for learning Elasticsearch.

## Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) - Fast Python package manager
- Docker and Docker Compose (for running Elasticsearch cluster)

## Setup

### 1. Install uv

If you don't have `uv` installed, you can install it with:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or using pip:

```bash
pip install uv
```

### 2. Install Dependencies

Using uv, install the project dependencies:

```bash
uv sync
```

This will create a virtual environment and install all required packages (elasticsearch and jupyterlab).

### 3. Start Elasticsearch Cluster

Start the Elasticsearch cluster using Docker Compose:

```bash
docker-compose up -d
```

Or for a 2-node cluster:

```bash
docker-compose -f docker-compose-2-nodes.yml up -d
```

Or for a 1-node cluster:

```bash
docker-compose -f docker-compose-1-nodes.yml up -d
```

Verify that Elasticsearch is running on `https://localhost:9200`:

```bash
curl https://localhost:9200
```

Optional: install Chrome extension **Elasticvue** (https://chromewebstore.google.com/detail/elasticvue/hkedbapjpblbodpgbajblpnlpenaebaa)

### 4. Launch JupyterLab

Start JupyterLab:

```bash
uv run jupyter lab
```

Or activate the virtual environment first:

```bash
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate  # On Windows

jupyter lab
```

## Contents

- **ES_TD1.ipynb**: First training exercise notebook
- **ES_TD2.ipynb**: Second training exercise notebook
- **ES_TD1.postman_collection.json**: Postman collection for ES_TD1
- **ES_TD2.postman_collection.json**: Postman collection for ES_TD2
- **docker-compose.yml**: Single-node Elasticsearch cluster configuration
- **docker-compose-2-nodes.yml**: Two-node Elasticsearch cluster configuration

## Usage

1. Open the Jupyter notebooks in JupyterLab
2. Make sure your Elasticsearch cluster is running
3. Follow the exercises in the notebooks

The notebooks connect to Elasticsearch at `http://localhost:9200` by default.

## Stopping the Cluster

To stop the Elasticsearch cluster:

```bash
docker-compose down
```

Or for the 2-node cluster:

```bash
docker-compose -f docker-compose-2-nodes.yml down
```

