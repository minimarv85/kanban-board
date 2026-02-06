# Skills Research Report - 2026-02-02

## ✅ INSTALLED: gemini-deep-research
- **Repo:** github.com/lazyeo/gemini-deep-research-skill
- **Status:** VERIFIED SAFE
- **Risk:** LOW
- **Purpose:** Multi-source research via Gemini Deep Research (50-100+ websites)
- **Requires:** Gemini Advanced subscription
- **Installed:** Yes (~/.openclaw/skills/gemini-deep-research/)

---

## ⚠️ NOT FOUND ON CLAWHUB (as of 2026-02-02)
The following skills from the curated list could NOT be located:
- research-company
- research-idea
- news-aggregator
- memory-system-v2
- context-compressor

**Possible reasons:**
1. Not yet published to ClawHub
2. Different naming convention
3. Removed/deprecated
4. Private/internal skills

**Action:** If you find these skills elsewhere, share the repo link and I'll verify before installing.

---

## 📦 BUNDLED SKILLS (54 total - Pre-installed, Vetted)

### Research & Information
| Skill | Purpose | Install Required |
|-------|---------|------------------|
| **blogwatcher** | Monitor blogs/RSS feeds for updates | `go install github.com/Hyaxia/blogwatcher/cmd/blogwatcher@latest` |
| **summarize** | Summarize URLs, files, YouTube videos | `brew install steipete/tap/summarize` |
| **bird** | X/Twitter CLI (READ-ONLY) | `npm install -g @steipete/bird` |
| **github** | Interact with GitHub repos, PRs, issues | `gh` CLI |

### Memory & Context
| Skill | Purpose |
|-------|---------|
| **session-logs** | Session logging and history |
| **memory-lite** | Lightweight memory (may be available) |

### Productivity & Notes
| Skill | Purpose |
|-------|---------|
| **apple-notes** | Apple Notes integration |
| **bear-notes** | Bear notes integration |
| **notion** | Notion integration |
| **obsidian** | Obsidian integration |
| **himalaya** | CLI for notes/mail |

### Tools & Utilities
| Skill | Purpose |
|-------|---------|
| **coding-agent** | Run Codex/Claude Code/OpenCode |
| **skill-creator** | Create new skills |
| **mcporter** | MCP server management |
| **video-frames** | Extract frames from videos |
| **model-usage** | Track API usage/costs |

---

## 🔍 SKILLS AVAILABLE ON CLAWHUB (Not Yet Installed)

From the awesome-openclaw-skills list, potentially useful skills include:

**Research (Need Verification):**
- deep-research (requires Gemini Advanced)
- news-aggregator (need repo)
- arxiv-watcher (need repo)

**Search (Need Verification):**
- ddg-search (DuckDuckGo)
- exa (Exa AI)
- perplexity (paid API)
- tavily (AI-optimized search)

**Automation (Need Verification):**
- n8n-automation
- home-assistant
- proactive-research

---

## RECOMMENDED NEXT STEPS

### Tier 1: Install Now (Easy Wins)
1. **blogwatcher** - Monitor blogs/feeds for trends
2. **summarize** - Already have CLI, just need to test
3. **gh** (GitHub CLI) - Already installed, enable it

### Tier 2: If You Have Accounts
1. **gemini-deep-research** - Requires Gemini Advanced (£20/mo)
2. **exa** - Exa API for neural search (paid)

### Tier 3: Later Investigation
1. Search ClawHub specifically for "news" and "research" skills
2. Check if memory-system-v2 exists under different name
3. Explore n8n automation if you want workflow building

---

## SECURITY CHECKLIST (Before Installing Any External Skill)

For any skill from ClawHub or GitHub:

✅ Check repo owner (trusted? active?)
✅ Read SKILL.md for dangerous commands
✅ Check for shell script execution
✅ Verify no data exfiltration endpoints
✅ Check dependencies for malicious packages
✅ Look at issue tracker for security reports
✅ Test in isolated session first

---

## USEFUL BUNDLED SKILLS ALREADY ENABLED

### bird (X/Twitter)
```bash
bird home          # Home timeline
bird search "query"  # Search X
bird mentions      # Your mentions
```

### github
```bash
gh repo list       # List repos
gh pr checks       # Check PR status
gh issue list      # List issues
```

### summarize
```bash
summarize "https://url" --model google/gemini-3-flash
```

### blogwatcher
```bash
blogwatcher add "Tech News" https://techcrunch.com/rss
blogwatcher scan
```

---

## RESOURCES

- ClawHub: clawhub.com/skills
- Awesome Skills List: github.com/VoltAgent/awesome-openclaw-skills
- Official Skills: github.com/openclaw/skills
