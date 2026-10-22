# Forage Forecast 360

A student-project prototype for adaptive rangeland planning. Includes a transparent forage budget, editable mixed-herd inputs, weather retrieval, reverse geocoding, nearby mapped water-feature lookup, photo upload with a basic green-pixel estimate, optional Groq AI explanations, and CSV export.

## Important limitations
- This is not a validated farm-management system.
- The starting forage values, growth rates, allowable use, reserve, intake percentages, and scenario adjustments are assumptions until replaced by local measurements and expert-approved thresholds.
- A photo's green pixels do not measure edible dry matter, species composition, digestibility, or carrying capacity.
- OpenStreetMap water features may be missing or outdated and do not prove access, water quality, flow, or potability.
- Weather forecasts are not forage-growth forecasts. Growth depends on local species, soil, season, moisture, temperature, grazing history, and management.
- Do not make real stocking decisions from this prototype alone.

## Setup (Windows)
1. Install Python 3.11 or newer.
2. Extract the ZIP.
3. Open a terminal in this folder.
4. Create a virtual environment:
   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
   ```
5. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
6. Copy `.env.example` to `.env`. Leave optional keys blank if not using those services.
7. Run:
   ```powershell
   streamlit run app.py
   ```

## Optional API keys
### Groq
Create an account and API key in the Groq console, then put it in `GROQ_API_KEY` inside `.env`. Check current free-tier limits and model availability in the provider console; they can change.

### Hugging Face
Create a token with the required inference permission if you later connect a hosted model. This prototype does not require the HF token. Hugging Face hosted inference can have limited free credits and may become billable, so check current pricing before enabling it.

### USDA NASS Quick Stats
Optional and relevant primarily to US agricultural statistics. Register for a Quick Stats key and set `USDA_NASS_API_KEY`. The current prototype does not call this API yet; don't enter a key expecting it to affect calculations.

## APIs used without a key for this demo
- Open-Meteo Forecast API: daily weather data, generally no key for normal non-commercial use.
- Nominatim: reverse geocoding from coordinates.
- OpenStreetMap Overpass API: searches mapped water-related features.

Respect each service's usage policy, attribution requirements, and rate limits. Public endpoints are not guaranteed to be available at all times. For a school demo, avoid repeated rapid requests and use a contact email in `USER_AGENT`.

## Calculation summary
The app estimates daily dry-matter demand as:

`animal count × liveweight (kg) × daily intake fraction`

It estimates a safe forage budget from standing forage × allowable use × reserve retention, plus estimated regrowth over the planning period. A scenario factor can reduce this budget. The model compares that supply with total herd demand across the selected horizon.

This simplified budget should be replaced by a locally validated forage model before real use. It does not independently certify ecological sustainability.
