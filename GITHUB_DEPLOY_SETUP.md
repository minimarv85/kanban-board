# GitHub Actions Deployment Setup

## Required Secrets

To enable automatic deployments, you need to add these secrets to GitHub:

### 1. Get Cloudflare API Token

1. Go to: https://dash.cloudflare.com/profile/api-tokens
2. Click "Create Token"
3. Use "Edit Cloudflare Pages" template or create custom with:
   - Account: Pages Edit
   - Zone: None
4. Copy the token

### 2. Get Cloudflare Account ID

1. Go to: https://dash.cloudflare.com/
2. Look at the URL: `https://dash.cloudflare.com/<YOUR_ACCOUNT_ID>/...`
3. Copy the account ID (long alphanumeric string)

### 3. Add Secrets to GitHub

1. Go to: https://github.com/minimarv85/kanban-board/settings/secrets/actions
2. Add these secrets:

| Secret Name | Value |
|-------------|-------|
| CLOUDFLARE_API_TOKEN | (from step 1) |
| CLOUDFLARE_PAGES_TOKEN | (same as API token) |
| CLOUDFLARE_ACCOUNT_ID | (from step 2) |

## After Setup

Once secrets are added, GitHub Actions will:
1. Automatically deploy on every push to main
2. Use the stable URL: https://kanban-board-eig.pages.dev

## Manual URL (before setup)

Use: https://d1fabc75.kanban-board-eig.pages.dev/
