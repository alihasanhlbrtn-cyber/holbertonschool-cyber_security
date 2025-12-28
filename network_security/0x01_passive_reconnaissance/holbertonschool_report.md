Holberton School Domain Information Report
1. IP Ranges

The domain holbertonschool.com and its subdomains use the following IP ranges and hosting providers:

    Amazon Web Services (AWS):
        Primary infrastructure hosting.
        Range: 54.0.0.0/8 (Examples seen: 54.172.x.x, 54.237.x.x)
        Range: 34.0.0.0/8 (Examples seen: 34.227.x.x)
        Range: 3.0.0.0/8 (US-East region)

    Cloudflare:
        Used for DNS, CDN, and DDoS protection on specific subdomains.
        Range: 104.16.0.0/12
        Range: 172.64.0.0/13

    Google LLC:
        Used for mail services (MX records) and some internal tools.
        Range: 172.217.0.0/16

2. Technologies and Frameworks

Based on Shodan analysis of headers and SSL certificates, the following technologies are in use across subdomains:
Web Servers & Proxies

    Nginx: Identifying as the primary reverse proxy and web server.
    Cloudflare Server: Seen in HTTP headers for protected subdomains.
    AWS ELB (Elastic Load Balancer): Identified via standard AWS cookies and behavior.

Application Frameworks

    Ruby on Rails: Primary backend framework for the intranet and main application portals (often identified by _holberton_session cookies or specific error pages).
    React / Webpack: Frontend framework used for the modern user interfaces (e.g., intranet.holbertonschool.com).

Services & Infrastructure

    SSH (OpenSSH): Detected on various management ports (usually filtered).
    DNS: Route53 (AWS) and Cloudflare managed DNS.
    Email: Google Workspace (formerly G Suite).

3. Subdomains Detected

Key subdomains identified during reconnaissance:

    www.holbertonschool.com
    intranet.holbertonschool.com
    apply.holbertonschool.com
    api.holbertonschool.com
