Welcome to Web Application Security Module \o/

Brief discussion:

<pre>

    Collegue:

    Hear this, My Boss Just asked me for <code>Customer Support</code> Dashboard.

    Me:

    And ? For a Dashboard with Supports UI, Customers UI and Admin

    Portal will takes you at least 4 weeks.

    Collegue:

    I challenged him to do it within 3 days for reward <b>;)</b>

    Me:

    Are you serious <b>:O</b>?

    Collegue:

    Yeah, I got <code>Paid</code> ChatGPT 4 by my side <b>:‘D</b>

…

3 Days later.

…

    Collegue:

    I already finish it, Take a look my friend <code>http://web0x00.hbtn</code>!

    Me:

    Am I allowed to pentest it <b>:p</b> ?

    Collegue:

    Feel free, It’s <code>Hack Proof</code>. I trust AI’s Codes, <b>\o/</b>

</pre>

Through this project we will guide you through exploiting 4 types of vulnerabilities which could occur within a web app :’)

You should have:

    Pre-Installed Kali Linux (or Use a Sandbox)

    Access to our Network (Through OpenVPN or Sandbox)

    Web Browser (We Recommand FireFox)

    Terminal (For curl and sqlmap)

Warming Up:

    Get a Target Machine

    Endpoint : http://web0x00.hbtn/login

    Append to your Hosts file the domain web0x00.hbtn pointing to the target machine ip.

    <pre

┌──(yosri㉿HBTN-LAB)-[~/0x00webfundamentals]

└─$ sudo bash -c “echo ‘&lt;Target_IP&gt; web0x00.hbtn’ &gt;&gt; /etc/hosts”

</pre>

    Test your connectivity

    <pre><b>Via terminal:</b>

┌──(yosri㉿HBTN-LAB)-[~/0x00webfundamentals]

└─$ curl http://web0x00.hbtn

&lt;!doctype html&gt;

&lt;html lang=en&gt;

&lt;title&gt;Redirecting…&lt;/title&gt;

&lt;h1&gt;Redirecting…&lt;/h1&gt;

&lt;p&gt;You should be redirected automatically to the target URL: &lt;a href=“/home”&gt;/home&lt;/a&gt;. If not, click the link.

&nbsp;

<b>Via Browser:</b>

<img src=“https://hbtn-gallery.s3.eu-central-1.amazonaws.com/UPXK3FIOG45M71KI.png” style=“width:100%;” />

</pre>
