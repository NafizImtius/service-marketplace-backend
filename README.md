# 🔧 Service Marketplace Backend

Flask REST API for the Service Marketplace application.

## 🚀 Tech Stack

- **Flask** - Web framework
- **SQLAlchemy** - ORM
- **SQLite** - Database (development)
- **Flask-CORS** - Handle cross-origin requests

## 📦 Installation
```bash
# Clone repository
git clone https://github.com/NafizImtius/service-marketplace-backend.git
cd service-marketplace-backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install flask flask-cors flask-sqlalchemy

# Run server
python app.py
```

Server runs on `http://localhost:5000`

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/providers` | Get all service providers |
| POST | `/api/providers` | Add new provider |

### Example Request (POST)
```json
{
  "name": "Karim Electricals",
  "category": "Electrician",
  "phone": "01712345678",
  "location": "Shyamoli",
  "rating": 4.8,
  "priceRange": "৳৳",
  "emoji": "👨‍🔧"
}
```

## 💾 Database

- SQLite database stored in `instance/providers.db`
- Auto-created on first run
- Comes with 4 default providers

## 🔜 Roadmap

- [ ] Add PUT/DELETE endpoints for provider management
- [ ] Migrate to PostgreSQL for production
- [ ] Add user authentication (JWT)
- [ ] Add search and filter endpoints
- [ ] Add validation and error handling
- [ ] Add automated tests

## 🎓 Academic Project

Part of CSE471 (System Analysis and Design) - BRAC University

**Developer:** Nafiz Imtius