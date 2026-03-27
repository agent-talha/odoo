# AGENTS.md

Development Guidelines

Always use Context7 MCP when library or API documentation, code generation, setup steps, or configuration details are needed by You/AI.
Always update this file when logic or workflow expectations change. Remove stale notes instead of stacking history.
When a feature or product surface is added, removed, or materially repurposed, update this file in the same change whenever that affects durable engineering rules, product constraints, or expected workflows.

## Branch and Deployment Context

- Active customization branch: `custom_our`
- Upstream source branch kept for sync/cherry-pick: `19.0`
- Dokploy compose path: `deploy/docker-compose.yml`
- Domain target used: `pos.deepvex.com`

## Dokploy Runtime Settings

- Container port for Odoo service: `8069`
- Required env vars:
  - `POSTGRES_PASSWORD`
  - `ODOO_DOMAIN`
- Optional env var:
  - `POSTGRES_USER` (default: `odoo`)

## Deployment Decisions Implemented

- Removed `odoo.conf` file mount requirement from compose.
- Switched from Dokploy bind mounts (`../files/...`) to Docker named volumes to avoid permission issues on `/var/lib/odoo`.
- Current named volumes in compose:
  - `odoo-db-data`
  - `odoo-web-data`
  - `odoo-extra-addons`

## POS Branding Customizations Implemented

The following user-facing Odoo branding was removed/replaced in POS and Self-Order UI:

- "Powered by Odoo" blocks (receipt + customer display)
- POS logos and branding render points were removed where possible (header, login, saver, receipt, customer display, and related report views).
- Odoo-branded page/app titles and user-facing branding strings were replaced with neutral wording where possible.
- Branded placeholders/defaults in POS self-order and connector messages were neutralized where possible.

## Recent Relevant Commits

- `20630d8a9a3` - Use named volumes for Odoo and Postgres in Dokploy
- `fa1b127afc81` - Remove Odoo branding from POS and self-order UI
- `ebff7c1b491d` - Replace remaining Odoo report title fallback

## Workflow Notes

- Make all customizations on `custom_our`.
- Keep `19.0` close to upstream and cherry-pick needed commits into `custom_our`.
- After each push, redeploy in Dokploy from `custom_our`.
