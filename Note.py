import json
import os
from datetime import datetime


class Note:
    def __init__(self, id, title, body, creation_time):
        self.id = id
        self.title = title
        self.body = body
        self.creation_time = creation_time
        self.last_modified_time = creation_time

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "creation_time": str(self.creation_time),
            "last_modified_time": str(self.last_modified_time)
        }

    @classmethod
    def from_dict(cls, d):
        return cls(
            id=d["id"],
            title=d["title"],
            body=d["body"],
            creation_time=datetime.fromisoformat(d["creation_time"])
        )

    def __repr__(self):
        return f"<Note {self.title} ({self.id})>"


def load_notes():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as f:
            data = json.load(f)
    else:
        data = {"notes": []}
    return data


def save_notes(data):
    with open("notes.json", "w") as f:
        json.dump(data, f, indent=4)


def create_note(data):
   # global data
    title = input("Введите заголовок заметки: ")
    body = input("Введите заметку: ")
    timestamp = datetime.now()
    id = len(data["notes"]) + 1
    note = Note(id, title, body, timestamp)
    data["notes"].append(note.to_dict())
    save_notes(data)
    print(f"Note '{title}' created. ")


def read_note(data):
   # global data
    identifier = input("Введите id или заголовок заметки: ")
    for note_dict in data["notes"]:
        if str(note_dict["id"]) == identifier or note_dict["title"] == identifier:
            note = Note.from_dict(note_dict)
            print(note.title)
            print(note.body)
            print(note.creation_time)
            print(note.last_modified_time)
            return
    print(f"Note '{identifier}' not found")


def update_note(data):
    # global data
    identifier = input("Введите id или заголовок заметки: ")
    for note_dict in data["notes"]:
        if str(note_dict["id"]) == identifier or note_dict["title"] == identifier:
            title = input(f"Введите новый заголовок ({note_dict['title']}): ")
            body = input(
                f"Введите новое содержание заметки ({note_dict['body']}): ")
            note_dict["title"] = title or note_dict["title"]
            note_dict["body"] = body or note_dict["body"]
            note_dict["last_modified_time"] = str(datetime.now())
            save_notes(data)
            print(f"Note '{note_dict['title']}' updated. ")
            return
    print(f"Note '{identifier}' not found")


def delete_note(data):
    identifier = input("Введите id заметки или заголовок: ")
    for note_dict in data["notes"]:
        if str(note_dict["id"]) == identifier or note_dict["title"]:
            data["notes"].remove(note_dict)
            save_notes(data)
            print(f"Note '{note_dict['title']}' deleted. ")
            return
    print(f"Note '{identifier}' not found")


def list_notes(data):
   # global data
    for note_dict in data["notes"]:
        note = Note.from_dict(note_dict)
        print(note.title)
        print(note.body)
        print(note.creation_time)
        print(note.last_modified_time)
        print()

    # while True:
    #     action = input(
    #         "Введите 'n' чтобы сделать новую заметку, 'r' чтобы прочитать, 'u' чтобы обновить, 'l' чтобы вывести список заметок, 'd' чтобы удалить,  'q' чтобы выйти: ")
    #     if action == "n":
    #         create_note(data)
    #     elif action == "r":
    #         read_note()
    #     elif action == "u":
    #         update_note()
    #     elif action == "d":
    #         delete_note(data)
    #     elif action == "l":
    #         list_notes(data)
    #     elif action == "q":
    #         break
    #     else:
    #         print("Неправильное действие")
