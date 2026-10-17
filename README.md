<div align="center">

<img src="https://raw.githubusercontent.com/dehyasec/dehyasec/main/assets/banner.svg?v=5" width="100%" alt="DEHYASEC, cybersecurity student. Abstract network diagram with the label BLACKSITE and the note: authorized lab testing only.">

<a href="https://github.com/dehyasec?tab=repositories"><img src="https://raw.githubusercontent.com/dehyasec/dehyasec/main/assets/btn-projects.svg?v=5" height="44" alt="GitHub projects"></a>
<a href="https://tryhackme.com/p/shaikhdehya"><img src="https://raw.githubusercontent.com/dehyasec/dehyasec/main/assets/btn-tryhackme.svg?v=5" height="44" alt="TryHackMe profile"></a>
<a href="https://profile.hackthebox.com/profile/01a12bed-bdea-714d-9178-494ccdd1038d"><img src="https://raw.githubusercontent.com/dehyasec/dehyasec/main/assets/btn-htb.svg?v=5" height="44" alt="Hack The Box profile"></a>
<a href="https://www.linkedin.com/in/dehya-shaikh-8610a8381/"><img src="https://raw.githubusercontent.com/dehyasec/dehyasec/main/assets/btn-linkedin.svg?v=5" height="44" alt="LinkedIn profile"></a>

**Cybersecurity student exploring network security, penetration testing, Linux and Python automation.**

</div>

```text
# profile.txt
name      Dehya (dehyasec)
role      cybersecurity student
focus     network security, pentesting,
          Linux, Python automation
lab       Kali Linux in VirtualBox,
          TryHackMe, Hack The Box
building  port-scanner, log-analyzer,
          file-integrity-monitor
ethics    authorized, lab-only testing
```

## About

I'm a cybersecurity student who learns by building. I use a Kali Linux lab, hands-on platforms and small Python projects to turn concepts into working tools.

- **Learning now:** TCP/IP networking, Linux administration, web application basics and Python scripting.
- **Building:** small security tools. So far a port scanner, an SSH log analyzer and a file integrity monitor.
- **Both sides of security:** offensive (recon, scanning, pentesting basics) and defensive (log analysis, detection, integrity monitoring).
- **How I practice:** hands-on labs, CTFs and practical projects on TryHackMe and Hack The Box.
- **Ethics:** I only test systems I own or have explicit permission to test.

## Current focus areas

| Area | What I'm studying |
|---|---|
| **Offensive fundamentals** | Recon and enumeration, port scanning, web application basics (OWASP Top 10), CTF challenges |
| **Defensive fundamentals** | Log analysis, brute-force detection, file integrity monitoring, incident response basics |
| **Foundations** | TCP/IP, Linux administration, Python scripting, cryptography basics |

## Featured projects

Three small tools built while learning. Each repository has usage docs, an ethical-use note and a roadmap.

<table>
  <tr>
    <td width="72" align="center" valign="top"><img src="https://raw.githubusercontent.com/dehyasec/dehyasec/main/assets/icon-port-scanner.svg?v=5" width="48" height="48" alt="Port scanner icon"></td>
    <td>
      <h3><a href="https://github.com/dehyasec/port-scanner">port-scanner</a></h3>
      <p>Multi-threaded TCP port scanner in Python, built to understand how network scanning works.</p>
      <p><code>python</code> <code>networking</code> <code>port-scanner</code> <code>security-tools</code></p>
      <p><b>Implemented</b></p>
      <ul>
        <li>Multi-threaded TCP scanning with an adjustable thread count</li>
        <li>Configurable port range and per-port timeout</li>
        <li>Service name shown for each open port</li>
        <li>Handles invalid hosts, bad port ranges and Ctrl+C cleanly</li>
      </ul>
      <p><b>Planned:</b> banner grabbing, JSON / CSV output, UDP scanning, multiple hosts</p>
      <p><a href="https://github.com/dehyasec/port-scanner">View repository</a></p>
    </td>
  </tr>
  <tr>
    <td width="72" align="center" valign="top"><img src="https://raw.githubusercontent.com/dehyasec/dehyasec/main/assets/icon-log-analyzer.svg?v=5" width="48" height="48" alt="Log analyzer icon"></td>
    <td>
      <h3><a href="https://github.com/dehyasec/log-analyzer">log-analyzer</a></h3>
      <p>Defensive tool that reads Linux authentication logs and flags suspicious SSH login patterns.</p>
      <p><code>python</code> <code>blue-team</code> <code>log-analysis</code> <code>ssh</code></p>
      <p><b>Implemented</b></p>
      <ul>
        <li>Parses failed and successful SSH logins with regular expressions</li>
        <li>Sliding-window burst detection with adjustable window and threshold</li>
        <li>Separates fast brute-force bursts from slow attackers</li>
        <li>Warns when a flagged IP also logged in successfully</li>
        <li>Reads a log file or stdin (works with <code>journalctl</code> output); ships with a sample log</li>
      </ul>
      <p><b>Planned:</b> invalid-user scan and key-based attack detection, JSON / CSV export, IP geolocation and allow-lists</p>
      <p><a href="https://github.com/dehyasec/log-analyzer">View repository</a></p>
    </td>
  </tr>
  <tr>
    <td width="72" align="center" valign="top"><img src="https://raw.githubusercontent.com/dehyasec/dehyasec/main/assets/icon-file-integrity.svg?v=5" width="48" height="48" alt="File integrity monitor icon"></td>
    <td>
      <h3><a href="https://github.com/dehyasec/file-integrity-monitor">file-integrity-monitor</a></h3>
      <p>Defensive tool that uses SHA-256 hashes to find new, modified and deleted files.</p>
      <p><code>python</code> <code>blue-team</code> <code>file-integrity</code> <code>sha256</code></p>
      <p><b>Implemented</b></p>
      <ul>
        <li>SHA-256 baseline of every file in a directory</li>
        <li>Reports modified, new and deleted files</li>
        <li>Glob ignore patterns (including whole folders) and <code>--update</code> to accept expected changes</li>
        <li>Exit code 0 (clean) or 1 (changes found), so scripts can react</li>
      </ul>
      <p><b>Planned:</b> permission and ownership tracking, hash-algorithm option, JSON report output, scheduled checks with alerts</p>
      <p><a href="https://github.com/dehyasec/file-integrity-monitor">View repository</a></p>
    </td>
  </tr>
</table>

## Toolkit

| Area | Skills | Status |
|---|---|---|
| **Programming** | Python, Bash | Python used in all three projects; Bash still learning |
| **Systems** | Linux, Kali Linux | Kali lab in VirtualBox; Linux admin still learning |
| **Security basics** | TCP/IP, networking, auth logs, file integrity monitoring, port scanning | Studying, applied in my projects |
| **Practice** | CTFs, TryHackMe, Hack The Box | Learning |

## Learning lab

No writeups are published yet, and nothing is listed here until it exists. This space is reserved for:

- CTF and lab writeups from TryHackMe and Hack The Box
- Notes on networking and Linux
- Lessons learned from security labs
- Small scripts and experiments

## GitHub activity

<p align="center"><img src="https://raw.githubusercontent.com/dehyasec/dehyasec/main/assets/stats-card.svg?v=5" width="560" alt="Public GitHub activity: repositories, commits and languages, generated from the GitHub API."></p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/dehyasec/dehyasec/output/github-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/dehyasec/dehyasec/output/github-snake.svg">
    <img alt="Animated contribution graph" src="https://raw.githubusercontent.com/dehyasec/dehyasec/output/github-snake-dark.svg" width="100%">
  </picture>
</p>

<sub>The activity card and the contribution animation are generated by scheduled GitHub Actions in this repository.</sub>

## Learning roadmap

- [x] GitHub profile and README
- [x] Home lab: Kali Linux in VirtualBox
- [x] Port scanner, log analyzer and file integrity monitor, each with a README
- [ ] Complete the TryHackMe Pre Security path, then Cyber Security 101
- [ ] Next project idea: password hash auditor
- [ ] Publish the first CTF writeups
- [ ] Earn an entry-level certification (Security+ or eJPT)
- [ ] Find a cybersecurity internship

## Contact

[LinkedIn](https://www.linkedin.com/in/dehya-shaikh-8610a8381/) · [TryHackMe](https://tryhackme.com/p/shaikhdehya) · [Hack The Box](https://profile.hackthebox.com/profile/01a12bed-bdea-714d-9178-494ccdd1038d) · [Email](mailto:shaikhdehya@gmail.com)

> **Ethical use.** Everything in these repositories is for education. I only test systems I own or have explicit permission to test, and I keep offensive work inside authorized labs.
