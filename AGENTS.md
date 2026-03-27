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
- Odoo logo component usage on customer display
- Odoo-branded page/app titles
- Odoo fallback logo image in navbar/customer display CSS
- Odoo-branded server error labels in POS popups
- POS header/login/saver/report/receipt/customer-display logo render points removed

### Main files updated for branding

- `addons/point_of_sale/views/pos_assets_index.xml`
- `addons/point_of_sale/static/src/app/main.js`
- `addons/point_of_sale/static/src/app/screens/receipt_screen/receipt/order_receipt.xml`
- `addons/point_of_sale/static/src/customer_display/customer_display.xml`
- `addons/point_of_sale/static/src/customer_display/customer_display.js`
- `addons/point_of_sale/static/src/app/utils/error_handlers.js`
- `addons/point_of_sale/static/src/app/components/popups/cash_move_popup/cash_move_list_popup/cash_move_list_popup.js`
- `addons/point_of_sale/static/src/app/components/navbar/navbar.scss`
- `addons/point_of_sale/static/src/css/customer_facing_display.css`
- `addons/pos_self_order/views/pos_self_order.index.xml`
- `addons/point_of_sale/static/src/app/components/navbar/navbar.xml`
- `addons/point_of_sale/static/src/app/screens/saver_screen/saver_screen.xml`
- `addons/point_of_sale/static/src/app/screens/login_screen/login_screen.xml`
- `addons/point_of_sale/static/src/app/screens/receipt_screen/receipt/receipt_header/receipt_header.xml`
- `addons/point_of_sale/static/src/app/components/navbar/sale_details_button/sales_detail_report.xml`
- `addons/point_of_sale/static/src/backend/lna_checklist/lna_checklist.xml`
- `addons/point_of_sale/static/src/customer_display/customer_display_data_service.js`
- `addons/point_of_sale/data/scenarios/clothes_data.xml`
- `addons/pos_self_order/views/custom_link_views.xml`
- `addons/pos_adyen/static/src/app/utils/payment/payment_adyen.js`
- `addons/pos_razorpay/static/src/app/utls/payment/payment_razorpay.js`
- `addons/pos_viva_com/static/src/app/payment_viva_com.js`
- `addons/pos_glory_cash/static/src/utils/glory_xml.js`

## Recent Relevant Commits

- `20630d8a9a3` - Use named volumes for Odoo and Postgres in Dokploy
- `fa1b127afc81` - Remove Odoo branding from POS and self-order UI
- `ebff7c1b491d` - Replace remaining Odoo report title fallback

## Workflow Notes

- Make all customizations on `custom_our`.
- Keep `19.0` close to upstream and cherry-pick needed commits into `custom_our`.
- After each push, redeploy in Dokploy from `custom_our`.
