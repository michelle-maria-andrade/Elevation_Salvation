# Elevation Salvation

This repository contains the environment assets and scripts for the Elevation Salvation task.

---

## Important: Git LFS Required
This repository uses **Git Large File Storage (LFS)** to manage large environment files (like `Africa_Savannah.zip`). 

To clone this repository correctly, you **must** have Git LFS installed on your system.

---

### Installation & Cloning

1.  **Install Git LFS**:
    * **Ubuntu/Debian**: `sudo apt install git-lfs`
    * **Fedora**: `sudo dnf install git-lfs`
    * **Windows**: Download from [git-lfs.github.com](https://git-lfs.github.com/)

2.  **Initialize LFS**:
    ```bash
    git lfs install
    ```

3.  **Clone the Repo**:
    ```bash
    git clone [https://github.com/michelle-maria-andrade/Elevation_Salvation.git](https://github.com/michelle-maria-andrade/Elevation_Salvation.git)
    cd Elevation_Salvation
    ```

4.  **Pull Large Files** (If they didn't download automatically):
    ```bash
    git lfs pull
    ```

---

### Project Structure
* **Africa_Savannah.zip**: The compressed Unreal Engine environment.
* **boundary.txt**: Coordinates for the simulation flight boundaries.
* **get_data.py**: Script for extracting telemetry/sensor data from the simulation.

---

### Usage
1.  Unzip `Africa_Savannah.zip`.
2.  Run the executable within the unzipped folder.
3.  Use `get_data.py` to interface with the simulation.