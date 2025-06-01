# Import library yang dibutuhkan
import tkinter as tk
from tkinter import messagebox

# Buat class untuk aplikasi to-do list
class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        # Buat frame untuk input tugas
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()

        # Buat label dan entry untuk input tugas
        self.task_label = tk.Label(self.input_frame, text="Tugas:")
        self.task_label.pack(side=tk.LEFT)
        self.task_entry = tk.Entry(self.input_frame, width=30)
        self.task_entry.pack(side=tk.LEFT)

        # Buat tombol untuk membuat tugas baru
        self.create_button = tk.Button(self.input_frame, text="Buat", command=self.create_task)
        self.create_button.pack(side=tk.LEFT)

        # Buat frame untuk menampilkan daftar tugas
        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack()

        # Buat label untuk menampilkan daftar tugas
        self.task_list_label = tk.Label(self.task_frame, text="Daftar Tugas:")
        self.task_list_label.pack()

        # Buat text box untuk menampilkan daftar tugas
        self.task_list_text = tk.Text(self.task_frame, width=40, height=10)
        self.task_list_text.pack()

        # Buat frame untuk mengedit dan menghapus tugas
        self.edit_frame = tk.Frame(self.root)
        self.edit_frame.pack()

        # Buat label dan entry untuk input tugas yang ingin diedit
        self.edit_task_label = tk.Label(self.edit_frame, text="Tugas yang ingin diedit:")
        self.edit_task_label.pack(side=tk.LEFT)
        self.edit_task_entry = tk.Entry(self.edit_frame, width=30)
        self.edit_task_entry.pack(side=tk.LEFT)

        # Buat tombol untuk mengedit tugas
        self.update_button = tk.Button(self.edit_frame, text="Edit", command=self.update_task)
        self.update_button.pack(side=tk.LEFT)

        # Buat tombol untuk menghapus tugas
        self.delete_button = tk.Button(self.edit_frame, text="Hapus", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT)

    def create_task(self):
        # Ambil input tugas dari entry
        task = self.task_entry.get()

        # Tambahkan tugas ke daftar tugas
        self.tasks.append(task)

        # Tampilkan daftar tugas
        self.task_list_text.delete(1.0, tk.END)
        for task in self.tasks:
            self.task_list_text.insert(tk.END, task + "\n")

        # Kosongkan entry
        self.task_entry.delete(0, tk.END)

    def update_task(self):
        # Ambil input tugas yang ingin diedit dari entry
        task_to_edit = self.edit_task_entry.get()

        # Cari tugas yang ingin diedit di daftar tugas
        for i, task in enumerate(self.tasks):
            if task == task_to_edit:
                # Edit tugas
                self.tasks[i] = self.task_entry.get()

                # Tampilkan daftar tugas
                self.task_list_text.delete(1.0, tk.END)
                for task in self.tasks:
                    self.task_list_text.insert(tk.END, task + "\n")

                # Kosongkan entry
                self.edit_task_entry.delete(0, tk.END)
                self.task_entry.delete(0, tk.END)

                return

        # Jika tugas tidak ditemukan, tampilkan pesan error
        messagebox.showerror("Error", "Tugas tidak ditemukan")

    def delete_task(self):
        # Ambil input tugas yang ingin dihapus dari entry
        task_to_delete = self.edit_task_entry.get()

        # Cari tugas yang ingin dihapus di daftar tugas
        for i, task in enumerate(self.tasks):
            if task == task_to_delete:
                # Hapus tugas
                del self.tasks[i]

                # Tampilkan daftar tugas
                self.task_list_text.delete(1.0, tk.END)
                for task in self.tasks:
                    self.task_list_text.insert(tk.END, task + "\n")

                # Kosongkan entry
                self.edit_task_entry.delete(0, tk.END)

                return

        # Jika tugas tidak ditemukan, tampilkan pesan error
        messagebox.showerror("Error", "Tugas tidak ditemukan")

# Buat root window
root = tk.Tk()

# Buat aplikasi to-do list
app = ToDoList(root)

# Jalankan aplikasi
root.mainloop()
