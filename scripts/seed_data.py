# scripts/seed_data.py

from faker import Faker
from sqlmodel import SQLModel, Session
from datetime import datetime
from powertrak.db import engine
from powertrak.models import Customer, Equipment, Job
from powertrak.models.job import JobStatus

fake = Faker()


def create_fake_customers(n: int = 10) -> list[Customer]:
    """Generate customers with names and ZIP codes."""
    return [
        Customer(
            name=fake.name(), zip_code=fake.zipcode(), created_at=datetime.utcnow()
        )
        for _ in range(n)
    ]


def create_fake_equipment(customers: list[Customer], n: int = 10) -> list[Equipment]:
    """Generate equipment tied to random customers."""
    return [
        Equipment(
            name=fake.word().capitalize() + " Machine",
            serial_number=fake.unique.bothify(text="SN-####-???"),
            description=fake.sentence(nb_words=6),
            owner_id=fake.random_element(customers).id,
        )
        for _ in range(n)
    ]


def create_fake_jobs(equipment_list: list[Equipment], n: int = 15) -> list[Job]:
    """Generate jobs tied to equipment with random completion status."""
    jobs: list[Job] = []
    for _ in range(n):
        eq = fake.random_element(equipment_list)
        job = Job(
            description=fake.text(max_nb_chars=120),
            scheduled_at=fake.date_time_this_year(),
            equipment_id=eq.id,
            created_at=datetime.utcnow(),
        )
        # 40% chance to mark as complete
        if fake.boolean(chance_of_getting_true=40):
            job.status = JobStatus.complete
        jobs.append(job)
    return jobs


def seed_database() -> None:
    """Drop/create tables, then seed customers, equipment, jobs, and rewards."""
    # 1) Ensure tables exist
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        # 2) Seed customers
        customers = create_fake_customers()
        session.add_all(customers)
        session.commit()
        for c in customers:
            session.refresh(c)

        # 3) Seed equipment
        equipment = create_fake_equipment(customers)
        session.add_all(equipment)
        session.commit()
        for e in equipment:
            session.refresh(e)

        # 4) Build map: equipment_id → customer_id
        equipment_map = {e.id: e.owner_id for e in equipment}

        # 5) Seed jobs
        jobs = create_fake_jobs(equipment)
        session.add_all(jobs)
        session.commit()
        for j in jobs:
            session.refresh(j)

            # 6) Award reward points for completed jobs
            if j.status == JobStatus.complete:
                cust_id = equipment_map[j.equipment_id]
                cust = next(c for c in customers if c.id == cust_id)
                cust.reward_points += 10

        # 7) Persist updated reward_points
        session.add_all(customers)
        session.commit()

    print("✅ Seed complete. Customers, equipment, jobs, and rewards loaded.")


if __name__ == "__main__":
    seed_database()
