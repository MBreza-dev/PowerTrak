from sqlmodel import SQLModel, Session
from powertrak.db import engine
from powertrak.models import Customer, Job, Equipment

def reset_database():
	print("⚠️  Dropping all tables...")
	SQLModel.metadata.drop_all(engine)
	print("✅ Tables dropped.")

	print("🛠️  Creating all tables...")
	SQLModel.metadata.create_all(engine)
	print("✅ Tables created.")

	# Optional: seed right away
	from seed_data import seed_database
	print("🌱 Seeding database...")
	seed_database()

if __name__ == "__main__":
	reset_database()
