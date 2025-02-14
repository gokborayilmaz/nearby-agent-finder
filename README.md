# 📍 Nearby Event Finder Agent - Day 18/21

This agent is part of the **Everyday New AI Agent** series - **Day 18/21** 🚀

## 📌 Overview

The **Nearby Event Finder Agent** allows users to find upcoming events in a specified city for a given date using **Google Maps MCP**.

### 🔹 Features:

- 📍 Retrieves event listings for a specified **city** and **date**.
- 🎭 Shows event **name, location, and category**.
- 🗺️ Uses **Google Maps MCP** to fetch relevant data.
- ✅ Simple UI for easy event lookup.

---

## 🛠️ Installation & Setup

### **Prerequisites**

- Python 3.9 or higher
- Git
- Virtual environment (recommended)
- **Google Maps API Key** (for MCP authentication)

### **Installation**

1️⃣ Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

2️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

3️⃣ Set up your environment variables:
Create a `.env` file in the root directory and configure it as follows:

```env
GOOGLE_MAPS_API_KEY="your_google_maps_api_key"
AZURE_OPENAI_ENDPOINT="your_azure_openai_endpoint"
AZURE_OPENAI_API_VERSION="your_azure_openai_api_version"
AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
```

---

## 🚀 Running the Application

Start the FastAPI server:

```bash
uvicorn upsonicai:app --reload
```

Open the UI in your browser:

```
http://127.0.0.1:8000/
```

---

## 🔗 API Endpoints

### **1️⃣ Find Events in a City**

- **Endpoint:** `GET /find_events`
- **Query Parameters:**
  - `city` (string) - The city where you want to find events.
  - `date` (string) - The date for the event search (format: YYYY-MM-DD).
- **Example Usage:**

```bash
curl "http://127.0.0.1:8000/find_events?city=New York&date=2025-06-15"
```

- **Response:**

```json
{
  "events": [
    {
      "name": "Jazz Festival 2025",
      "location": "Central Park, New York",
      "date": "2025-06-15",
      "category": "Music"
    }
  ]
}
```

---

🔗 **Explore More:** [GitHub Repository](https://github.com/your-repo-url)

🚀 **UpsonicAI - Making AI Agents Simple & Scalable!**

