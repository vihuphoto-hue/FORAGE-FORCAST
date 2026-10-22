import requests
from config import USER_AGENT, REQUEST_TIMEOUT_SECONDS

HEADERS = {"User-Agent": USER_AGENT}

def reverse_geocode(latitude: float, longitude: float) -> dict:
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {"lat": latitude, "lon": longitude, "format": "jsonv2", "zoom": 10}
    r = requests.get(url, params=params, headers=HEADERS, timeout=REQUEST_TIMEOUT_SECONDS)
    r.raise_for_status()
    data = r.json()
    address = data.get("address", {})
    return {
        "display_name": data.get("display_name", ""),
        "country": address.get("country", ""),
        "state": address.get("state", address.get("region", "")),
        "county": address.get("county", ""),
        "raw": address,
    }

def geocode_place(place: str) -> dict:
    url = "https://nominatim.openstreetmap.org/search"
    r = requests.get(url, params={"q": place, "format": "jsonv2", "limit": 1},
                     headers=HEADERS, timeout=REQUEST_TIMEOUT_SECONDS)
    r.raise_for_status()
    items = r.json()
    if not items:
        raise ValueError("Place not found")
    return {"latitude": float(items[0]["lat"]), "longitude": float(items[0]["lon"]),
            "display_name": items[0].get("display_name", "")}

def nearest_water_features(latitude: float, longitude: float, radius_m: int = 5000) -> list:
    """Find nearby mapped water features. OpenStreetMap data may be incomplete/out of date."""
    query = f"""
    [out:json][timeout:20];
    (
      node(around:{radius_m},{latitude},{longitude})[natural~"^(water|spring)$"];
      way(around:{radius_m},{latitude},{longitude})[natural~"^(water|spring)$"];
      relation(around:{radius_m},{latitude},{longitude})[natural=water];
      node(around:{radius_m},{latitude},{longitude})[waterway~"^(river|stream|canal)$"];
      way(around:{radius_m},{latitude},{longitude})[waterway~"^(river|stream|canal)$"];
      node(around:{radius_m},{latitude},{longitude})[man_made=water_well];
      node(around:{radius_m},{latitude},{longitude})[amenity=drinking_water];
    );
    out center tags;
    """
    url = "https://overpass-api.de/api/interpreter"
    r = requests.post(url, data=query, headers=HEADERS, timeout=REQUEST_TIMEOUT_SECONDS + 10)
    r.raise_for_status()
    data = r.json()
    results = []
    for el in data.get("elements", [])[:30]:
        tags = el.get("tags", {})
        center = el.get("center", {})
        lat = el.get("lat", center.get("lat"))
        lon = el.get("lon", center.get("lon"))
        results.append({
            "Name": tags.get("name", "Unnamed mapped water feature"),
            "Type": tags.get("waterway", tags.get("natural", tags.get("amenity", tags.get("man_made", "water")))),
            "Latitude": lat, "Longitude": lon,
            "Note": "Verify on site; map data does not confirm flow, access or water quality."
        })
    return results
