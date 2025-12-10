# Custom Domain Configuration for GitHub Pages

If you want to use a custom domain (like maticak.cz or chatbot.maticni-gymnazium.cz), follow these steps:

## Option 1: Using a subdomain (Recommended)

### Step 1: DNS Configuration
Add a CNAME record in your domain provider:
```
Type: CNAME
Name: chatbot (or maticak, or whatever you prefer)
Value: tmutina79-png.github.io
TTL: 3600
```

### Step 2: GitHub Configuration
1. Go to: https://github.com/tmutina79-png/chatbot-rag-ready/settings/pages
2. Under "Custom domain", enter: `chatbot.yourdomain.cz`
3. Wait for DNS check (green checkmark)
4. Enable "Enforce HTTPS"

## Option 2: Using apex domain (yourdomain.cz)

### Step 1: DNS Configuration
Add A records in your domain provider:
```
Type: A
Name: @ (or leave blank)
Value: 185.199.108.153
Value: 185.199.109.153
Value: 185.199.110.153
Value: 185.199.111.153
TTL: 3600
```

### Step 2: GitHub Configuration
Same as Option 1, but enter: `yourdomain.cz`

## Verification

After configuration, your chatbot will be available at:
- `https://chatbot.yourdomain.cz/` (subdomain)
- OR `https://yourdomain.cz/` (apex domain)

DNS propagation can take up to 24 hours, but usually works within 10-30 minutes.
