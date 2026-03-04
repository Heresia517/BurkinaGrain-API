import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.session import SessionLocal
from app.models.cereal import Cereal

def seed():
    db = SessionLocal()
    
    cereals = [
        {"name": "Mais", "region": "Ouagadougou", "price_per_kg": 185.0, "unit": "kg", "source": "SONAGESS 2025"},
        {"name": "Mil", "region": "Ouagadougou", "price_per_kg": 210.0, "unit": "kg", "source": "SONAGESS 2025"},
        {"name": "Sorgho", "region": "Ouagadougou", "price_per_kg": 195.0, "unit": "kg", "source": "SONAGESS 2025"},
        {"name": "Riz local", "region": "Ouagadougou", "price_per_kg": 425.0, "unit": "kg", "source": "SONAGESS 2025"},
        {"name": "Mais", "region": "Bobo-Dioulasso", "price_per_kg": 170.0, "unit": "kg", "source": "SONAGESS 2025"},
        {"name": "Mil", "region": "Bobo-Dioulasso", "price_per_kg": 195.0, "unit": "kg", "source": "SONAGESS 2025"},
        {"name": "Sorgho", "region": "Bobo-Dioulasso", "price_per_kg": 180.0, "unit": "kg", "source": "SONAGESS 2025"},
        {"name": "Riz local", "region": "Bobo-Dioulasso", "price_per_kg": 400.0, "unit": "kg", "source": "SONAGESS 2025"},
        {"name": "Mais", "region": "Koudougou", "price_per_kg": 175.0, "unit": "kg", "source": "SONAGESS 2025"},
        {"name": "Mil", "region": "Koudougou", "price_per_kg": 200.0, "unit": "kg", "source": "SONAGESS 2025"},
        {"name": "Sorgho", "region": "Koudougou", "price_per_kg": 190.0, "unit": "kg", "source": "SONAGESS 2025"},
        {"name": "Mil", "region": "Dori", "price_per_kg": 250.0, "unit": "kg", "source": "SONAGESS 2025"},
        {"name": "Sorgho", "region": "Dori", "price_per_kg": 235.0, "unit": "kg", "source": "SONAGESS 2025"},
        {"name": "Mais", "region": "Dori", "price_per_kg": 220.0, "unit": "kg", "source": "SONAGESS 2025"},
        {"name": "Mais", "region": "Fada N'Gourma", "price_per_kg": 180.0, "unit": "kg", "source": "SONAGESS 2025"},
        {"name": "Mil", "region": "Fada N'Gourma", "price_per_kg": 215.0, "unit": "kg", "source": "SONAGESS 2025"},
        {"name": "Sorgho", "region": "Fada N'Gourma", "price_per_kg": 200.0, "unit": "kg", "source": "SONAGESS 2025"},
    ]
    
    count = 0
    for data in cereals:
        exists = db.query(Cereal).filter_by(name=data["name"], region=data["region"]).first()
        if not exists:
            db.add(Cereal(**data))
            count += 1
    
    db.commit()
    print(f"OK {count} cereales inserees avec succes")
    db.close()

if __name__ == "__main__":
    seed()