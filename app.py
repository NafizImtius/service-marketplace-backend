from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///providers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Provider model
class Provider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, default=4.0)
    priceRange = db.Column(db.String(10))
    emoji = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'phone': self.phone,
            'location': self.location,
            'rating': self.rating,
            'priceRange': self.priceRange,
            'emoji': self.emoji
        }

# Create tables
with app.app_context():
    db.create_all()
    
    # Add default providers if database is empty
    if Provider.query.count() == 0:
        default_providers = [
            Provider(
                name="Karim Electricals",
                category="Electrician",
                phone="01712345678",
                location="Shyamoli",
                rating=4.8,
                priceRange="৳৳",
                emoji="👨‍🔧"
            ),
            Provider(
                name="Rahim Plumbing Services",
                category="Plumber",
                phone="01798765432",
                location="Mohammadpur",
                rating=4.5,
                priceRange="৳৳",
                emoji="🚰"
            ),
            Provider(
                name="Shahana Cleaning Co.",
                category="Cleaner",
                phone="01856781234",
                location="Mirpur-10",
                rating=5.0,
                priceRange="৳৳৳",
                emoji="🧹"
            ),
            Provider(
                name="Cool Tech AC Service",
                category="AC Repair",
                phone="01923456789",
                location="Gulshan",
                rating=4.2,
                priceRange="৳৳",
                emoji="❄️"
            )
        ]
        db.session.add_all(default_providers)
        db.session.commit()

@app.route('/api/providers', methods=['GET'])
def get_providers():
    providers = Provider.query.all()
    return jsonify([p.to_dict() for p in providers])

@app.route('/api/providers', methods=['POST'])
def add_provider():
    data = request.json
    new_provider = Provider(
        name=data['name'],
        category=data['category'],
        phone=data['phone'],
        location=data['location'],
        rating=data.get('rating', 4.0),
        priceRange=data.get('priceRange', '৳৳'),
        emoji=data.get('emoji', '🔧')
    )
    db.session.add(new_provider)
    db.session.commit()
    return jsonify(new_provider.to_dict()), 201

@app.route('/api/providers/<int:id>', methods=['DELETE'])
def delete_provider(id):
    provider = Provider.query.get(id)
    
    if provider is None:
        return jsonify({'error': 'Provider not found'}), 404
    
    db.session.delete(provider)
    db.session.commit()
    
    return jsonify({'message': 'Provider deleted successfully'}), 200


@app.route('/api/providers/<int:id>', methods=['PUT'])
def update_provider(id):
    provider = Provider.query.get(id)
    
    if provider is None:
        return jsonify({'error': 'Provider not found'}), 404
    
    data = request.json
    
    # Update fields if provided
    if 'name' in data:
        provider.name = data['name']
    if 'category' in data:
        provider.category = data['category']
    if 'phone' in data:
        provider.phone = data['phone']
    if 'location' in data:
        provider.location = data['location']
    if 'rating' in data:
        provider.rating = data['rating']
    if 'priceRange' in data:
        provider.priceRange = data['priceRange']
    
    db.session.commit()
    
    return jsonify(provider.to_dict()), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)