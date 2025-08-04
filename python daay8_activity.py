FILENAME = "notes.txt"
from datetime import datetime

def show_menu():
    print("\nNotes Manager")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete Notes")
    print("4. Search Notes")
    print("5. Delete Individual Note")
    print("6. Exit")


def add_note():
    note=input("Enter your note: ")
    timestamp = datetime.now.strftime("[%Y-%m-%d %H:%M:%S]")
    with open(FILENAME, "a") as file:
        file.write(f"{timestamp} {note}\n")
    print("Note Saved")

def view_notes():
    try:
        with open(FILENAME, "r") as file:
            print("\n Your Notes:")
            print(file.read())
    except FileNotFoundError:
        print("No notes found.")

def delete_notes():
    import os
    try:
        os.remove(FILENAME)
        print("All notes deleted.")
    except FileNotFoundError:
        print("Nothing to delete.")

def search_notes():
    keyword = input("Enter a keyword to search: ").lower()
    try:
        with open(FILENAME, "r") as file:
            notes = file.readlines()
            matches = [note for note in notes if keyword in note.lower()]
            if matches:
                print("\nMatching Notes:")
                for note in matches:
                    print(note.strip())
            else:
                print("No matches found.")
    except FileNotFoundError:
        print("No notes to search.")

def delete_single_note():
    try:
        with open(FILENAME, "r") as file:
            notes = file.readlines()

        if not notes:
            print("No notes to delete.")
            return

        for idx, note in enumerate(notes, 1):
            print(f"{idx}. {note.strip()}")

        line_num = int(input("Enter the note number to delete: "))
        if 1 <= line_num <= len(notes):
            removed = notes.pop(line_num - 1)
            with open(FILENAME, "w") as file:
                file.writelines(notes)
            print(f"Deleted: {removed.strip()}")
        else:
            print("Invalid number.")
    except FileNotFoundError:
        print("No notes found.")
    except ValueError:
        print("Please enter a valid number.")



while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        delete_notes()
    elif choice == "4":
        search_notes()
    elif choice == "5":
        delete_single_note()
    elif choice == "6":
        print("Goodbye")
        break
    else:
        print("Invalid Choice.")