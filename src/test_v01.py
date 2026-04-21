from classifier import classify
from sorter import move_file

def test_v01():
    fake_file = "example.jpg"

    category = classify(fake_file)

    print("File:", fake_file)
    print("Category:", category)
    print("Sorter would move file to:", category)

test_v01()
