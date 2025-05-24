# tcp_udp_scanner
This is a Beginner level automation script to understand how the Nmap works, Using Nmap tool  I have written a automation script in python which scans the given input Private IP address in your wifi or ethernet enabled network connection and scans the ports which are used by TCP , UDP ports and returns port addresses which are vulnerable to exploitation in a detailed manner,
# 🔍 Nmap Port Scanner Automation Tool

A simple Python-based Nmap automation tool that allows you to run various types of network scans such as SYN ACK, UDP, and Comprehensive scans with ease. This tool leverages the powerful capabilities of [Nmap](https://nmap.org/) and its Python bindings to automate network reconnaissance tasks.

---

## 🧰 Features

- SYN ACK Scan (`-sS`)
- UDP Scan (`-sU`)
- Comprehensive Scan (`-sS -sV -sC -A -O`)
- Interactive terminal input for target IP and scan type
- Display of Nmap version, scan info, protocol details, and open ports

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Sure! Below is a detailed `README.md` file that includes:

* **Project description**
* **How to set it up**
* **Dependencies and installation steps**
* **Tool information**
* **Nmap official website link**
* **Usage instructions**

You can copy and paste this into your repository’s `README.md` file:

---

````markdown
# 🔍 Nmap Port Scanner Automation Tool

A simple Python-based Nmap automation tool that allows you to run various types of network scans such as SYN ACK, UDP, and Comprehensive scans with ease. This tool leverages the powerful capabilities of [Nmap](https://nmap.org/) and its Python bindings to automate network reconnaissance tasks.

---

## 🧰 Features

- SYN ACK Scan (`-sS`)
- UDP Scan (`-sU`)
- Comprehensive Scan (`-sS -sV -sC -A -O`)
- Interactive terminal input for target IP and scan type
- Display of Nmap version, scan info, protocol details, and open ports

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
````

### 2. Install Python

Ensure Python 3 is installed on your system. Download it from the official website:

* [https://www.python.org/downloads/](https://www.python.org/downloads/)

### 3. Install Nmap

Make sure Nmap is installed on your system.

#### 🔗 Official Nmap Download Links:

* **Windows:** [https://nmap.org/download.html#windows](https://nmap.org/download.html#windows)
* **Linux (Debian/Ubuntu):**

  ```bash
  sudo apt update
  sudo apt install nmap
  ```
* **macOS (via Homebrew):**

  ```bash
  brew install nmap
  ```

### 4. Set Up Python Environment

You can use `venv` or install dependencies globally.

#### Install `python-nmap` (Python binding for Nmap):

```bash
pip install python-nmap
```

---

## 📦 Dependencies

| Package       | Description              | Installation Command                                     |
| ------------- | ------------------------ | -------------------------------------------------------- |
| `nmap`        | Network scanning tool    | [Download from Nmap.org](https://nmap.org/download.html) |
| `python-nmap` | Python bindings for Nmap | `pip install python-nmap`                                |
| `python`      | Programming language     | [Download Python](https://python.org)                    |

---

## 🛠️ How to Use

1. Run the script:

   ```bash
   python your_script_name.py
   ```

2. Enter the target IP address when prompted.

3. Choose the scan type:

   * `1` → SYN ACK Scan
   * `2` → UDP Scan
   * `3` → Comprehensive Scan

4. The tool will display:

   * Nmap version
   * Scan info
   * Host status
   * Protocols scanned
   * Open ports

---

## ⚠️ Note

* **Root/Administrator Privileges:** Some scans (like SYN and UDP scans) require elevated privileges. Run the script with `sudo` on Unix systems or as Administrator on Windows.
* Ensure your usage complies with legal and ethical guidelines. Unauthorized scanning of networks can be illegal.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements

* [Nmap](https://nmap.org/)
* [python-nmap GitHub](https://github.com/alexxy/python-nmap)


