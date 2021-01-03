import model
import repository


def test_repository_can_save_a_batch(session):
    batch = model.Batch("batch1", "RUSTY-SOAPDISH", 100, eta=None)

    repo = repository.SqlAlchemyRepository(session)
    repo.add(batch)  # repo.add() is the method under test here.
    session.commit()  # keep the .commit() outside of the repository and make it the responsibility of the caller.

    rows = list(session.execute(
        'SELECT reference, sku, _purchased_quantity, eta FROM "batches"'  # use the raw SQL to verify that the right data has been saved.
    ))
    assert rows == [("batch1", "RUSTY-SOAPDISH", 100, None)]