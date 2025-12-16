import os
import tempfile
from Phonebook import PhoneBook, Contact


def test_add_and_list():
    pb = PhoneBook()
    pb.add_contact("Alice", "123")
    pb.add_contact("Bob", "456")
    pb.add_contact("Alice", "789")
    names = [c.name for c in pb.list_contacts()]
    assert "Alice" in names
    assert "Bob" in names
    alice = pb.contacts["Alice"]
    assert set(alice.numbers) == {"123", "789"}


def test_find_and_remove():
    pb = PhoneBook()
    pb.add_contact("Charlie", "111")
    pb.add_contact("Charles", "222")
    res = pb.find_contacts("char")
    assert len(res) == 2
    assert pb.remove_contact("Charlie")
    assert not pb.remove_contact("Charlie")


def test_save_load():
    pb = PhoneBook()
    pb.add_contact("Diana", "333")
    tmp = tempfile.NamedTemporaryFile(delete=False)
    path = tmp.name
    tmp.close()
    try:
        pb.save_to_file(path)
        pb2 = PhoneBook()
        pb2.load_from_file(path)
        assert "Diana" in pb2.contacts
        assert pb2.contacts["Diana"].numbers == ["333"]
    finally:
        os.remove(path)


if __name__ == "__main__":
    test_add_and_list()
    test_find_and_remove()
    test_save_load()
    print("All tests passed")
