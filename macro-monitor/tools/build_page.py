#!/usr/bin/env python3
"""Render any Markdown file into a styled Macro Monitor page (dark hub theme).
Usage: build_page.py SRC OUT KICKER TITLE SUBTITLE BACK_HREF BACK_LABEL"""
import sys, re, markdown

SRC, OUT   = sys.argv[1], sys.argv[2]
KICKER     = sys.argv[3] if len(sys.argv) > 3 else "Reference"
TITLE      = sys.argv[4] if len(sys.argv) > 4 else "Document"
SUBTITLE   = sys.argv[5] if len(sys.argv) > 5 else ""
BACK_HREF  = sys.argv[6] if len(sys.argv) > 6 else "index.html"
BACK_LABEL = sys.argv[7] if len(sys.argv) > 7 else "← Back to Macro Monitor"

body = markdown.markdown(open(SRC, encoding="utf-8").read(),
                         extensions=["tables", "sane_lists", "fenced_code"])
body = re.sub(r'<a href="(https?://[^"]+)"',
              r'<a href="\1" target="_blank" rel="noopener noreferrer"', body)
body = body.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")

TPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Macro Monitor — __TITLE__</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root{--bg:#0a0e14;--surface:#111820;--border:#1e2a38;--text:#c8d3df;--muted:#6b7d93;--bright:#e8edf3;--blue:#4a9eff;}
  *{margin:0;padding:0;box-sizing:border-box;}
  body{background:var(--bg);color:var(--text);font-family:'IBM Plex Sans',-apple-system,system-ui,sans-serif;line-height:1.65;-webkit-font-smoothing:antialiased;min-height:100vh;padding-bottom:50px;}
  a{color:inherit;}
  .nav{background:var(--surface);border-bottom:1px solid var(--border);}
  .nav .in{max-width:900px;margin:0 auto;padding:14px 40px;display:flex;align-items:center;justify-content:space-between;}
  .nav .brand{display:flex;align-items:center;gap:11px;}
  .nav .dot{width:30px;height:30px;border-radius:7px;background:rgba(74,158,255,.12);border:1px solid var(--border);display:flex;align-items:center;justify-content:center;font-size:15px;}
  .nav .nm{font-weight:600;font-size:15px;color:var(--bright);letter-spacing:-.01em;}
  .nav .back{font-family:'IBM Plex Mono',monospace;font-size:12px;color:var(--muted);text-decoration:none;letter-spacing:.04em;}
  .nav .back:hover{color:var(--blue);}
  .page{max-width:900px;margin:0 auto;padding:46px 40px 0;}
  @media(max-width:620px){.nav .in{padding:14px 20px;}.page{padding:32px 20px 0;}}
  .kicker{font-family:'IBM Plex Mono',monospace;font-size:11px;font-weight:500;letter-spacing:2.5px;text-transform:uppercase;color:var(--muted);margin-bottom:8px;}
  .head{padding-bottom:22px;border-bottom:1px solid var(--border);margin-bottom:8px;}
  .head h1{font-size:34px;font-weight:700;color:var(--bright);letter-spacing:-.4px;}
  .head .sub{margin-top:12px;font-size:15px;color:var(--muted);max-width:62ch;}
  .content h2{font-size:21px;font-weight:600;color:var(--bright);letter-spacing:-.2px;margin:36px 0 10px;padding-bottom:10px;border-bottom:1px solid var(--border);}
  .content h2:first-of-type{margin-top:24px;}
  .content p{font-size:15px;color:var(--text);margin:0 0 14px;}
  .content a{color:var(--blue);text-decoration:none;}
  .content a:hover{text-decoration:underline;}
  .content strong{color:var(--bright);font-weight:600;}
  .content ul,.content ol{margin:0 0 14px;padding-left:22px;}
  .content li{font-size:14.5px;color:var(--text);margin:6px 0;}
  .content li::marker{color:var(--muted);}
  .content pre{background:#070b10;color:#aebfd2;border:1px solid var(--border);border-radius:9px;padding:18px 20px;overflow-x:auto;font-family:'IBM Plex Mono',monospace;font-size:12px;line-height:1.5;margin:8px 0 18px;}
  .content code{font-family:'IBM Plex Mono',monospace;font-size:12.5px;background:var(--surface);border:1px solid var(--border);padding:1px 5px;border-radius:4px;color:var(--blue);}
  .content pre code{background:none;border:none;padding:0;color:inherit;font-size:12px;}
  .tbl{overflow-x:auto;margin:8px 0 18px;border:1px solid var(--border);border-radius:8px;}
  table{width:100%;border-collapse:collapse;font-size:13px;min-width:540px;}
  thead th{background:var(--surface);color:var(--bright);text-align:left;padding:10px 12px;font-weight:600;font-family:'IBM Plex Mono',monospace;font-size:10.5px;letter-spacing:.04em;text-transform:uppercase;border-bottom:1px solid var(--border);}
  tbody td{padding:10px 12px;border-bottom:1px solid var(--border);vertical-align:top;color:var(--text);}
  tbody tr:nth-child(even){background:rgba(255,255,255,.015);}
  tbody tr:last-child td{border-bottom:none;}
  .site-footer{max-width:900px;margin:56px auto 0;padding:24px 40px 0;border-top:1px solid var(--border);}
  .site-footer .attrib{font-family:'IBM Plex Mono',monospace;font-size:12px;color:var(--muted);}
  .site-footer .attrib a{color:var(--blue);text-decoration:none;}
  .site-footer .attrib a:hover{text-decoration:underline;}
  .site-footer .gl{font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--muted);margin-top:8px;}
  @media(max-width:620px){.site-footer{padding:24px 20px 0;}}
</style>
</head>
<body>
<nav class="nav"><div class="in">
  <div class="brand"><span class="dot">📡</span><span class="nm">Macro Monitor</span></div>
  <a class="back" href="__BACK_HREF__">__BACK_LABEL__</a>
</div></nav>
<main class="page">
  <div class="head">
    <div class="kicker">__KICKER__</div>
    <h1>__TITLE__</h1>
    __SUB__
  </div>
  <div class="content">
__BODY__
  </div>
</main>
<footer class="site-footer">
  <p class="attrib">Service offered by <a href="https://atnode.ai" target="_blank" rel="noopener noreferrer">atnode.ai</a> using the awesome <a href="https://hyperagent.com" target="_blank" rel="noopener noreferrer">hyperagent platform</a>.</p>
  <p class="gl">Internal monitoring summary — not investment advice.</p>
</footer>
</body>
</html>
"""

sub_html = f'<div class="sub">{SUBTITLE}</div>' if SUBTITLE else ""
out = (TPL.replace("__TITLE__", TITLE).replace("__KICKER__", KICKER)
          .replace("__SUB__", sub_html).replace("__BACK_HREF__", BACK_HREF)
          .replace("__BACK_LABEL__", BACK_LABEL).replace("__BODY__", body))
open(OUT, "w", encoding="utf-8").write(out)
print("wrote", OUT, len(out), "bytes")
