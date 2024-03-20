import json
from datetime import datetime

class Note:
    def __init__(self, note_id, title, body, timestamp=None):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = timestamp or datetime.now()

    def to_dict(self):
        return {
            "note_id": self.note_id,
            "title": self.title,
            "body": self.body,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }

    @classmethod
    def from_dict(cls, note_dict):
        note_id = note_dict.get("note_id")
        title = note_dict.get("title")
        body = note_dict.get("body")
        timestamp_str = note_dict.get("timestamp")
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        return cls(note_id, title, body, timestamp)

    def __str__(self):
        return f"[{self.timestamp}] {self.title}: {self.body}"
    
class NoteManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.file_path, "r") as file:
                notes_data = json.load(file)
                return [Note.from_dict(note_dict) for note_dict in notes_data]
        except FileNotFoundError:
            return []

    def save_notes(self):
        notes_data = [note.to_dict() for note in self.notes]
        with open(self.file_path, "w") as file:
            json.dump(notes_data, file, indent=4)

    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        note = Note(note_id, title, body)
        self.notes.append(note)
        self.save_notes()

    def edit_note(self, note_id, title, body):
        note = self.get_note_by_id(note_id)
        if note:
            note.title = title
            note.body = body
            note.timestamp = datetime.now()
            self.save_notes()
        else:
            print("Заметка не найдена")

    def delete_note(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            self.save_notes()
        else:
            print("Заметка не найдена")

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        return None

    def filter_notes_by_date(self, date):
        filtered_notes = []
        for note in self.notes:
            if note.timestamp.date() == date:
                filtered_notes.append(note)
        return filtered_notes

    def print_notes(self, notes):
        for note in notes:
            print(note)


def main():
    file_path = "notes.json"
    manager = NoteManager(file_path)

    while True:
        command = input("Введите команду (add/edit/delete/read/filter/exit): ")

        if command == "add":
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            manager.add_note(title, body)
            print("Заметка успешно сохранена")

        elif command == "edit":
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новое тело заметки: ")
            manager.edit_note(note_id, title, body)
            print("Заметка успешно отредактирована")

        elif command == "delete":
            note_id = int(input("Введите ID заметки для удаления: "))
            manager.delete_note(note_id)
            print("Заметка успешно удалена")

        elif command == "read":
            manager.print_notes(manager.notes)

        elif command == "filter":
            date_str = input("Введите дату для фильтрации заметок (гггг-мм-дд): ")
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d").date()
                filtered_notes = manager.filter_notes_by_date(date)
                manager.print_notes(filtered_notes)
            except ValueError:
                print("Некорректный формат даты")

        elif command == "exit":
            break

        else:
            print("Некорректная команда")

if __name__ == "__main__":
    main()

            