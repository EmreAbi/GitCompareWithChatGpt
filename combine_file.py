import os
import tkinter as tk
from tkinter import filedialog, Text, scrolledtext

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(sticky="nsew")
        self.create_widgets()

    def create_widgets(self):
        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.rowconfigure(self, 0, weight=1)

        self.prompt_text = scrolledtext.ScrolledText(self, height=3)
        self.prompt_text.grid(row=0, column=0, columnspan=5, sticky="ew")
        self.prompt_text.insert(tk.INSERT, "PROMPT: ")

        self.listbox = tk.Listbox(self, selectmode=tk.EXTENDED)
        self.listbox.grid(row=1, column=0, columnspan=5, sticky="nsew")

        self.select_file_button = tk.Button(self)
        self.select_file_button["text"] = "Select Files"
        self.select_file_button["command"] = self.select_files
        self.select_file_button.grid(row=2, column=0, sticky="ew")

        self.select_folder_button = tk.Button(self)
        self.select_folder_button["text"] = "Select Folder"
        self.select_folder_button["command"] = self.select_folder
        self.select_folder_button.grid(row=2, column=1, sticky="ew")

        self.remove_selected_button = tk.Button(self)
        self.remove_selected_button["text"] = "Remove Selected"
        self.remove_selected_button["command"] = self.remove_selected
        self.remove_selected_button.grid(row=2, column=2, sticky="ew")

        self.combine_button = tk.Button(self)
        self.combine_button["text"] = "Combine Files"
        self.combine_button["command"] = self.combine_files
        self.combine_button.grid(row=2, column=3, sticky="ew")

    def select_files(self):
        filenames = filedialog.askopenfilenames()
        for filename in filenames:
            self.listbox.insert(tk.END, filename)

    def select_folder(self):
        foldername = filedialog.askdirectory()
        for dirpath, dirnames, filenames in os.walk(foldername):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                self.listbox.insert(tk.END, filepath)

    def remove_selected(self):
        selected_indices = self.listbox.curselection()
        for i in reversed(selected_indices):
            self.listbox.delete(i)

    def combine_files(self):
        import re
        prompt = self.prompt_text.get('1.0', 'end-1c')
        content_list = []
        
        for filename in self.listbox.get(0, tk.END):
            content_list.append('//<{}>\n'.format(filename))
            with open(filename, "r") as infile:
                content = infile.read()
                content = '\n'.join(line.strip() for line in content.split('\n'))
                content = re.sub(r'\n\s*\n', '\n', content)
                content_list.append(content + '\n\n')

        # The combined content
        content_all = prompt + '\n\n' + ''.join(content_list)

        # Calculate the total number of lines
        total_lines = content_all.count('\n')

        # If total lines exceed 500, then we need to split the file
        if total_lines > 500:
            # Call split_prompt function to get the splitted files
            splitted_files = Application.split_prompt(content_all, 10000)
            # Write the splitted content to their respective files
            for file_data in splitted_files:
                with open(file_data['name'], 'w') as f:
                    f.write(file_data['content'])
        else:
            # If total lines are less than 500, then write the content to a single file
            with open("combined_file.txt", "w") as outfile:
                outfile.write(content_all)


    def split_prompt(text, split_length):
        if split_length <= 0:
            raise ValueError("Max length must be greater than 0.")

        num_parts = -(-len(text) // split_length)
        file_data = []

        for i in range(num_parts):
            start = i * split_length
            end = min((i + 1) * split_length, len(text))

            if i == num_parts - 1:
                content = f'[START PART {i + 1}/{num_parts}]\n' + text[start:end] + f'\n[END PART {i + 1}/{num_parts}]'
                content += '\nALL PARTS SENT. Now you can continue processing the request.'
            else:
                content = f'Do not answer yet. This is just another part of the text I want to send you. Just receive and acknowledge as "Part {i + 1}/{num_parts} received" and wait for the next part.\n[START PART {i + 1}/{num_parts}]\n' + text[start:end] + f'\n[END PART {i + 1}/{num_parts}]'
                content += f'\nRemember not answering yet. Just acknowledge you received this part with the message "Part {i + 1}/{num_parts} received" and wait for the next part.'

            file_data.append({
                'name': f'split_{str(i + 1).zfill(3)}_of_{str(num_parts).zfill(3)}.txt',
                'content': content
            })

        return file_data

def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
