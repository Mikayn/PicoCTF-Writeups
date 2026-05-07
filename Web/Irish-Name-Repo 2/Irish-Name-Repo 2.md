# Irish-Name-Repo 2

### Challenge Description:

![{3DF4A846-BB4C-4A84-9304-A77248B81E36}.png](3DF4A846-BB4C-4A84-9304-A77248B81E36.png)

### Exploitation

Im back for round 2 (though I did Irish Name Repo 3 first but this is still my 2nd one). The website looks the same, just the login page is different.

The challenge requires logging in as admin to solve. The website lists some famous Irish people (I think Idk any of them).

![{ACB01023-BDF2-424A-8979-BAB8AD9CAA57}.png](ACB01023-BDF2-424A-8979-BAB8AD9CAA57.png)

The menu has 2 options: `support` and `admin login`. As part of recon, I viewed support first, which was a Q&A between site admin and the users. This interaction was quite hilarious and also gave a valuable insight. 

![{2A1DE182-C8A1-4F4C-BD14-3BEA0CE65340}.png](2A1DE182-C8A1-4F4C-BD14-3BEA0CE65340.png)

SQLi was going to be my first attempt if I had not found anything else, so this worked out fine. 

![{A3D6095B-4039-4E6C-BD91-336ACB113D3B}.png](A3D6095B-4039-4E6C-BD91-336ACB113D3B.png)

I tried the classic check for SQLi, even though it is already confirmed, by passing `'` and the site does throw an error. 

The next thing to do was attempt the injection via a very simple bypass that should have been flitered if the login had been strengthened. The username becomes `admin'--` . 

```html
Logged in!

Your flag is: picoCTF{REDACTED}
```

The security clearly has not been improved smh.