#!/usr/bin/env python3
"""
Convert non-clickable product cards in the M1ND MVP into either:
- Real <a> links where a destination exists
- Properly-styled pending stubs (with 'pending' class) where they don't

Strategy: each page gets its own mapping of product-name -> destination.
Cards without destinations get class="product-card pending" so they look
non-clickable (instead of looking like dead links).
"""

import re
import os

MVP_ROOT = "/home/claude/m1nd-mvp"

# For each page, define which cards should link where.
# Cards not listed = stay as <div> but add 'pending' class.
PAGE_LINKS = {
    # The MESH index — these have real external products
    "mesh/index.html": {
        # External links (open in new tab via target attribute below)
        "PR0J.co": "https://pr0j.co",
        "MR-KT.com": "https://mr-kt.com",
        "EasyVideo.co": "https://easyvideo.co",
        "modernmotiongraphics.com": "https://modernmotiongraphics.com",
        "m1nd.co publishing infrastructure": "../index.html",
        "CHANNEL": None,  # in dev, no link
    },
    # T1NY — future products, no destinations yet
    "t1ny/index.html": {
        "Quarterly Market Scans": None,
        "Field reports": None,
        "Case studies": None,
    },
    # MEAL — future research reports, no destinations yet  
    "meal/index.html": {
        "The Toronto Importer Landscape": None,
        "The Microsystem Case Studies": None,
        "Off-Grid Food at Domestic Scale": None,
        "CFIA Compliance Landscape": None,
        "A Year of the BDRC Catalogue": None,
        "Longer-horizon candidates": None,
    },
    # MHYC — Trinity Bellwoods already links; other 7 are pending
    "mhyc/index.html": {
        "Friedrichshain": None,
        "Lower East Side": None,
        "Roma Norte": None,
        "Príncipe Real": None,
        "Shimokitazawa": None,
        "Lavapiés": None,
        "Williamsburg, Kreuzberg, Marais...": None,
    },
    # BXBX — hako already links; others need destinations
    "bxbx/index.html": {
        "Yado-S": None,
        "Kago": None,
        "Kago-V": None,
        "4×6 Greenhouse": None,
        "Palram 6×8 Greenhouse": None,
    },
    # B1KE — three variants, all pending real builds
    "b1ke/index.html": {
        "Commuter": None,
        "Cargo Trike": None,
        "Ebike Cart": None,
    },
    # COOK — Chicken Tagine has the demo cell artifact
    "stock/cook.html": {
        "Chicken Tagine": "../../cook-tagine-cell-v0.1.html",
        "Mapo Tofu": None,
        "Cacio e Pepe": None,
        "Cochinita Pibil": None,
        "Mujadara": None,
        "Bún Chả": None,
    },
    # GROW & SPORE — all cells pending production-depth pages
    "stock/grow.html": "ALL_PENDING",
    "stock/spore.html": "ALL_PENDING",
}


def process_page(filepath, link_map):
    """Process a single HTML file, converting product-card divs."""
    full_path = os.path.join(MVP_ROOT, filepath)
    with open(full_path, 'r') as f:
        content = f.read()

    original = content
    
    # Find all <div class="product-card" ...> blocks and their content
    # Pattern: <div class="product-card" [optional style]>...<div class="product-name">NAME</div>...</div>
    # We need to match the full card including all nested divs
    
    # Strategy: find each card opening, find the matching closing div,
    # extract the product-name, decide what to do
    
    pattern = re.compile(
        r'<div class="product-card"([^>]*)>\s*'  # opening tag with attrs
        r'(.*?)'  # content
        r'</div>\s*</div>',  # closing — two divs because last child is product-meta
        re.DOTALL
    )
    
    def replace_card(match):
        attrs = match.group(1)
        inner = match.group(2)
        
        # Find product name
        name_match = re.search(r'<div class="product-name">([^<]+)</div>', inner)
        if not name_match:
            return match.group(0)  # no name found, leave alone
        
        name = name_match.group(1).strip()
        
        # If link_map is "ALL_PENDING", every card is pending
        if link_map == "ALL_PENDING":
            destination = None
        else:
            destination = link_map.get(name)
        
        # Decode the inner HTML entities for matching
        name_decoded = name.replace('&amp;', '&').replace('&times;', '×')
        if link_map != "ALL_PENDING" and destination is None and name not in link_map:
            # Try decoded name match
            for key, value in link_map.items():
                if key.replace('&', '&amp;').replace('×', '&times;') == name:
                    destination = value
                    break
        
        # Reconstruct the full card content (we matched two closing divs, but the
        # actual structure is <div class="product-card">...<div class="product-meta">...</div></div>
        # so we need to re-add the inner content with both closing divs
        full_inner = inner + '</div>\n        </div>'
        # Actually simpler: keep the original card's inner structure intact
        
        if destination:
            # External URL → add target="_blank"
            if destination.startswith('http'):
                return f'<a class="product-card" href="{destination}" target="_blank" rel="noopener">\n          {inner}</div>\n        </a>'
            else:
                return f'<a class="product-card" href="{destination}">\n          {inner}</div>\n        </a>'
        else:
            # Pending — make it a non-clickable div with pending class
            return f'<div class="product-card pending">\n          {inner}</div>\n        </div>'
    
    new_content = pattern.sub(replace_card, content)
    
    if new_content != original:
        with open(full_path, 'w') as f:
            f.write(new_content)
        return True
    return False


# Process all configured pages
for page, link_map in PAGE_LINKS.items():
    full_path = os.path.join(MVP_ROOT, page)
    if not os.path.exists(full_path):
        print(f"SKIP (not found): {page}")
        continue
    
    changed = process_page(page, link_map)
    print(f"{'✓ UPDATED' if changed else '  unchanged'}: {page}")

print("\nDone.")
