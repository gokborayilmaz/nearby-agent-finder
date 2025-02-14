import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
from upsonic import Agent, Task, ObjectResponse

# Load environment variables
load_dotenv()

app = FastAPI(title="Nearby Event Finder Agent")

# Initialize the AI agent
event_finder_agent = Agent("Nearby Event Finder Agent", model="azure/gpt-4o")

# Define Google Maps MCP
class GoogleMapsMCP:
    command = "npx"
    args = ["-y", "@modelcontextprotocol/server-google-maps"]
    env = {"GOOGLE_MAPS_API_KEY": os.getenv("GOOGLE_MAPS_API_KEY")}

# Define response format
class Event(ObjectResponse):
    name: str
    location: str
    date: str
    category: str

class EventList(ObjectResponse):
    events: list[Event]

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Nearby Event Finder</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-100 flex justify-center items-center h-screen">
        <div class="bg-white p-8 rounded-lg shadow-lg w-[40rem]">
            <h1 class="text-2xl font-bold text-center mb-4">📍 Find Events Near You</h1>
            <input id="city" type="text" placeholder="Enter a city" class="w-full p-2 border rounded mb-4">
            <input id="date" type="date" class="w-full p-2 border rounded mb-4" value="" >
            <button onclick="findEvents()" class="bg-blue-500 text-white px-4 py-2 rounded w-full">Find Events</button>
            <div id="result" class="mt-4 text-sm text-gray-800 bg-gray-50 p-4 rounded overflow-y-auto h-64"></div>
        </div>
        <script>
            async function findEvents() {
                const city = document.getElementById("city").value;
                const date = document.getElementById("date").value;
                if (!city || !date) {
                    alert("Please enter both a city and a date.");
                    return;
                }
                const response = await fetch(`http://127.0.0.1:8000/find_events?city=${encodeURIComponent(city)}&date=${encodeURIComponent(date)}`);
                const data = await response.json();
                document.getElementById("result").innerText = JSON.stringify(data, null, 2);
            }
        </script>
    </body>
    </html>
    """

@app.get("/find_events")
async def find_events(city: str = Query(..., title="City"), date: str = Query(..., title="Event Date")):
    """Finds upcoming events in a specified city for a given date."""
    try:
        event_task = Task(
            f"Find upcoming events happening in {city} on {date}, including name, location, and category.",
            tools=[GoogleMapsMCP],
            response_format=EventList
        )
        event_finder_agent.do(event_task)
        response = event_task.response

        if not response:
            return {"error": "No events found for this city and date."}

        return {"events": response.events}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
