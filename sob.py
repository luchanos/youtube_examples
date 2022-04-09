class TextFile:
    def __init__(self, name: str):
        self.text_data = ""
        self.name = name
        self.cursor = 0

    def append_text(self, text: str):
        if self.cursor == len(self.text_data):
            self.text_data += text
            self.cursor += len(text)
        else:
            self.text_data = self.text_data[:self.cursor] +\
                             text + self.text_data[self.cursor:]

    def delete_text(self):
        str_for_work_lst = list(self.text_data)
        if self.cursor < len(self.text_data):
            str_for_work_lst.pop(self.cursor)
            self.text_data = "".join(str_for_work_lst)

    def move_cursor(self, move_steps):
        self.cursor = int(move_steps) if \
            int(move_steps) <= len(self.text_data) else len(self.text_data)

    def __str__(self):
        return self.text_data


class FileEditor:
    def __init__(self):
        self.files = {}
        self.current_edit_file = None
        self.current_edit_file_name = None
        self.history = []

    def create_file(self, name):
        self.files[name] = TextFile(name)

    def switch(self, name):
        file_for_editing = self.files.get(name)
        if file_for_editing is None:
            print("File not found!")  # тут можно делать raise
        else:
            self.current_edit_file = file_for_editing
            self.current_edit_file_name = file_for_editing.name

    def parse_queries(self, queries: list):
        for query in queries:
            command = query[0]
            if command == "APPEND":
                self.current_edit_file.append_text(query[1])
            elif command == "DELETE":
                self.current_edit_file.delete_text()
            elif command == "MOVE":
                self.current_edit_file.move_cursor(query[1])
            elif command == "CREATE":
                self.files[query[1]] = TextFile(query[1])
            elif command == "SWITCH":
                self.switch(query[1])

    def __str__(self):
        return str(self.files)


queries = [
    ["APPEND", "Hey"],
    ["APPEND", " there"],
    ["APPEND", "!"],
    ["MOVE", "2"],
    ["DELETE"],
    ["APPEND", "!"]
]

test_editor = FileEditor()
test_file = TextFile("my_name")

test_editor.create_file("my_name")
print(test_editor)
test_editor.switch("my_name")
test_editor.parse_queries(queries)
# test_editor.current_edit_file.move_cursor(2)
test_editor.parse_queries(queries)
print(test_editor.current_edit_file)
# print(test_editor.current_edit_file.cursor)
# test_editor.current_edit_file.move_cursor(-10000)
# print(test_editor.current_edit_file.cursor)
# test_editor.current_edit_file.delete_text()
# print(test_editor.current_edit_file)
# test_editor.current_edit_file.delete_text()
# print(test_editor.current_edit_file)
# test_editor.current_edit_file.delete_text()
# print(test_editor.current_edit_file)
