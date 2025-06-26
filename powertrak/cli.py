import typer
from powertrak.db import init_db, get_session
from powertrak.models import Customer, Equipment, Job

app = typer.Typer(help="PowerTrak Repair Scheduler CLI")


@app.command()
def init():
    """Create or reset the database."""
    init_db()
    typer.echo("Database initialized.")


@app.command()
def list_customers():
    """List all customers."""
    session = get_session()
    for c in session.query(Customer).all():
        typer.echo(f"{c.id}: {c.name} <{c.email or 'no email'}>")


@app.command()
def list_equipment():
    """List all equipment with owner info."""
    session = get_session()
    for e in session.query(Equipment).all():
        # split into details + meta for line-length sanity
        details = f"{e.id}: {e.name}"
        meta = f"SN: {e.serial_number or '—'} • Owner {e.customer_id}"
        typer.echo(f"{details} — {meta}")


@app.command()
def list_jobs():
    """List all jobs with status."""
    session = get_session()
    for j in session.query(Job).all():
        typer.echo(
            f"{j.id}: [{j.status}] {j.description or 'no desc'} "
            f"(Cust {j.customer_id}, Equip {j.equipment_id}) – Created {j.created_at}"
        )


if __name__ == "__main__":
    app()
