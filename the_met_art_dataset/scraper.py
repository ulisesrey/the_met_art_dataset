import requests
import os
import json
import time

def scrape_met_paintings(query="paintings", limit=2):
    # 1. Search for Highlights in 'Paintings' medium
    url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
    params = {
        "isHighlight": "true",
        "medium": "Paintings",
        "q": query
    }
    
    ids = requests.get(url, params=params).json().get('objectIDs', [])[:limit]
    print(ids)
    db = []
    os.makedirs("data/raw/images", exist_ok=True)

    for oid in ids:
        # 2. Get Object Data
        response = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{oid}")
        if response.status_code == 200:
            try:
                obj = response.json()
            except requests.exceptions.JSONDecodeError:
                print(f"⚠️ Error decoding JSON for ID {oid}. Skipping.")
                continue
        else:
            print(f"❌ Failed to fetch ID {oid}: Status {response.status_code}. Skipping.")
            # If you get a 429 (Too Many Requests), wait a bit longer
            if response.status_code == 429:
                print("🚦 Rate limit hit. Sleeping for 5 seconds...")
                time.sleep(5)
            continue
        
        # 3. Check for image and Public Domain
        if obj.get('primaryImage') and obj.get('isPublicDomain'):
            img_url = obj.get('primaryImage')
            file_name = f"data/raw/images/{oid}.jpg"
            
            #4. Download Image
            img_data = requests.get(img_url).content
            with open(file_name, 'wb') as f:
                f.write(img_data)
            
            # 5. Save Metadata
            db.append({
                "id": oid,
                "title": obj.get('title'),
                "author": obj.get('artistDisplayName'),
                "artist_nationality": obj.get('artistNationality', "Unknown"),
                "artist_gender": obj.get('artistGender', ""),
                "artist_display_bio": obj.get('artistDisplayBio', ""),
                "artist_begin_date": obj.get('artistBeginDate', ""),
                "artist_end_date": obj.get('artistEndDate', ""),
                "object_name": obj.get('objectName', ""),
                "object_year_desc": obj.get('objectDate'),
                "object_begin_date": obj.get('objectBeginDate'),
                "object_end_date": obj.get('objectEndDate'),
                "medium": obj.get('medium'),
                "classification": obj.get('classification'),
                "department": obj.get('department'),
                "period": obj.get('period', ""),
                "culture": obj.get('culture', ""),
                "repository": obj.get('repository', "Metropolitan Museum of Art"),
                "primary_image_url": obj.get('primaryImage'),
                "primary_image_small": obj.get('primaryImageSmall'),
                "local_path": file_name
                        })
            print(f"✅ Downloaded: {obj.get('title')}")
            time.sleep(0.5) # Be kind to their servers!

    with open("data/raw/art_db.json", "w") as f:
        json.dump(db, f, indent=4)

if __name__ == "__main__":
    scrape_met_paintings()