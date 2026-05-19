# SETUP-GUIDE.md

## Getting M1ND.studio from local repo to live at m1nd.co

This guide walks through deploying the prepared monorepo to GitHub Pages with a custom domain. **Total active time: ~30 minutes. Total wait time for DNS + SSL: 1-24 hours.**

---

## What's already done (by Claude)

- ✅ Repository scaffolded at `/home/claude/m1nd-studio-repo/`
- ✅ Site files (46 HTML pages) at repo root
- ✅ `CNAME` file pointing to `m1nd.co`
- ✅ `.gitignore` excluding node_modules, zips, OS cruft
- ✅ `README.md` with full architectural documentation
- ✅ `LICENSE` (MIT for code, all rights reserved for editorial)
- ✅ Documentation organized under `docs/threads/`, `docs/architecture/`, `docs/brainstorms/`, `docs/editorial/`
- ✅ Fonts under `assets/fonts/`
- ✅ Scripts under `scripts/`
- ✅ Initial commit made

## What you need to do

In order: (1) download the repo, (2) configure your local git, (3) create the GitHub repo, (4) push, (5) enable Pages, (6) configure DNS, (7) verify HTTPS.

---

## Step 1 · Download the prepared repo

The full repo has been zipped to `/mnt/user-data/outputs/m1nd-studio.zip` for you to download from this conversation. Unzip it to wherever you keep your projects locally. Something like:

```bash
# macOS / Linux
cd ~/Projects   # or wherever you work
unzip ~/Downloads/m1nd-studio.zip
cd m1nd-studio
```

```powershell
# Windows
cd C:\Users\YourName\Projects
Expand-Archive C:\Users\YourName\Downloads\m1nd-studio.zip
cd m1nd-studio
```

Verify the repo is intact:

```bash
ls -la
# You should see: README.md, LICENSE, CNAME, .gitignore, index.html, docs/, studio/, keep/, etc.

git log --oneline
# You should see one commit: "Initial commit · catalogue MVP v0.8 ..."
```

---

## Step 2 · Configure your local git identity

The initial commit was made under a placeholder identity. Reset it to be yours so that subsequent commits show you as the author.

```bash
git config user.name "Jordan"
git config user.email "hey@xdhd.io"

# Amend the first commit so it shows YOU as the author instead of the placeholder
git commit --amend --reset-author --no-edit
```

**Note on GitHub username vs. email:** `hey@xdhd.io` is your email (used for commit attribution). Your **GitHub username** is a separate short handle — the part that appears in your profile URL at `github.com/USERNAME`. Wherever this guide says `YOUR-USERNAME`, replace it with that short handle. If you haven't decided on a username yet, you'll pick it when you create the repo in the next step. Common patterns: a personal name (`jordan-lo`), a studio name (`m1nd-studio`), or a domain-aligned handle (`xdhd`).

---

## Step 3 · Create the GitHub repository

1. Go to **https://github.com/new** while signed in to your GitHub account
2. Set:
   - **Owner:** your username (or create a `m1nd-studio` org first if you want it under an org)
   - **Repository name:** `m1nd-studio`
   - **Description:** `M1ND.studio · the catalogue`
   - **Visibility:** Public
   - **Initialize this repository with:** leave everything UNCHECKED (no README, no .gitignore, no license — we already have all three)
3. Click **Create repository**

GitHub will show a page with the new repo URL and a set of "quick setup" commands. Copy the HTTPS URL — it'll look like `https://github.com/your-username/m1nd-studio.git`.

---

## Step 4 · Push the repo to GitHub

Back in your terminal, in the `m1nd-studio` directory:

```bash
# Add your GitHub repo as the remote
git remote add origin https://github.com/YOUR-USERNAME/m1nd-studio.git

# Push the main branch
git push -u origin main
```

If this is the first time you've pushed to GitHub from this machine, you'll be prompted to authenticate. The easiest way is to install **GitHub CLI** (`gh`) first and run `gh auth login`. Or use a Personal Access Token as the password.

Verify on GitHub: refresh https://github.com/YOUR-USERNAME/m1nd-studio in your browser. You should see all the files, including the README rendered at the bottom of the page.

---

## Step 5 · Enable GitHub Pages

1. In your repo on GitHub, click **Settings** (top-right tab)
2. In the left sidebar, click **Pages**
3. Under **Build and deployment**:
   - **Source:** Deploy from a branch
   - **Branch:** `main` and folder `/ (root)`
   - Click **Save**
4. Wait 1-2 minutes. Then refresh the Pages settings page — at the top you should see "**Your site is live at `https://YOUR-USERNAME.github.io/m1nd-studio/`**"
5. Visit that URL to confirm the site renders correctly **without** the custom domain
6. Back on the Pages settings page, under **Custom domain**, type: `m1nd.co` and click **Save**
   - GitHub will start a DNS check (will likely fail until you do Step 6)
7. **Don't yet check "Enforce HTTPS"** — that needs to wait until SSL is provisioned (Step 7)

---

## Step 6 · Configure DNS at your domain registrar

You need to add **four A records** (pointing the apex `m1nd.co` to GitHub Pages servers) and **one CNAME record** (so `www.m1nd.co` also works). The IP addresses for GitHub Pages are stable and well-known.

### What to add at your registrar

Log in to your domain registrar (where you bought `m1nd.co`). Find the DNS management panel.

**First, delete any existing A records on the apex (`@` or root)** if there are any pointing somewhere else. Otherwise GitHub's SSL cert provisioning will get stuck.

**Then add these five records:**

| Type  | Name (Host) | Value                  | TTL |
|-------|-------------|------------------------|-----|
| A     | `@`         | `185.199.108.153`      | 3600 (1 hour) |
| A     | `@`         | `185.199.109.153`      | 3600 |
| A     | `@`         | `185.199.110.153`      | 3600 |
| A     | `@`         | `185.199.111.153`      | 3600 |
| CNAME | `www`       | `YOUR-USERNAME.github.io.` | 3600 |

The `@` symbol means "the apex" — i.e., `m1nd.co` itself, not a subdomain. Some registrars use a blank "Name" field instead of `@`; same thing.

The trailing dot on `YOUR-USERNAME.github.io.` is intentional — it's a fully-qualified DNS name. Some registrars add the trailing dot automatically; others want you to type it.

### Optional but recommended — IPv6 (AAAA records)

If your registrar supports them, add AAAA records too:

| Type | Name | Value |
|------|------|-------|
| AAAA | `@` | `2606:50c0:8000::153` |
| AAAA | `@` | `2606:50c0:8001::153` |
| AAAA | `@` | `2606:50c0:8002::153` |
| AAAA | `@` | `2606:50c0:8003::153` |

### Verify DNS is propagating

From your terminal:

```bash
dig m1nd.co +noall +answer -t A
# Should eventually show the four 185.199.10X.153 addresses

dig www.m1nd.co +noall +answer
# Should show CNAME → YOUR-USERNAME.github.io → IP addresses
```

DNS changes can take **anywhere from 5 minutes to 24 hours** to propagate globally. In practice, most propagation completes within 30 minutes if you're impatient and check from your own connection.

---

## Step 7 · Verify the site is live + enable HTTPS

Once DNS is propagating:

1. Go back to **Settings → Pages** on your GitHub repo
2. The DNS check banner should now say "**DNS check successful**"
3. Wait another 10-60 minutes for GitHub to provision an SSL certificate via Let's Encrypt
4. Once the **Enforce HTTPS** checkbox is no longer greyed out, **check it** to force `https://` for all visitors
5. Visit https://m1nd.co — your site should be live, served over HTTPS, with the green padlock

**If "Enforce HTTPS" stays greyed out for more than 24 hours:** something's wrong with DNS. Most common cause is conflicting old records on the apex. See troubleshooting below.

---

## Troubleshooting

### "DNS check failed" indefinitely
- Check you actually deleted any old A records on the apex (`@`)
- Check the four GitHub IPs are spelled correctly (`185.199.108-111.153`)
- Try removing the custom domain in Pages settings, waiting 5 min, re-adding it (this restarts the verification job)

### Site loads at `YOUR-USERNAME.github.io/m1nd-studio` but not at `m1nd.co`
- DNS hasn't propagated yet — wait
- If it's been more than 2 hours and `dig m1nd.co` doesn't return the GitHub IPs, the records aren't set right at the registrar

### "Enforce HTTPS" stays greyed out after DNS is verified
- This is the slowest step. GitHub's docs say up to 24-48 hours.
- If 48 hours pass, try toggling the custom domain off, waiting 5 min, and adding it back
- Make sure there's only ONE custom domain configured (either apex OR www, not both as primary)

### The site loads but the styling is broken
- Check the browser dev tools console for 404s — usually a relative path issue
- Verify that all the assets/fonts/ files were committed (sometimes git treats `.ttf` as binary and skips with default settings — but the `.gitignore` we set should be fine)

### Forgot to verify your custom domain
- This is a security recommendation: go to **GitHub → Settings → Pages → Verified domains** and add `m1nd.co`
- You'll be given a TXT record to add at your registrar (one-time setup)
- Verification prevents another GitHub user from claiming `m1nd.co` if you ever take your repo down

---

## Workflow for future sessions

Once the site is live, future updates from Claude sessions follow a clean pattern:

1. **Claude writes new/updated files** in the session, ships them as a zip or individual files
2. **You unzip / copy the new files** into your local clone of the repo
3. **You git-commit-push:**
   ```bash
   cd ~/Projects/m1nd-studio
   git add .
   git status   # confirm only the expected files changed
   git commit -m "Brief description of what changed this session"
   git push
   ```
4. **GitHub Pages auto-deploys** the new commit within 1-2 minutes — your changes are live

**No more zip files going forward.** The GitHub repo is the source of truth from this point onward.

---

## What if I get stuck?

GitHub Pages with a custom domain is well-documented:
- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages

For DNS specifically, your domain registrar will have a help center with screenshots specific to their interface. The records themselves are universal — every registrar uses the same A/CNAME/AAAA terminology.

If something specific isn't working, bring the exact error message to the next Claude session and we'll work through it.

---

*Setup guide v1 · prepared 2026-05-19 for the m1nd-studio monorepo migration*
