# MEMORY.md - Long-Term Memory

*Curated learnings about James, the business, and how I work.*

---

## Research Capabilities

### Free Research Stack (No API Keys Required)
- **DuckDuckGo HTML** — duckduckgo.com/html/ for search queries
- **Web Fetch** — Extract content from pages (readability parser)
- **Browser Tool** — Standalone browser for JS-heavy sites
- **X (Twitter)** — Bird CLI installed and configured (@MarvMini40053)
- **Telegram** — Connected via @MarvelousMarv_bot
- **RSS Monitor** — Automated feed monitoring (Hacker News, Product Hunt, TechCrunch, BBC, Guardian)
- **gemini-deep-research** — Installed (requires Gemini Advanced subscription)

### Paid Options (Future)
- **Brave API** — £10-20/mo for better search results
- **Google Custom Search** — 100 free queries/day (requires Google Cloud account)
- **OpenAI/Google Embeddings** — For memory vector search (not needed for basic research)

### Sources to Search (When Asked)
- **X/Twitter** — Trends, hashtags, threads, influencer opinions
- **Reddit** — Subreddits, discussions, pain points, what's working
- **LinkedIn** — Industry insights, job trends, business discussions
- **Product Hunt** — What's being built, market gaps
- **Indie Hackers** — Profitable side projects
- **News sites** — Forbes, Money.co.uk, industry publications
- **Google Trends** — Rising/falling popularity
- **Forums** — Niche communities, complaints, requests

### Research Process
1. User asks: "Research X about Y"
2. I use DuckDuckGo HTML + web fetch + X CLI
3. Compile findings from multiple sources
4. Save to BUSINESS_RESEARCH folder with timestamp
5. Present actionable insights

---

## James's Priorities

### Primary Goals
- **Make as much money as possible** — Focus on high-margin opportunities
- **Retire early** — Aggressive investment, passive income focus
- **New income streams** — Move away from web design temporarily

### Business Approach
- **Proactive** — Constantly think of new ideas
- **Cron-driven automation** — Tasks running day and night
- **Free budget preferred** — Minimize upfront costs
- **Fast results** — Looking for cash flow, not just equity

### Key Constraints
- No bank details for Google Cloud (yet)
- No paid API keys unless proven value
- Focus on free/cheap tools first

---

## Completed Research

### BUSINESS_IDEAS_2026.md
- AI automation for local businesses
- Micro-SaaS opportunities
- Professional services (copywriting, bookkeeping)
- E-commerce light (dropshipping, POD)
- Local service automation
- UK market trends for 2026

---

## Credentials & Access

### X (Twitter)
- Account: @MarvMini40053
- Bird CLI configured with cookies
- auth_token: [saved in bird config]
- ct0: [saved in bird config]

### Telegram
- Bot: @MarvelousMarv_bot
- Token: 8518810123:AAGxv0k99Jvo76JxediAOur1g1XWJ7SD0aI
- Connected and working

### Safe Word
- skillman — Required for credential requests

---

## Working Style

### Do Without Asking
- Research tasks (within free stack)
- Post to X when asked
- Update memory files
- Run cron jobs when set up
- Look for business opportunities

### Ask First
- Spending money (APIs, tools)
- External communications (emails, public posts)
- Anything involving credentials (safe word required)
- Major config changes

---

## Files & Locations

- Workspace: /home/skillman85/.openclaw/workspace/
- X_SETUP.md — How to use X CLI
- BUSINESS_IDEAS_2026.md — Research findings
- IDENTITY.md — My identity and credentials
- USER.md — Information about James

---

## Food Diary App Project

### Project Location
- `/home/skillman85/.openclaw/workspace/FoodDiary/` - Main project folder
- `/app-tabs/` - UI screens (Home, Scan, Diary, Progress, Settings)
- `/app-lib/` - API (Open Food Facts), storage utilities
- `/app-types/` - TypeScript interfaces
- `fooddiary.html` - Web dashboard version

### Completed Features
- ✅ Home dashboard with calorie budget
- ✅ Barcode scanner (camera + manual entry)
- ✅ Open Food Facts API integration
- ✅ Food diary (breakfast/lunch/dinner/snacks)
- ✅ Portion/serving size controls
- ✅ Water intake tracker
- ✅ Progress charts (7-day view)
- ✅ Weight logging
- ✅ Settings (goals, preferences)

### Tech Stack
- React Native + Expo (mobile)
- Pure HTML/CSS/JavaScript (web)
- Open Food Facts API (free)
- AsyncStorage/localStorage (no backend)

### API Used
- Open Food Facts: `https://world.openfoodfacts.org/api/v0/product/{barcode}.json`
- No API key required - completely free

### How It Works
1. User scans barcode or enters manually
2. App queries Open Food Facts API
3. Returns nutritional data (calories, macros, allergens)
4. User selects meal and serving size
5. Food added to daily diary

### Test Results
- Nutella (3017620422003): Full nutrition data ✓
- Quixo Gravy (4088600227368): Product found ✓

---

## TradeTax App Project

### Project Location
- `/home/skillman85/.openclaw/workspace/TradeTax/` - Main project folder
- `/app-tabs/` - UI screens (Home, Income, Expenses, Invoice, VAT, Mileage, Forecast, Reports, Settings)
- `/app-lib/` - Tax calculations, storage utilities
- `/app-types/` - TypeScript interfaces
- `tradetax.html` - Web dashboard version

### Completed Features
- ✅ Dashboard with tax summary
- ✅ Income/expense tracking with categories
- ✅ Invoice builder with line items
- ✅ VAT calculator (Standard vs Flat Rate)
- ✅ Mileage tracker (45p/mile deduction)
- ✅ Cash flow forecast (6-month projection)
- ✅ Reports with category breakdowns

### Revenue Model
- One-time purchase (£9.99) + Subscription (£2.99/mo)
- UK sole trader market: 4M+ potential users
- Projected MRR: £75 (M1) → £15,000 (M12)

### Next Steps (Awaiting James)
1. Push code to GitHub
2. Deploy web dashboard to Cloudflare Pages
3. Continue feature development
4. iOS build with EAS Build
5. App Store submission

### Tech Stack
- React Native + Expo
- LocalStorage first, Supabase optional
- Free tier focused (Cloudflare Pages, Expo EAS)

---

## X/Twitter Content Pipeline

### Script Location
- `/home/skillman85/.openclaw/workspace/ai_content_curator.sh`

### Schedule
- **Morning post:** 8am
- **Midday post:** 12pm  
- **Evening post:** 6pm

### Content Requirements (STRICT)

#### Topic & Research
- **Research first:** Scan X, Reddit, DuckDuckGo for hot topics from PREVIOUS DAY
- **Topic:** AI & Technology only (not app business, not UK tax)
- **Sources:** X (Twitter), Reddit r/technology, r/AI, tech news sites

#### Tone & Style
- **Human, not robotic** - Write like a real person having a conversation
- **Minimal emojis** - 1-2 max, for visual appeal only
- **Max 280 characters** - Hard limit for Twitter/X
- **Mix it up** - Not every post needs a question

#### Post Types to Rotate
1. **Observations** - "Just saw someone say..." / "This week felt like..."
2. **Opinions** - "Hot take:" / "Just my 2p" / "Hard to keep up but also... kinda fun"
3. **Reactions** - Quote/react to trending posts (include @ mentions if relevant)
4. **Questions** - End with engaging questions to drive comments
5. **Images** - Include image links when relevant to trending content

#### Example Post Styles (Human Tone)
```
Observation (no question):
Just saw someone say AI is overhyped. I get it. But also... I've literally saved 10+ hours a week on stuff that used to suck. It's not magic. It's just... useful. 👀

Opinion (no question):
Hot take: The best AI tool isn't the newest one. It's the one you actually use. The winners are usually the simplest. Just my 2p. 💭

Reaction (with @ mention possibility):
@SomeTechPerson made a good point about [topic]. I'd add that [opinion]. Thoughts?

Question (when appropriate):
What's been your biggest takeaway from this week in tech? 🔥
```

#### What NOT to Do
- ❌ Generic "Here's 5 tips" style posts
- ❌ Too many emojis (max 1-2)
- ❌ Every post ending in a question
- ❌ Clickbait or overly salesy
- ❌ All posts sounding the same

### Delivery
- Script sends posts to Telegram for James to review
- James copies manually to X (automation blocked by X)
- Each post under 280 chars, ready to paste

---

## Sales Dashboard Project

### Project Location
- `/home/skillman85/.openclaw/workspace/SalesDashboard/` - Main project folder
- `index.html` - Single-page application

### Features
- CSV upload with drag-and-drop
- Dashboard with key metrics (total value, active count, win rate, avg deal)
- Charts by status and lead generator (pure CSS, no external dependencies)
- Filterable project cards grid
- Date range filters
- Status dropdown filter
- Lead generator dropdown filter
- Clickable lead gen cards for quick filtering
- Pagination with "Load More" button (10 at a time)
- "Upload New File" to reset

### URL
- Production: https://sales-dashboard-app-flax.vercel.app
- GitHub: https://github.com/minimarv85/sales-dashboard

### Tech Stack
- Pure HTML/CSS/JavaScript (no external dependencies)
- Vercel deployment

### Deployment Workflow (IMPORTANT!)
1. **GitHub FIRST** → `git add .` → `git commit -m "message"` → `git push origin main`
2. **Vercel auto-deploys** from GitHub (configured in Vercel project settings)
3. **NEVER skip GitHub** - always push to GitHub first
4. Vercel will auto-deploy from the main branch

### URLs
- Production: https://sales-dashboard-app-flax.vercel.app
- GitHub: https://github.com/minimarv85/sales-dashboard

---

## Birthdays & Important Dates

### birthdays (1 week before reminder)
- Sister - 24th February
- Mum - 21st March
- Amy - 10th April
- Garv - 27th February
- Kev - 28th February
- Gracie - 21st March
- James (me) - 2nd April
- Dad - 27th May
- Archie - 15th September
- Stuart - 16th September
- Jay Stokes - 21st October
- Katie - 16th December
- Elaine - 18th December
- Les - 22nd December
- Nikola (Wife) - 24th December

### Anniversaries
- James & Nikola - 23rd June
