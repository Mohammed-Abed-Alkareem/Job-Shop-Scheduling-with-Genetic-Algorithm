import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from projectFiles.Data.read_csv import dictionary_store
from projectFiles.Genetic_Algoritm.genetic_algorithm import genetic_algorithm, machine_phases, extract_jobs, draw_gantt_chart
from projectFiles.Genetic_Algoritm.Fitness_Functions import get_makespan, get_working_time
from projectFiles.Genetic_Algoritm.Crossover_Functions import make_crossover, modified_order_crossover

Jobs = dictionary_store("Data/job_shop_schedule.csv")

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Genetic Algorithm")

        # Custom Colors
        label_bg_color = "#87CEFA"  # Light blue
        label_fg_color = "#00008B"  # Dark blue
        entry_bg_color = "#f0f0f0"  # Light gray
        entry_fg_color = "#000000"  # Black
        button_bg_color = "#00008B"  # Dark blue
        button_fg_color = "#FFFFFF"  # White

        # Custom Fonts
        label_font = ("Arial", 12)
        entry_font = ("Arial", 12)

        master.configure(bg=label_bg_color)

        #window size
        master.geometry("1200x800")



        self.label = ttk.Label(master, text="Genetic Algorithm", font=label_font, background=label_bg_color, foreground=label_fg_color)
        self.label.pack(pady=3)

        self.population_size_label = ttk.Label(master, text="Population Size:", font=label_font, background=label_bg_color, foreground=label_fg_color)
        self.population_size_entry = ttk.Entry(master, font=entry_font, background=entry_bg_color, foreground=entry_fg_color)
        self.population_size_label.pack(pady=3)
        self.population_size_entry.pack(pady=3)

        self.generations_label = ttk.Label(master, text="Generations:", font=label_font, background=label_bg_color, foreground=label_fg_color)
        self.generations_entry = ttk.Entry(master, font=entry_font, background=entry_bg_color, foreground=entry_fg_color)
        self.generations_label.pack(pady=3)
        self.generations_entry.pack(pady=3)

        self.mutation_rate_label = ttk.Label(master, text="Mutation Rate (0-1):", font=label_font, background=label_bg_color, foreground=label_fg_color)
        self.mutation_rate_entry = ttk.Entry(master, font=entry_font, background=entry_bg_color, foreground=entry_fg_color)
        self.mutation_rate_label.pack(pady=3)
        self.mutation_rate_entry.pack(pady=3)

        self.satisfaction_value_label = ttk.Label(master, text="Satisfaction Value:", font=label_font, background=label_bg_color, foreground=label_fg_color)
        self.satisfaction_value_entry = ttk.Entry(master, font=entry_font, background=entry_bg_color, foreground=entry_fg_color)
        self.satisfaction_value_label.pack(pady=3)
        self.satisfaction_value_entry.pack(pady=3)

        self.fitness_function_label = ttk.Label(master, text="Fitness Function:", font=label_font, background=label_bg_color, foreground=label_fg_color)
        self.fitness_function_var = tk.StringVar()
        self.fitness_function_combobox = ttk.Combobox(master, textvariable=self.fitness_function_var, values=["Makespan", "Working Time"], font=entry_font, background=entry_bg_color, foreground=entry_fg_color)
        self.fitness_function_label.pack(pady=3)
        self.fitness_function_combobox.pack(pady=3)

        self.crossover_function_label = ttk.Label(master, text="Crossover Function:", font=label_font,
                                                  background=label_bg_color, foreground=label_fg_color)
        self.crossover_function_label.pack(pady=3)
        self.crossover_function_var = tk.StringVar()
        self.crossover_function_combobox = ttk.Combobox(master, textvariable=self.crossover_function_var,
                                                        values=["Normal Crossover", "Modified Order Crossover"],
                                                        font=entry_font, background=entry_bg_color,
                                                        foreground=entry_fg_color)
        self.crossover_function_combobox.pack(pady=3)

        self.run_button = ttk.Button(master, text="Run Genetic Algorithm", command=self.run_genetic_algorithm, style="Run.TButton")
        self.run_button.pack(pady=3)

        self.figure = Figure(figsize=(8, 6), dpi=100)  # Adjust figure size as needed
        self.canvas = FigureCanvasTkAgg(self.figure, master=master)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=3, pady=3)

        self.adjust_layout()

        # Set validation for entry widgets
        validate_cmd = master.register(self.validate_entry)
        self.population_size_entry.configure(validate="key", validatecommand=(validate_cmd, "%P"), invalidcommand=(validate_cmd, "%P"))
        self.generations_entry.configure(validate="key", validatecommand=(validate_cmd, "%P"), invalidcommand=(validate_cmd, "%P"))
        self.mutation_rate_entry.configure(validate="key", validatecommand=(validate_cmd, "%P"), invalidcommand=(validate_cmd, "%P"))
        self.satisfaction_value_entry.configure(validate="key", validatecommand=(validate_cmd, "%P"), invalidcommand=(validate_cmd, "%P"))

    def adjust_layout(self):
        pass

    def validate_entry(self, value):
        if value.strip() == "":
            return True
        if value.replace(".", "").isdigit():
            return True
        return False

    def run_genetic_algorithm(self):
        population_size = int(self.population_size_entry.get())
        generations = int(self.generations_entry.get())
        mutation_rate = float(self.mutation_rate_entry.get())
        satisfaction_value = int(self.satisfaction_value_entry.get())
        fitness_function = get_makespan if self.fitness_function_var.get() == "Makespan" else get_working_time
        crossover_function = make_crossover if self.crossover_function_var.get() == "Normal Crossover" else modified_order_crossover

        best_chromosome, makespan,gen = genetic_algorithm(jobs=Jobs, population_size=population_size,
                                                      generations=generations, mutation_rate=mutation_rate,
                                                      fitness_function=fitness_function,
                                                      satisfication_vlue=satisfaction_value,
                                                      crossover_function=crossover_function)

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        machines_process = machine_phases(best_chromosome)
        jobs = extract_jobs(machines_process)
        draw_gantt_chart(machines_process, jobs, ax=ax)
        self.canvas.draw()

root = tk.Tk()

# Customizing styles
style = ttk.Style(root)
style.configure("TLabel", foreground="#00008B", background="#87CEFA", font=("Arial", 12))
style.configure("TButton", foreground="#FFFFFF", background="#00008B", font=("Arial", 12))

my_gui = GUI(root)
root.mainloop()
