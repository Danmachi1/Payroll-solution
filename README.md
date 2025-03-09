# CRF Management Tool

## 📌 Overview
The **CRF Management Tool** is a **Java-based desktop application** designed to streamline the management of **CRF (Change Request Forms), PSL Tracking, Meeting Notes, Tasks, and Reminders** within an organization. The tool provides an intuitive **graphical user interface (GUI)** using **Java Swing** and follows a **modular** and **extendable** design.

---

## 🚀 Features

- **📊 Dashboard** – Provides an overview of active tasks, reminders, and PSL tracking.
- **📂 PSL Tracker** – Helps users track PSL (Project Status Logs) efficiently.
- **📅 Reminders & Task Management** – Allows users to create, update, and manage their work tasks.
- **📝 Meeting Notes** – Easily take and organize meeting notes, linked with reminders.
- **🔧 Settings Panel** – Customize the tool’s behavior and settings.
- **📅 Outlook Calendar Integration** – Directly opens Outlook calendar for scheduling.
- **🖥️ Multi-Window Support** – Uses `JDesktopPane` for a tab-like multi-panel interface.
- **⚡ Lightweight & Responsive** – Built with Java Swing for fast execution.

---

## 🏗️ Tech Stack

- **Java 11+**
- **Swing GUI** (`JInternalFrame`, `JDesktopPane`, `JPanel`)
- **Maven (for dependencies)**
- **Microsoft Outlook Integration** (for calendar)

---

## 🎯 Installation & Usage

### 🔹 Prerequisites:
- Install **Java 11+**
- Install **Maven** (if building from source)
- Ensure **Outlook** is installed (for Calendar Integration)

### 🔹 Running the Application:
1. **Clone the Repository**  
   ```sh
   git clone https://github.com/your-github-username/CRF-Management-Tool.git
   cd CRF-Management-Tool
   ```
2. **Compile and Run**  
   ```sh
   mvn clean install
   java -jar target/CRFManagementTool.jar
   ```
   *OR, if running directly from Eclipse:*
   - Open the project in **Eclipse**.
   - Right-click `MainApp.java` → **Run As** → **Java Application**.

---

## 🖥️ UI Overview

### 🌟 Main Dashboard
![Dashboard Screenshot](assets/screenshots/dashboard.png)

### 📂 PSL Tracker
![PSL Tracker](assets/screenshots/psl_tracker.png)

### 📅 Meeting Notes & Tasks
![Meeting Notes](assets/screenshots/meeting_notes.png)

---

## ⚙️ Project Structure

```
📦 com.crfmanagement
 ┣ 📂 gui
 ┃ ┣ 📜 MainApp.java  # Entry point of the application
 ┃ ┣ 📜 DashboardPanel.java
 ┃ ┣ 📜 PSLTrackerPanel.java
 ┃ ┣ 📜 MeetingNotesPanel.java
 ┃ ┣ 📜 RemindersPanel.java
 ┃ ┣ 📜 TaskManagementPanel.java
 ┃ ┗ 📜 SettingsPanel.java
 ┣ 📂 utils
 ┃ ┗ 📜 UIUtils.java  # Helper methods for UI customization
 ┣ 📜 pom.xml  # Maven project dependencies
 ┣ 📜 README.md  # This file
 ┣ 📜 LICENSE  # Open-source license
 ┗ 📂 assets
   ┗ 📂 screenshots  # UI images for README
```

---

## 🛠️ Future Enhancements
- **🌐 Database Support** – Store PSL, tasks, and reminders in an SQLite or PostgreSQL database.
- **📤 Export to Excel** – Add CSV/Excel export for PSL Tracking.
- **🔔 Notifications** – Implement system tray reminders for important tasks.

---

## 🤝 Contributing
1. **Fork** the repository.
2. **Clone** your fork:  
   ```sh
   git clone https://github.com/your-username/CRF-Management-Tool.git
   ```
3. **Create a new branch**:  
   ```sh
   git checkout -b feature-new-enhancement
   ```
4. **Commit your changes** and push to your fork.
5. **Submit a Pull Request (PR).**

---

## 📄 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact
📧 **Salah Chouhaib** – *Developer & Project Manager*  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/your-profile)  
📂 [GitHub](https://github.com/your-github-username)  

**Made with ❤️ in Java**
  
