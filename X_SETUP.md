# X (Twitter) Setup & Usage Guide

## Setup Process

### 1. Install Bird CLI
```bash
npm install -g @steipete/bird
```

### 2. Get Authentication Cookies
Bird requires cookie-based auth (not password):
- Go to x.com in Chrome (logged in)
- Press F12 → Application → Cookies → https://x.com
- Copy values for `auth_token` and `ct0`

### 3. Configure Credentials (Persistent)

**Option A: Environment Variables (Quick)**
```bash
export AUTH_TOKEN="<auth_token_value>"
export CT0="<ct0_value>"
# Add to ~/.bashrc for persistence
```

**Option B: Config File**
Create `~/.config/bird/config.json5`:
```json5
{
  authToken: "<auth_token_value>",
  ct0: "<ct0_value>"
}
```

### 4. Verify
```bash
bird whoami
```

## Usage

### Reading
```bash
bird home                    # Home timeline
bird home -n 10              # 10 tweets
bird search "query" -n 10    # Search
bird mentions                # Your mentions
bird user-tweets @handle     # User's tweets
```

### Posting
```bash
bird tweet "Your message here"
bird reply <url> "Your reply"
```

### Other
```bash
bird trending                # Trending topics
bird news -n 10              # News
bird likes                   # Your likes
bird bookmarks               # Your bookmarks
```

## Quick Reference (Env Vars Required)
For each command, export credentials first:
```bash
AUTH_TOKEN="..." CT0="..." bird <command>
```

Or add to shell profile for persistent access:
```bash
echo 'export AUTH_TOKEN="..."' >> ~/.bashrc
echo 'export CT0="..."' >> ~/.bashrc
source ~/.bashrc
```

## If Credentials Expire
1. Log into x.com in browser
2. F12 → Application → Cookies → x.com
3. Get new `auth_token` and `ct0` values
4. Update env vars or config file
