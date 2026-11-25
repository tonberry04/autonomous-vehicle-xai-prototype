# autonomous-vehicle-xai-prototype

**Prose word count:** ~448 words

## Project Status
This repository contains a desktop prototype simulating a dual-passenger Explainable AI (XAI) interface for an autonomous vehicle during ambiguous driving edge cases.

- **Implemented:** Dual-passenger voting interface, consensus detection, conflict-retry looping, single-user implied-consent override on timeout, and automatic emergency stop bypass for life-threatening hazards.
- **Simulated:** Five hardcoded driving scenarios, static PNG road scenes, hardcoded XAI status messages, and randomized decision windows (8–22 seconds).
- **Planned:** Auditory urgency alerts for distracted passengers, live perception/sensor integration, and physical vehicle actuation.

## Technology Stack
- **Python 3 & Tkinter:** Core language and GUI framework used to build the window layout, button states, and event-driven countdown timer.
- **Standard Libraries (`os`, `random`):** Used for relative asset path resolution and randomized scenario timers.
- **Undecided:** Audio playback library (e.g., `playsound` vs. `pygame`) for the planned auditory alert module.

## Running the Prototype
No external `pip` packages are required; the prototype uses Python's built-in standard library.

1. Clone the repository and ensure all scenario PNGs (`Clear_Road.png`, `Emergency_Stop.png`, `Foggy_Road.png`, `Trees_On_Road.png`, `Road_Works.png`, `Traffic_Lights_Broken.png`) are in the same directory as the script.
2. Run the application:

```bash
git clone https://github.com/tonberry04/autonomous-vehicle-xai-prototype.git
cd autonomous-vehicle-xai-prototype
python Interaction_Application.py
```
3. Click **Simulate Next Scenario** to cycle through the five test cases and inspect consensus, conflict, single-user override, and timeout behaviors.


## Development Record
- **Stage 1 – Initial GUI & Layout:** Built the base Tkinter window (`1280x720`) with top XAI banners and dual-passenger control panels. Verified window scaling and disabled/enabled button states.
- **Stage 2 – Interactive Decision Logic:** Implemented `check_logic()` and `update_timer()` to handle matching votes, conflict resets without restarting the timer, implied-consent overrides, and immediate life-threatening bypasses. Manually tested all five interaction outcomes.
- **Stage 3 – Scenario Assets & Timing:** Added the five road scenarios, mapped local PNG backgrounds via `set_background()`, and added randomized 8–22s timers to simulate variable urgency. Checked relative path loading across runs.

## AI Assistance
- **Code & Debugging (Gemini Pro 3.1):** Used to scaffold the initial Tkinter class structure, troubleshoot image-loading logic, and debug edge cases. I wrote the core interactive logic manually, adapted the timer and scenario definitions to match Assignment 1, and manually tested every branch to verify clean state resets. The Tkinter class was further modified to match the specifications required for this project, including fixed window sizing to prevent misaligned backgrounds.
- **Visual Assets (Gemini Pro 3.1):** Used to generate the background road-scenario PNGs for the application (the storyboards themselves are screenshots of the running application, which partially display these images). I reviewed each image to ensure it matched its corresponding hazard prompt.
- **Documentation:** Gemini was used to help structure and format this README, which I reviewed and edited for accuracy. 

## Additional Files
All source code and scenario PNG assets are included directly in this repository. No accompanying ZIP file is required.
