import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("300x200")
        self.root.configure(bg="lightgray")

        self.time_elapsed = 0
        self.running = False

        # Display Timer
        self.label = tk.Label(root, text="0s", font=("Arial", 30), bg="lightgray")
        self.label.pack(pady=20)

        # Start/Pause Button
        self.start_pause_button = tk.Button(root, text="Start", font=("Arial", 14), bg="blue", fg="white",
                                            command=self.toggle)
        self.start_pause_button.pack(pady=5)

        # Reset Button
        self.reset_button = tk.Button(root, text="Reset", font=("Arial", 14), bg="red", fg="white",
                                      command=self.reset)
        self.reset_button.pack(pady=5)

        # Update Timer
        self.update_timer()

    def toggle(self):
        """Starts or Pauses the Stopwatch"""
        if self.running:
            self.running = False
            self.start_pause_button.config(text="Start")
        else:
            self.running = True
            self.start_time = time.time() - self.time_elapsed
            self.start_pause_button.config(text="Pause")
            self.update_timer()

    def reset(self):
        """Resets the Stopwatch"""
        self.running = False
        self.time_elapsed = 0
        self.label.config(text="0s")
        self.start_pause_button.config(text="Start")

    def update_timer(self):
        """Updates the stopwatch display while running"""
        if self.running:
            self.time_elapsed = time.time() - self.start_time
            self.label.config(text=f"{int(self.time_elapsed)}s")
            self.root.after(1000, self.update_timer)  # Update every second
        elif not self.running and self.time_elapsed > 0:
            self.label.config(text=f"{int(self.time_elapsed)}s")

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()
