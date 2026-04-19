# Reliquery — Marketing Site

The public-facing website for Reliquery, the brand intelligence Chrome extension.

## Stack

- **Astro 4** — static site generator
- **Tailwind CSS** — styling
- **Cloudflare Pages** — hosting (free tier, deploys from GitHub on push)

## Pages

- `/` — landing page (hero, three modes, Brand Reliquary explainer, pricing, CTA)
- `/privacy` — privacy policy (required by Chrome Web Store)
- `/terms` — terms of service (lawyer-review recommended before production)

## Local development

```bash
npm install
npm run dev
```

Then open http://localhost:4321

## Build

```bash
npm run build
```

Output goes to `dist/`. Cloudflare Pages auto-detects this.

## Deploy to Cloudflare Pages

1. Push this repo to GitHub
2. Cloudflare Dashboard → Workers & Pages → Create → Connect to Git
3. Select the repo
4. Framework preset: **Astro**
5. Build command: `npm run build`
6. Build output directory: `dist`
7. Save and Deploy

You'll get a free URL like `reliquery-www.pages.dev` immediately.

## Connect custom domain

Once your domain (`reliquery.app`) is on Cloudflare nameservers and shows "Active" in the Cloudflare DNS dashboard:

1. Workers & Pages → your project → Custom domains → "Set up a custom domain"
2. Enter `reliquery.app`
3. Cloudflare auto-creates DNS records and provisions SSL (~5 minutes)
4. Optionally repeat for `www.reliquery.app`

## Editing content

- **Landing page copy:** `src/pages/index.astro`
- **Privacy policy:** `src/pages/privacy.astro`
- **Terms:** `src/pages/terms.astro`
- **Header / footer / metadata:** `src/layouts/Base.astro`
- **Brand colors:** `tailwind.config.mjs`

## TODO before launch

- [ ] Replace `#` placeholder in "Add to Chrome" buttons with the real Chrome Web Store URL once published
- [ ] Have a lawyer review the Terms of Service for your jurisdiction
- [ ] Set up the `support@reliquery.app` email address
- [ ] Add screenshots of the extension in action (consider an `/screenshots` section)
- [ ] Create OpenGraph image (1200×630) at `public/og.png` and reference it in Base.astro
