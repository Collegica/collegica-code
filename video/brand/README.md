# Brand assets

Canonical logos and marks for use across video projects — the source of truth to
update, so a rebrand or a logo fix happens in one place instead of N project folders.

- `collegica-mark.svg` — the Collegica "C" module mark (copied from
  `website/static/img/collegica-mark.svg`, which stays the actual source of truth for
  the website itself).
- `owl-planning-logo.svg` / `.png` — the OWL Planning owl mark. The SVG is the real
  source; the PNG is the original export, kept for reference.

## Using one of these in a video project

HyperFrames resolves asset paths against **each project's own root** — a composition
can't reach outside its project directory with `../` (the linter flags this as
`invalid_parent_traversal_in_asset_path`; render may tolerate it, but Studio preview
and other consumers 404). So a project that wants a logo on-screen needs its own copy:

```bash
cp ../brand/owl-planning-logo.svg my-project/assets/
```

Reference it from a composition with a root-relative path, e.g.
`<img src="assets/owl-planning-logo.svg">`.

If a mark changes here, re-copy it into every project that uses it — there's no
symlink/build step doing that automatically today.
