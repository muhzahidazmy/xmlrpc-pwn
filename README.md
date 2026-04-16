# ⚔️ XMLRPC-Attack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Purpose-Ethical%20Hacking-red?style=for-the-badge" />
</p>

**XMLRPC-Attack** is a powerful yet lightweight tool for identifying and exploiting vulnerabilities in **XML-RPC endpoints**, commonly found in platforms like **WordPress**.  
Designed for **penetration testers** and **security researchers**, it supports brute-force credential testing, method enumeration, and direct method invocation against exposed XML-RPC interfaces.

> ⚠️ **DISCLAIMER**: This tool is intended **for educational purposes and authorized penetration testing only**. Unauthorized use against systems you do not own or have explicit permission to test is **illegal** and punishable by law. The author assumes no responsibility for misuse.

---

## 🔥 Features

| Feature | Description |
|---|---|
| 🔐 **Brute Force Login** | Attempts login via `wp.getUsersBlogs` with a supplied username and password list |
| 🔍 **Method Enumeration** | Lists all available XML-RPC methods exposed on the target server |
| 📞 **Direct Method Call** | Invokes any specific XML-RPC method with custom parameters |
| 🎨 **Color-Coded Output** | Clean, readable CLI output with color-highlighted results |

---

## ⚙️ Requirements

- Python **3.8+**
- **No external dependencies** — uses built-in `xmlrpc.client` and `argparse` modules only

---

## 🚀 Installation

```bash
git clone https://github.com/ForwardEcho/xmlrpc-attack.git
cd xmlrpc-attack
chmod +x xmlrpcattack.py   # Linux/macOS only
```

---

## 📖 Usage

```
python xmlrpcattack.py -u <URL> [options]
```

### Arguments

| Flag | Long Flag | Description |
|---|---|---|
| `-u` | `--url` | **(Required)** URL of the target XML-RPC endpoint |
| `-l` | `--list` | List all available methods on the server |
| `-m` | `--method` | Call a specific XML-RPC method |
| `-U` | `--user` | Username for brute force attack |
| `-P` | `--passwords` | Path to a wordlist file for brute force |

---

## 💡 Examples

### 1. Enumerate Available Methods
```bash
python xmlrpcattack.py -u http://target.com/xmlrpc.php --list
```

### 2. Brute Force Login
```bash
python xmlrpcattack.py -u http://target.com/xmlrpc.php -U admin -P wordlist.txt
```

### 3. Call a Specific Method
```bash
python xmlrpcattack.py -u http://target.com/xmlrpc.php -m wp.getUsersBlogs admin password123
```

### 4. Call `system.multicall` with Paired Parameters
```bash
python xmlrpcattack.py -u http://target.com/xmlrpc.php -m system.multicall wp.getUsersBlogs admin
```

---

## 📁 Project Structure

```
xmlrpc-attack/
├── xmlrpcattack.py   # Main script
├── README.md         # Documentation
└── wordlist.txt      # (Optional) Password wordlist for brute force
```

---

## 🧠 How It Works

XML-RPC is a remote procedure call protocol that uses XML to encode requests and HTTP as the transport mechanism. WordPress exposes an `xmlrpc.php` endpoint that, when not properly secured, can be exploited via:

- **Credential stuffing / brute force** — using `system.multicall` or `wp.getUsersBlogs` to test many passwords efficiently
- **Information disclosure** — enumerating all supported methods via `system.listMethods()`
- **Unauthorized actions** — calling privileged methods directly if authentication is weak

---

## 🛡️ Ethical Use & Legal Notice

This tool is strictly for use in:
- **Authorized penetration testing** engagements
- **CTF (Capture The Flag)** competitions
- **Research on systems you own or have written permission to test**

**Do not use this tool against systems without explicit permission.** The author (**ForwardEcho**) is not responsible for any damage caused by misuse of this software.

---

## 👤 Author

**ForwardEcho**  
Cybersecurity Enthusiast | Ethical Hacker | Security Researcher

- GitHub: [@ForwardEcho](https://github.com/ForwardEcho)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
