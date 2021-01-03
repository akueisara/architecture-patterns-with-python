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


def insert_order_line(session):
    session.execute(  # This tests the read side, so the raw SQL is preparing data to be read by the repo.get().
        'INSERT INTO order_lines (orderid, sku, qty)'
        ' VALUES ("order1", "GENERIC-SOFA", 12)'
    )
    [[orderline_id]] = session.execute(
        'SELECT id FROM order_lines WHERE orderid=:orderid AND sku=:sku',
        dict(orderid="order1", sku="GENERIC-SOFA")
    )
    return orderline_id


# TODO: add more details later
def insert_batch(session, batch_id):
    pass


def insert_allocation(session, orderline_id, batch_id):
    pass


def test_repository_can_retrieve_a_batch_with_allocations(session):
    orderline_id = insert_order_line(session)
    batch1_id = insert_batch(session, "batch1")
    insert_batch(session, "batch2")
    insert_allocation(session, orderline_id, batch1_id)

    repo = repository.SqlAlchemyRepository(session)
    retrieved = repo.get("batch1")

    expected = model.Batch("batch1", "GENERIC-SOFA", 100, eta=None)
    # checks that the types match, and that the reference is the same
    assert retrieved == expected  # Batch.__eq__ only compares reference
    # explicitly check on its major attributes, including ._allocations, which is a Python set of OrderLine value objects.
    assert retrieved.sku == expected.sku
    assert retrieved._purchased_quantity == expected._purchased_quantity
    assert retrieved._allocations == {
        model.OrderLine("order1", "GENERIC-SOFA", 12),
    }