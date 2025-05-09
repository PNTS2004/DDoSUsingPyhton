# Basic DDos Script

This is a **Basic DDos Script** written in Python using the `socket` and `threading` modules. The goal is simple: simulate a flood of TCP connection requests to a specified IP address and port. Infact rather than thinking of it as a full-blown DDoS tool, think of it as a very minimal stress tester, more like a tiny proof-of-concept for understanding how connection flooding works.

 **DISCLAIMER**: This script is for **educational purposes only**. Never use it on systems you don't own or don't have permission to test. Unauthorized use could be illegal and unethical.

## What it does

You feed it:

* A **target IP address**
* A **target port**
* A **fake IP** (just for spoofing the "Host" field)

The script then spins up thousands of threads. Each thread:

1. Creates a new TCP connection to the target.
2. Sends a fake HTTP GET request.
3. Closes the connection.
4. Increments a counter that tracks how many requests have been fired.

If all goes well, every 500 connections, it prints a quick status update so you know it's still chugging along.

## How to use

It's very straightforward to run:

```bash
python ddos.py
```

Then it’ll prompt you for:

* Target IP (like `192.168.1.10`)
* Port (like `80` or `443`)
* A fake IP (just for fun, like `123.2.3.4`)

After that, it kicks off 50,000 threads (yep, that’s a lot), and each one tries to send a small TCP request to the target. The threading isn't super efficient or elegant, but it works for quick tests and learning.

### Requirements

* Python 3.x
* Internet connection (if your target is online)

### Notes

* This isn't a stealthy or resilient attack tool. Firewalls or rate-limiting will probably catch this easily.
* If your machine isn’t beefy, it might freeze or crash running 50,000 threads. Use smaller thread counts for testing!
* The "fake IP" isn't actually spoofed at the network level—it's just used in the `Host` header of the HTTP request to create confusion.
