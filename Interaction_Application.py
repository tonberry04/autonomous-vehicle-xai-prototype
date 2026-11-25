import tkinter as tk
import os
import random

class AutonomousVehicleUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Autonomous Vehicle HCI Prototype")
        self.root.geometry("1280x720")
        self.root.resizable(False, False) 
        
        self.root.configure(bg="#2d2d2d")

        # Background Image Label
        self.label_bg = tk.Label(self.root, bg="#2d2d2d")
        self.label_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Scenarios mapped to specific PNG images
        self.scenarios = [
            {
                "title": "Pedestrian in Road",
                "life_threatening": True,
                "xai": "Critical hazard detected. Immediate stop required.",
                "optA": None,
                "optB": None,
                "image": "Emergency_Stop.png"
            },
            {
                "title": "Severe Fog & Low Visibility",
                "life_threatening": False,
                "xai": "Visibility < 10m. Sensor reliability dropping.",
                "optA": "Proceed Slowly",
                "optB": "Pull Over",
                "image": "Foggy_Road.png"
            },
            {
                "title": "Fallen Tree Blocking Path",
                "life_threatening": False,
                "xai": "Path fully blocked. Reverse required.",
                "optA": "Reverse & Reroute",
                "optB": "Wait for Clearance",
                "image": "Trees_On_Road.png"
            },
            {
                "title": "Active Road Works",
                "life_threatening": False,
                "xai": "Lane closed ahead. Merge required.",
                "optA": "Merge Right",
                "optB": "Wait for Gap",
                "image": "Road_Works.png"
            },
            {
                "title": "Broken Traffic Lights",
                "life_threatening": False,
                "xai": "Traffic Lights offline. Proceed with caution.",
                "optA": "Go ahead (No oncoming traffic)",
                "optB": "Stop",
                "image": "Traffic_Lights_Broken.png"
            }
        ]
        self.current_idx = -1

        # Interaction State
        self.user1_choice = None
        self.user2_choice = None
        self.time_left = 10
        self.timer_running = False

        self.setup_ui()
        self.reset_idle() # Load the clear road image initially


    def setup_ui(self):
        # UI Top Layer: Stimulus & XAI 
        self.label_title = tk.Label(self.root, text="DRIVING", font=("Segoe UI", 24, "bold"), bg="#2d2d2d", fg="white")
        self.label_title.pack(pady=15)

        self.label_xai = tk.Label(self.root, text="Cruising safely.", font=("Segoe UI", 16), bg="#444444", fg="#ffaa00", padx=20, pady=10)
        self.label_xai.pack(pady=5)

        self.label_timer = tk.Label(self.root, text="", font=("Segoe UI", 36, "bold"), bg="#2d2d2d", fg="#ff5555")
        self.label_timer.pack(pady=5)

        # UI Middle Layer: Passenger Inputs
        self.frame_controls = tk.Frame(self.root, bg="#2d2d2d")
        
        self.frame_controls.pack(pady=(200, 10))

        # User 1 Control Zone
        self.frame_u1 = tk.Frame(self.frame_controls, bg="#333333", padx=20, pady=20, bd=2, relief=tk.RIDGE)
        self.frame_u1.pack(side=tk.LEFT, expand=True, padx=20)
        tk.Label(self.frame_u1, text="User 1", font=("Segoe UI", 16), bg="#333333", fg="#88ccff").pack(pady=5)
        self.btn_u1_a = tk.Button(self.frame_u1, text="Opt A", font=("Segoe UI", 14), width=15, command=lambda: self.vote(1, "A"), state=tk.DISABLED)
        self.btn_u1_a.pack(pady=5)
        self.btn_u1_b = tk.Button(self.frame_u1, text="Opt B", font=("Segoe UI", 14), width=15, command=lambda: self.vote(1, "B"), state=tk.DISABLED)
        self.btn_u1_b.pack(pady=5)
        self.label_u1_status = tk.Label(self.frame_u1, text="", bg="#333333", fg="white", font=("Segoe UI", 12))
        self.label_u1_status.pack(pady=5)

        # User 2 Control Zone
        self.frame_u2 = tk.Frame(self.frame_controls, bg="#333333", padx=20, pady=20, bd=2, relief=tk.RIDGE)
        self.frame_u2.pack(side=tk.RIGHT, expand=True, padx=20)
        tk.Label(self.frame_u2, text="User 2", font=("Segoe UI", 16), bg="#333333", fg="#88ccff").pack(pady=5)
        self.btn_u2_a = tk.Button(self.frame_u2, text="Opt A", font=("Segoe UI", 14), width=15, command=lambda: self.vote(2, "A"), state=tk.DISABLED)
        self.btn_u2_a.pack(pady=5)
        self.btn_u2_b = tk.Button(self.frame_u2, text="Opt B", font=("Segoe UI", 14), width=15, command=lambda: self.vote(2, "B"), state=tk.DISABLED)
        self.btn_u2_b.pack(pady=5)
        self.label_u2_status = tk.Label(self.frame_u2, text="", bg="#333333", fg="white", font=("Segoe UI", 12))
        self.label_u2_status.pack(pady=5)

        # Trigger Button
    
        self.btn_trigger = tk.Button(self.root, text="Simulate Next Scenario", font=("Segoe UI", 14, "bold"), bg="#007bff", fg="white", command=self.next_scenario)
        self.btn_trigger.pack(pady=10)

    # Update Button States
    def update_button_states(self, state, scenario=None):
        if scenario:
            self.btn_u1_a.config(state=state, text=scenario["optA"])
            self.btn_u1_b.config(state=state, text=scenario["optB"])
            self.btn_u2_a.config(state=state, text=scenario["optA"])
            self.btn_u2_b.config(state=state, text=scenario["optB"])
        else:
            self.btn_u1_a.config(state=state, text="Opt A")
            self.btn_u1_b.config(state=state, text="Opt B")
            self.btn_u2_a.config(state=state, text="Opt A")
            self.btn_u2_b.config(state=state, text="Opt B")

    def next_scenario(self):
        self.current_idx = (self.current_idx + 1) % len(self.scenarios)
        scenario = self.scenarios[self.current_idx]

        # Update Background Image and Text
        self.set_background(scenario["image"])
        self.label_title.config(text=scenario["title"], fg="white")
        self.label_xai.config(text=scenario["xai"], bg="#444444", fg="#ffaa00")
        self.btn_trigger.config(state=tk.DISABLED)

        
        if scenario["life_threatening"]:
            self.resolve("EMERGENCY STOP\n(Life Threatening Bypass)", "#ff3333")
            return

        # Random Time
        self.time_left = random.randint(8, 22) 

        self.user1_choice = None
        self.user2_choice = None
        self.update_button_states(tk.NORMAL, scenario)
        self.label_u1_status.config(text="")
        self.label_u2_status.config(text="")
        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if not self.timer_running:
            return

        self.label_timer.config(text=f"{self.time_left}s")

        if self.time_left <= 0:
            self.timer_running = False
            
            scenario = self.scenarios[self.current_idx]
            
            # Implied Consent Logic
            if self.user1_choice and not self.user2_choice:
                action = scenario["optA"] if self.user1_choice == "A" else scenario["optB"]
                self.resolve(f"ACTION EXECUTED: {action}\n(User 1 Override - User 2 Inactive)", "#33cc33")
                
            elif self.user2_choice and not self.user1_choice:
                action = scenario["optA"] if self.user2_choice == "A" else scenario["optB"]
                self.resolve(f"ACTION EXECUTED: {action}\n(User 2 Override - User 1 Inactive)", "#33cc33")
                
            else:
                # Total Inaction
                self.resolve("EMERGENCY STOP\n(Timeout / Total Inaction)", "#ff3333")
        else:
            self.time_left -= 1
            self.root.after(1000, self.update_timer)

    def vote(self, user, choice):
        if not self.timer_running: return

        if user == 1:
            self.user1_choice = choice
            self.label_u1_status.config(text=f"Selected: {choice}")
        else:
            self.user2_choice = choice
            self.label_u2_status.config(text=f"Selected: {choice}")

        self.check_logic()

    def check_logic(self):
        
        if self.user1_choice and self.user2_choice:
            
            # Compare Options Chosen
            if self.user1_choice == self.user2_choice:
                scenario = self.scenarios[self.current_idx]
                action = scenario["optA"] if self.user1_choice == "A" else scenario["optB"]
                
                # Continue using Action A / Action B
                self.resolve(f"ACTION EXECUTED: {action}\n(Consensus Reached)", "#33cc33")
            else:
                # Conflicting Options
                self.user1_choice = None
                self.user2_choice = None
                self.label_u1_status.config(text="")
                self.label_u2_status.config(text="")
                self.label_xai.config(text="CONFLICT DETECTED! Re-select matching options.", bg="#aa0000", fg="white")


    #Loading Images from PC
    def set_background(self, image_filename):
        try:
            
            base_dir = os.path.dirname(os.path.abspath(__file__))
            
           
            image_path = os.path.join(base_dir, image_filename)
            
            
            self.bg_photo = tk.PhotoImage(file=image_path)
            self.label_bg.config(image=self.bg_photo)
        except Exception as e:
            
            print(f"FAILED TO LOAD: Tried looking for {image_path}")
            print(f"Error details: {e}")

    def resolve(self, message, color):
        self.timer_running = False
        self.update_button_states(tk.DISABLED)
        self.label_timer.config(text="")
        self.label_title.config(text=message, fg=color)
        self.root.after(3500, self.reset_idle)

    def reset_idle(self):
        self.set_background("Clear_Road.png")
        self.label_title.config(text="DRIVING", fg="white")
        self.label_xai.config(text="Cruising safely. No intervention required.", bg="#444444", fg="#ffaa00")
        self.btn_trigger.config(state=tk.NORMAL)
        self.label_u1_status.config(text="")
        self.label_u2_status.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutonomousVehicleUI(root)
    root.mainloop()