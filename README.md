# dramacool-scraper

A lightweight Flask API that scrapes drama listings from `asianc.to` and returns JSON responses.

## Codebase overview

Project structure:

- `main.py`  
  Flask app entrypoint, route definitions, and response caching.
- `src/popular.py`  
  Scraper for most-popular drama pages.
- `src/recent.py`  
  Scraper for recently-added dramas.
- `requirements.txt`  
  Python dependencies.
- `vercel.json`  
  Vercel deployment configuration.

## Tech stack

- Python
- Flask
- Flask-Caching (simple in-memory cache, 5-minute endpoint cache)
- Requests
- BeautifulSoup4

## Setup and run

1. Create and activate a virtual environment (recommended).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the API locally:

```bash
python main.py
```

By default, Flask runs on `http://127.0.0.1:5000`.

## API endpoints

Base URL (local): `http://127.0.0.1:5000`

### 1) `GET /`

Health/welcome endpoint.

**Example response**

```json
{
  "message": "Welcome message"
}
```

---

### 2) `GET /popular`

Returns popular drama items from:
`https://asianc.to/most-popular-drama?page={page}`

**Query params**

- `page` (optional): page number as string/integer.  
  Default: `1`.

**Response shape**

```json
{
  "page": "recent",
  "currentPage": "1",
  "status": 200,
  "error": null,
  "results": [
    {
      "id": "/drama-detail/...",
      "title": "...",
      "image": "https://..."
    }
  ]
}
```

**Notes**

- Endpoint response is cached for 300 seconds.
- On request/scrape failure, `error` is populated and `results` may be empty.

---

### 3) `GET /recent`

Returns recently added drama items from:
`https://asianc.to/recently-added`

**Response shape**

```json
{
  "page": "popular",
  "status": 200,
  "error": null,
  "results": [
    {
      "title": "...",
      "image": "https://...",
      "id": "/drama-detail/..."
    }
  ]
}
```

**Notes**

- Endpoint response is cached for 300 seconds.
- On request/scrape failure, `error` is populated and `results` may be empty.
- Note: current implementation in `src/recent.py` sets `page` to `"popular"`, which may differ from the expected `"recent"` label.

## Deployment

`vercel.json` is configured to serve `main.py` via `@vercel/python`, routing all paths to the Flask app.
