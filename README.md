<div align="center">

<img src="https://raw.githubusercontent.com/dehyasec/dehyasec/main/assets/banner.svg?v=6" width="100%" alt="DEHYASEC. Cybersecurity student building practical tools and exploring network security, Linux and Python automation.">

<a href="https://github.com/dehyasec?tab=repositories"><img src="https://raw.githubusercontent.com/dehyasec/dehyasec/main/assets/btn-projects.svg?v=6" height="36" alt="GitHub projects"></a>
<a href="https://tryhackme.com/p/shaikhdehya"><img src="https://raw.githubusercontent.com/dehyasec/dehyasec/main/assets/btn-tryhackme.svg?v=6" height="36" alt="TryHackMe profile"></a>
<a href="https://profile.hackthebox.com/profile/01a12bed-bdea-714d-9178-494ccdd1038d"><img src="https://raw.githubusercontent.com/dehyasec/dehyasec/main/assets/btn-htb.svg?v=6" height="36" alt="Hack The Box profile"></a>
<a href="https://www.linkedin.com/in/dehya-shaikh-8610a8381/"><img src="https://raw.githubusercontent.com/dehyasec/dehyasec/main/assets/btn-linkedin.svg?v=6" height="36" alt="LinkedIn profile"></a>

<img src="https://raw.githubusercontent.com/dehyasec/dehyasec/main/assets/terminal.svg?v=6" width="100%" alt="Profile card. Identity: DEHYASEC. Role: Cybersecurity student. Interests: network security, Linux, Python. Practice: CTFs and authorized security labs. Projects: Python security utilities. Principle: learn, test, document, improve.">

</div>

## About

I'm Dehya, a cybersecurity student. I learn by building small, documented tools in a Kali Linux lab and by practicing on TryHackMe and Hack The Box. I care about both sides of security, offensive and defensive, and I only test systems I own or have explicit permission to test.

## Current focus

| Track | Studying |
|---|---|
| **Offensive** | Recon and enumeration, port scanning, web application basics, CTF challenges |
| **Defensive** | Log analysis, brute-force detection, file integrity monitoring, incident response basics |
| **Foundations** | TCP/IP, Linux administration, Python scripting, cryptography basics |

## Featured projects

<a href="https://github.com/dehyasec/port-scanner"><img src="https://raw.githubusercontent.com/dehyasec/dehyasec/main/assets/project-1-port-scanner.svg?v=6" width="100%" alt="Port scanner icon, project 1 of 3"></a>

### [port-scanner](https://github.com/dehyasec/port-scanner)

A multi-threaded TCP port scanner in Python, built to understand how network scanning works.

- Scans a configurable port range with adjustable threads and timeout
- Lists open ports with their common service names
- Validates input and exits cleanly on bad hosts, ranges or Ctrl+C

`python` `networking` `sockets` `multithreading`

**Scope:** it reports TCP ports that accept a connection. Service names come from a standard port lookup, not from probing the service. Use it only on systems you are authorized to test.

[View repository](https://github.com/dehyasec/port-scanner)

<a href="https://github.com/dehyasec/log-analyzer"><img src="https://raw.githubusercontent.com/dehyasec/dehyasec/main/assets/project-2-log-analyzer.svg?v=6" width="100%" alt="Log analyzer icon, project 2 of 3"></a>

### [log-analyzer](https://github.com/dehyasec/log-analyzer)

A defensive tool that reads Linux SSH authentication logs and flags suspicious login patterns.

- Detects bursts of failed logins from one IP within a configurable time window
- Separates fast brute-force bursts from slow, low-rate attempts
- Warns when a flagged IP also has a successful login

`python` `blue-team` `log-analysis` `ssh`

**Reading the output:** a flag means a log pattern deserves a closer look, not that an attack happened or succeeded. It only parses OpenSSH password events, so it won't see attempts spread across many IPs or events that never reach those log lines.

[View repository](https://github.com/dehyasec/log-analyzer)

<a href="https://github.com/dehyasec/file-integrity-monitor"><img src="https://raw.githubusercontent.com/dehyasec/dehyasec/main/assets/project-3-file-integrity-monitor.svg?v=6" width="100%" alt="File integrity monitor icon, project 3 of 3"></a>

### [file-integrity-monitor](https://github.com/dehyasec/file-integrity-monitor)

A defensive tool that records SHA-256 hashes of a directory and reports new, modified and deleted files.

- Builds a hash baseline and compares later scans against it
- Supports ignore patterns and `--update` to accept expected changes
- Exits with code 0 or 1 so scripts can react to changes

`python` `blue-team` `file-integrity` `sha256`

**Limits:** it detects changes after they happen and does not prevent tampering. Keep the baseline where an attacker on the system can't edit it, and treat a reported change as something to investigate, not proof of compromise.

[View repository](https://github.com/dehyasec/file-integrity-monitor)

## Toolkit

| Area | Skills |
|---|---|
| **Programming** | Python (used in all three projects), Bash (learning) |
| **Systems** | Linux, Kali Linux in a VirtualBox lab |
| **Foundations** | TCP/IP, networking, authentication logs, file integrity monitoring |
| **Practice** | CTFs, TryHackMe, Hack The Box (learning) |

## Learning lab

> No writeups yet, and nothing is listed until it exists. This is where CTF and lab writeups, networking and Linux notes, lessons from security labs and small experiments will go.

## GitHub activity

<p align="center"><img src="https://raw.githubusercontent.com/dehyasec/dehyasec/main/assets/stats-card.svg?v=6" width="560" alt="Public GitHub activity: repositories, commits and languages, generated from the GitHub API."></p>

## Learning roadmap

- [x] GitHub profile and README
- [x] Kali Linux home lab
- [x] Three Python security tools published: port-scanner, log-analyzer, file-integrity-monitor
- [ ] Complete TryHackMe Pre Security, then Cyber Security 101
- [ ] Next tool: password hash auditor
- [ ] Publish the first CTF writeups
- [ ] Entry-level certification (Security+ or eJPT)
- [ ] Cybersecurity internship

## Contact

[LinkedIn](https://www.linkedin.com/in/dehya-shaikh-8610a8381/) · [TryHackMe](https://tryhackme.com/p/shaikhdehya) · [Hack The Box](https://profile.hackthebox.com/profile/01a12bed-bdea-714d-9178-494ccdd1038d) · [Email](mailto:shaikhdehya@gmail.com)

**Responsible use.** Everything here is for education. I only test systems I own or have explicit permission to test, and I keep offensive work inside authorized labs.

<p align="center"><img src="https://raw.githubusercontent.com/dehyasec/dehyasec/main/assets/footer.svg?v=6" width="100%" alt="BLACKSITE by DEHYASEC"></p>
