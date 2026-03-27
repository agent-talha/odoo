# Custom POS Branding

This addon removes default POS branding elements (logos/titles) using safe template and CSS overrides.

## Install

1. Ensure compose mounts `../custom_addons` to `/mnt/extra-addons`.
2. Redeploy Dokploy.
3. In Odoo Apps, click `Update Apps List`.
4. Search for `Custom POS Branding` and install it.
5. Hard-refresh POS browser tab (or clear service worker/cache) after installation.

## Notes

- This addon targets `point_of_sale` and `pos_restaurant`.
- Use this module for future branding edits instead of patching Odoo core files.
