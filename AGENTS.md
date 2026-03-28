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
- Odoo service now builds from `deploy/Dockerfile` using official `odoo:19.0` as the base image.

## Workflow Notes

- Make all customizations on `custom_our`.
- Keep `19.0` close to upstream and cherry-pick needed commits into `custom_our`.
- After each push, redeploy in Dokploy from `custom_our`.
- If deployment changes are not visible after redeploy, force rebuild in Dokploy to refresh image layers.
