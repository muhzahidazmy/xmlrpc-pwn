# ⚔️ XMLRPC-Attack

**XMLRPC-Attack** is a powerful yet lightweight tool for identifying and exploiting vulnerabilities in **XML-RPC endpoints**, commonly found in platforms like **WordPress**.  
Designed for **penetration testers** and **security researchers**, it allows brute-force testing, method enumeration, and targeted calls to exposed XML-RPC methods.

---

## 🔥 Features

- 🔐 **Brute Force Login** – Attempts login using `system.multicall` with a supplied username and password list
- 💣 **Denial of Service (DOS)** – Exploits XML-RPC to overwhelm the server with resource-heavy calls
- 🔍 **Method Enumeration** – Lists available XML-RPC methods on the server
- 📄 **Readable Output** – Clean, color-coded CLI results for easy analysis
<!-- - 🌐 **Endpoint Detection** – Coming soon: detect presence of XML-RPC endpoints -->

---

## ⚙️ Requirements

- Python **3.8+**
- No external libraries required (built-in modules only)

---

## 🚀 Installation

```bash
git clone https://github.com/ForwardEcho/xmlrpc-attack.git
cd xmlrpc-attack
chmod +x xmlrpcattack.py
