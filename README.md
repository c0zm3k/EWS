# Student Risk Monitor | Analytics Command Center

A high-fidelity, industrial skeuomorphic web application for monitoring and predicting student academic risk. This system transforms raw academic data into tactical diagnostic readouts using a tactile control panel interface.

## 🕹️ System Interface
The UI is designed as an **Industrial Control Panel**, featuring:
- **Tactile Tactility**: Physical bevels, recessed wells, and brushed metal textures.
- **Dynamic Telemetry**: LED status indicators (Nominal vs. Alert) and glowing technical readouts.
- **Interactive Analytics**: Enlargable high-resolution charts for variance visualization.

![System Terminal](C:/Users/LENOVO/.gemini/antigravity/brain/baa3ddde-fb43-4249-852f-a9a2fd509f53/media__1770223052787.png)
*Active System Terminal for data input.*

## 🚀 Key Features
- **Predictive Engine**: Analyzes Attendance, Midterm Scores, and CGPA to determine unit risk probability.
- **Unit Diagnostic Panels**: Individual high-fidelity readouts for every student, featuring "System Tech Notes" and personalized monikers.
- **Name-Enabled Pipeline**: Full support for student names throughout the data stream and UI.
- **Data Export/Import**: Integrated demo data generator for system calibration and testing.

![Dashboard Overview](C:/Users/LENOVO/.gemini/antigravity/brain/baa3ddde-fb43-4249-852f-a9a2fd509f53/media__1770223052761.png)
*Tactical Monitoring Log and real-time status telemetry.*

![High-Resolution Analytics](C:/Users/LENOVO/.gemini/antigravity/brain/baa3ddde-fb43-4249-852f-a9a2fd509f53/media__1770223052790.png)
*Detailed variance visualization with percentage readouts.*

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8+
- Git

### Initializing Terminal
1. **Clone/Setup Repository**:
   ```bash
   git clone <repository-url>
   cd EWS
   ```

2. **Configure Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Calibrate Demo Data**:
   ```bash
   python scripts/create_demo.py
   ```

4. **Launch Analysis Stream**:
   ```bash
   python app.py
   ```
   *Access the terminal at: http://127.0.0.1:5000*

## 📁 Project Architecture
- `app.py`: Main Analytics Engine & Flask Server.
- `templates/`: Tactical UI layouts (`index.html`, `dashboard.html`).
- `static/css/style.css`: Skeuomorphic design system & color tokens.
- `models/`: Trained logistic regression and decision tree pickels.
- `scripts/`: System utility tools (Demo generation).
- `data/`: Protected data stream storage (Uploads/Static).

## 🛡️ Version Control
The project is initialized with Git. Sensitive binaries and temporary caches are filtered via `.gitignore`.
