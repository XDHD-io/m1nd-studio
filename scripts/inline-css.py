#!/usr/bin/env python3
"""
Inline the shared CSS into every HTML file in the MVP so that:
1. Files work when opened locally via file:// without ANY external loading
2. No path resolution issues
3. Add a global anchor reset so no link ever shows up as default blue
"""

import os
import re

MVP_ROOT = "/home/claude/m1nd-mvp"

# Read the shared CSS
with open(os.path.join(MVP_ROOT, 'shared/studio.css'), 'r') as f:
    shared_css = f.read()

# Add a global anchor reset at the start (after :root) to prevent default-blue links
# The current CSS has * { box-sizing... } reset but no anchor color reset
anchor_reset = """
/* Global anchor reset — prevents default browser-blue links anywhere */
a {
  color: inherit;
  text-decoration: none;
}
a:hover {
  color: var(--hanko);
}
"""

# Inject the anchor reset right after the * { ... } block
shared_css = shared_css.replace(
    "* { box-sizing: border-box; margin: 0; padding: 0; }",
    "* { box-sizing: border-box; margin: 0; padding: 0; }\n" + anchor_reset
)

# Find every HTML file
html_files = []
for root, _, files in os.walk(MVP_ROOT):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

print(f"Found {len(html_files)} HTML files to update.\n")

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    
    # Find the link tag — there can be different relative paths
    # Patterns to match: href="shared/studio.css", href="../shared/studio.css"
    css_link_pattern = re.compile(r'<link rel="stylesheet" href="[^"]*shared/studio\.css">')
    
    if css_link_pattern.search(content):
        # Replace with inlined <style>
        replacement = f'<style>\n{shared_css}\n</style>'
        content = css_link_pattern.sub(replacement, content)
        
        with open(filepath, 'w') as f:
            f.write(content)
        
        rel_path = os.path.relpath(filepath, MVP_ROOT)
        size_kb = len(content) / 1024
        print(f"  ✓ {rel_path} ({size_kb:.1f}KB)")
    else:
        rel_path = os.path.relpath(filepath, MVP_ROOT)
        print(f"  - {rel_path} (no CSS link found — skipping)")

print("\nDone.")
