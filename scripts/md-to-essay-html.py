#!/usr/bin/env python3
"""
Convert M1ND.studio editorial markdown into HTML publication pages.

Used for the .0001 / .0002 consulting research reports and editorial pieces.
Output: a single self-contained HTML file styled to the studio's editorial register —
EB Garamond body, Space Grotesk display, proper hierarchy, no nav clutter.

Usage:
    python3 md-to-essay-html.py INPUT.md OUTPUT.html "Publication Code" "Practice"

Example:
    python3 md-to-essay-html.py KEEP.0001.md keep/0001.html "KEEP.0001" "KEEP"
"""

import sys
import re
import html as html_lib
from pathlib import Path


# ============================================================================
# TEMPLATE
# ============================================================================

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · {practice} · M1ND.studio</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&family=IBM+Plex+Mono:wght@300;400;500&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap');

:root {{
  --paper: #F4F1E8;
  --paper-rule: #C8C2B5;
  --paper-faint: #E0DCD0;
  --paper-shade: #EAE6D9;
  --ink: #1A1814;
  --ink-soft: #4A4640;
  --ink-faint: #8A8580;
  --hanko: {accent};
  --hanko-deep: #6E5429;
  --hanko-bright: #B85540;
  --display: 'Space Grotesk', system-ui, sans-serif;
  --serif: 'Inter', Georgia, sans-serif;
  --classical: 'EB Garamond', Georgia, 'Times New Roman', serif;
  --mono: 'IBM Plex Mono', 'Courier New', monospace;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
a {{ color: inherit; text-decoration: none; }}
a:hover {{ color: var(--hanko-bright); }}
html {{ font-size: 16px; -webkit-font-smoothing: antialiased; scroll-behavior: smooth; }}
body {{ background: var(--paper); color: var(--ink); font-family: var(--classical); line-height: 1.55; }}

.studio-nav {{
  position: sticky; top: 0; z-index: 100;
  background: var(--paper); border-bottom: 1px solid var(--paper-rule);
  padding: 14px 32px; display: flex; justify-content: space-between; align-items: center;
  font-family: var(--mono); font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase;
}}
.studio-nav .nav-home {{ display: flex; align-items: center; gap: 10px; color: var(--ink); }}
.studio-nav .nav-mark {{ width: 22px; height: 22px; background: var(--ink); color: var(--paper); display: flex; align-items: center; justify-content: center; font-family: var(--display); font-size: 13px; font-weight: 500; }}
.studio-nav .nav-name {{ font-weight: 500; }}
.studio-nav .nav-name .dot {{ color: var(--hanko-bright); }}
.studio-nav .nav-links {{ display: flex; gap: 24px; }}
.studio-nav .nav-link {{ color: var(--ink-soft); }}
.studio-nav .nav-link:hover {{ color: var(--ink); }}
.studio-nav .nav-link.current {{ color: var(--hanko); }}

.breadcrumb {{
  max-width: 760px; margin: 0 auto; padding: 16px 32px 0;
  font-family: var(--mono); font-size: 10px; letter-spacing: 0.12em;
  color: var(--ink-faint); text-transform: uppercase;
}}
.breadcrumb a {{ color: var(--ink-faint); }}
.breadcrumb a:hover {{ color: var(--ink); }}
.breadcrumb .sep {{ margin: 0 8px; color: var(--paper-rule); }}
.breadcrumb .current {{ color: var(--ink); }}

article {{ max-width: 720px; margin: 0 auto; padding: 48px 32px 96px; }}

.essay-header {{
  margin-bottom: 56px;
  padding-bottom: 32px;
  border-bottom: 1px solid var(--paper-rule);
}}
.essay-eyebrow {{
  font-family: var(--mono);
  font-size: 11px;
  letter-spacing: 0.16em;
  color: var(--hanko);
  text-transform: uppercase;
  margin-bottom: 16px;
}}
.essay-title {{
  font-family: var(--display);
  font-size: 48px;
  font-weight: 400;
  line-height: 1.0;
  letter-spacing: -0.025em;
  margin-bottom: 20px;
}}
.essay-subtitle {{
  font-family: var(--classical);
  font-style: italic;
  font-size: 22px;
  line-height: 1.35;
  color: var(--ink-soft);
  margin-bottom: 28px;
  max-width: 32ch;
}}
.essay-meta {{
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.08em;
  color: var(--ink-faint);
  text-transform: uppercase;
  line-height: 1.7;
}}
.essay-meta strong {{ color: var(--ink-soft); font-weight: 500; }}

.essay-body {{
  font-family: var(--classical);
  font-size: 19px;
  line-height: 1.7;
  color: var(--ink);
}}

.essay-body h2 {{
  font-family: var(--display);
  font-size: 28px;
  font-weight: 500;
  line-height: 1.2;
  letter-spacing: -0.015em;
  margin: 56px 0 18px;
  color: var(--ink);
}}

.essay-body h3 {{
  font-family: var(--display);
  font-size: 21px;
  font-weight: 500;
  line-height: 1.25;
  margin: 40px 0 14px;
  color: var(--ink);
}}

.essay-body h4 {{
  font-family: var(--classical);
  font-style: italic;
  font-weight: 600;
  font-size: 19px;
  margin: 28px 0 10px;
  color: var(--ink);
}}

.essay-body p {{
  margin-bottom: 22px;
}}

.essay-body p strong {{ font-weight: 600; }}
.essay-body p em {{ font-style: italic; }}

.essay-body ul, .essay-body ol {{
  margin: 0 0 22px 24px;
  padding-left: 0;
}}
.essay-body li {{
  margin-bottom: 8px;
  padding-left: 4px;
}}

.essay-body hr {{
  border: none;
  border-top: 1px solid var(--paper-rule);
  margin: 48px auto;
  width: 60%;
}}

.essay-body blockquote {{
  margin: 32px 0 32px 24px;
  padding-left: 20px;
  border-left: 3px solid var(--paper-rule);
  font-style: italic;
  color: var(--ink-soft);
}}

.essay-body em.colophon {{
  display: block;
  margin-top: 56px;
  padding-top: 24px;
  border-top: 1px solid var(--paper-rule);
  font-family: var(--mono);
  font-style: normal;
  font-size: 12px;
  line-height: 1.6;
  color: var(--ink-faint);
  letter-spacing: 0.02em;
}}

footer.essay-footer {{
  max-width: 720px;
  margin: 64px auto 0;
  padding: 32px;
  border-top: 1px solid var(--paper-rule);
  font-family: var(--mono);
  font-size: 11px;
  letter-spacing: 0.1em;
  color: var(--ink-faint);
  text-transform: uppercase;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
}}
footer.essay-footer a {{ color: var(--ink-soft); }}
footer.essay-footer a:hover {{ color: var(--hanko-bright); }}

@media (max-width: 720px) {{
  .essay-title {{ font-size: 36px; }}
  .essay-subtitle {{ font-size: 19px; }}
  .essay-body {{ font-size: 17px; }}
  .essay-body h2 {{ font-size: 24px; }}
  article {{ padding: 32px 20px 64px; }}
}}
</style>
</head>
<body>

<nav class="studio-nav">
  <a href="../index.html" class="nav-home">
    <span class="nav-mark">M</span>
    <span class="nav-name">M1ND<span class="dot">.</span>studio</span>
  </a>
  <div class="nav-links">
    <a href="../index.html" class="nav-link">Catalogue</a>
    <a href="index.html" class="nav-link current">{practice}</a>
  </div>
</nav>

<nav class="breadcrumb">
  <a href="../index.html">M1ND.studio</a>
  <span class="sep">/</span>
  <a href="index.html">{practice}</a>
  <span class="sep">/</span>
  <span class="current">{title}</span>
</nav>

<article>
  <header class="essay-header">
    <div class="essay-eyebrow">{eyebrow}</div>
    <h1 class="essay-title">{title}</h1>
    {subtitle_html}
    <div class="essay-meta">
      {meta_html}
    </div>
  </header>

  <div class="essay-body">
{body_html}
  </div>
</article>

<footer class="essay-footer">
  <div>
    <a href="index.html">← {practice} practice</a>
  </div>
  <div>{title} · M1ND.studio · 2026</div>
</footer>

</body>
</html>
"""

# ============================================================================
# MARKDOWN-TO-HTML CONVERTER
# ============================================================================

def escape(s):
    return html_lib.escape(s)

def inline_format(text):
    """Convert inline markdown: **bold**, *italic*, `code`."""
    # Bold
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    # Italic (single asterisks, but not inside bold which already replaced)
    text = re.sub(r'(?<!\w)\*([^*\n]+?)\*(?!\w)', r'<em>\1</em>', text)
    # Inline code
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return text


def markdown_to_html(md):
    """
    Convert markdown to HTML for the essay template.
    Handles: # → handled as title (skipped), ## → h2, ### → h3, #### → h4,
             paragraphs, lists, bold/italic/code, horizontal rules,
             colophon (italic paragraph at end after final ---).
    """
    lines = md.split('\n')

    # Skip the title line (already in template header) — find first non-empty,
    # non-# line of substance
    output = []
    i = 0

    # Skip front matter (title + ## subtitle + bold meta lines)
    # We'll parse those separately in the caller. Skip until we hit the first ---
    found_first_hr = False
    while i < len(lines):
        if lines[i].strip() == '---':
            found_first_hr = True
            i += 1
            break
        i += 1

    if not found_first_hr:
        # No HR found, start from beginning
        i = 0

    # Now process body
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Horizontal rule
        if stripped == '---':
            output.append('<hr>')
            i += 1
            continue

        # Headers
        if stripped.startswith('#### '):
            output.append(f'<h4>{inline_format(escape(stripped[5:]))}</h4>')
            i += 1
            continue
        if stripped.startswith('### '):
            output.append(f'<h3>{inline_format(escape(stripped[4:]))}</h3>')
            i += 1
            continue
        if stripped.startswith('## '):
            output.append(f'<h2>{inline_format(escape(stripped[3:]))}</h2>')
            i += 1
            continue
        if stripped.startswith('# '):
            # Should have been consumed as title, but if it appears mid-body, treat as h2
            output.append(f'<h2>{inline_format(escape(stripped[2:]))}</h2>')
            i += 1
            continue

        # List items
        if re.match(r'^[-*]\s', stripped):
            # Collect consecutive list items
            list_items = []
            while i < len(lines) and re.match(r'^[-*]\s', lines[i].strip()):
                item = lines[i].strip()[2:]
                list_items.append(f'<li>{inline_format(escape(item))}</li>')
                i += 1
            output.append('<ul>')
            output.extend(list_items)
            output.append('</ul>')
            continue

        # Numbered list items
        if re.match(r'^\d+\.\s', stripped):
            list_items = []
            while i < len(lines) and re.match(r'^\d+\.\s', lines[i].strip()):
                item = re.sub(r'^\d+\.\s', '', lines[i].strip())
                list_items.append(f'<li>{inline_format(escape(item))}</li>')
                i += 1
            output.append('<ol>')
            output.extend(list_items)
            output.append('</ol>')
            continue

        # Paragraph: accumulate non-empty lines
        if stripped:
            para_lines = [stripped]
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith('#') and not re.match(r'^[-*]\s', lines[i].strip()) and not re.match(r'^\d+\.\s', lines[i].strip()) and lines[i].strip() != '---':
                para_lines.append(lines[i].strip())
                i += 1
            para_text = ' '.join(para_lines)
            # Check if this is the colophon (final italic paragraph after a ---)
            if para_text.startswith('*') and para_text.endswith('*') and para_text.count('*') == 2:
                # It's a single italic paragraph — likely a colophon
                inner = para_text[1:-1]
                output.append(f'<p><em class="colophon">{inline_format(escape(inner))}</em></p>')
            else:
                output.append(f'<p>{inline_format(escape(para_text))}</p>')
            continue

        # Empty line — skip
        i += 1

    return '\n'.join(output)


def extract_metadata(md):
    """
    Extract title, subtitle, and meta lines from the essay's front matter.
    Returns (title, subtitle, meta_lines_list, remaining_md).
    """
    lines = md.split('\n')
    title = ''
    subtitle = ''
    meta_lines = []

    i = 0
    # Title
    while i < len(lines) and not lines[i].strip().startswith('# '):
        i += 1
    if i < len(lines):
        title = lines[i].strip()[2:]
        i += 1

    # Skip blank lines
    while i < len(lines) and not lines[i].strip():
        i += 1

    # Subtitle (## line) — optional
    if i < len(lines) and lines[i].strip().startswith('## '):
        subtitle = lines[i].strip()[3:]
        i += 1

    # Skip blank lines
    while i < len(lines) and not lines[i].strip():
        i += 1

    # Meta lines: **Key:** Value, etc.
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line == '---':
            break
        if line.startswith('**') or line.startswith('*'):
            # It's a metadata line
            meta_lines.append(line)
            i += 1
        else:
            break

    return title, subtitle, meta_lines


def render_meta_html(meta_lines):
    """Render the front-matter meta lines into a nice HTML meta block."""
    rendered = []
    for line in meta_lines:
        # Convert **Key:** Value → <strong>Key:</strong> Value
        formatted = inline_format(escape(line))
        rendered.append(f'<div>{formatted}</div>')
    return '\n      '.join(rendered)


def convert(input_path, output_path, eyebrow, practice, accent):
    """Convert a markdown essay to HTML."""
    md = Path(input_path).read_text()

    title, subtitle, meta_lines = extract_metadata(md)
    body_html = markdown_to_html(md)
    subtitle_html = f'<p class="essay-subtitle">{inline_format(escape(subtitle))}</p>' if subtitle else ''
    meta_html = render_meta_html(meta_lines)

    html = TEMPLATE.format(
        title=escape(title),
        subtitle_html=subtitle_html,
        meta_html=meta_html,
        body_html=body_html,
        eyebrow=eyebrow,
        practice=practice,
        accent=accent,
    )

    Path(output_path).write_text(html)
    print(f"  ✓ {output_path} ({len(body_html.split())} words rendered)")


if __name__ == '__main__':
    if len(sys.argv) < 6:
        print("Usage: md-to-essay-html.py INPUT.md OUTPUT.html EYEBROW PRACTICE ACCENT_HEX")
        sys.exit(1)
    convert(*sys.argv[1:6])
