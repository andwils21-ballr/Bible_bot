#!/usr/bin/env python3
"""Build the navigable reading site into docs/ (GitHub Pages serves it free).

Left rail = books, click a book = its chapters, click a chapter = read it.
Output is a shell page plus one JSON file per book, so the rail never reloads.
Stdlib only. Run from the repo root:  python3 build_site.py
"""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
BOOKS_DIR = os.path.join(ROOT, "books")
DOCS = os.path.join(ROOT, "docs")


def parse_chapter(path):
    """Split a chapter file into its frontmatter dict and body text."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    meta = {}
    if text.startswith("---"):
        _, fm, body = text.split("---", 2)
        for line in fm.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    else:
        body = text
    return meta, body.strip()


VERSE_RE = re.compile(r"^\*\*(\d+)\*\*\s+(.*)$", re.S)


def inline(s):
    """Escape, then re-apply the only inline markup the spec allows."""
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", s)
    return s.replace("  \n", "<br>\n")


def to_html(body):
    """Render the narrow Markdown subset the spec permits."""
    out, in_notes = [], False
    for block in re.split(r"\n\s*\n", body):
        block = block.strip()
        if not block or block == "---":
            continue
        if block.startswith("# "):
            out.append(f"<h1>{inline(block[2:])}</h1>")
        elif block.startswith("## "):
            heading = block[3:].strip()
            in_notes = heading.lower() == "notes"
            cls = ' class="notes-head"' if in_notes else ""
            out.append(f"<h2{cls}>{inline(heading)}</h2>")
        elif block.startswith("- "):
            items = "".join(
                f"<li>{inline(ln[2:].strip())}</li>"
                for ln in block.splitlines()
                if ln.strip().startswith("- ")
            )
            out.append(f'<ul class="{"notes" if in_notes else ""}">{items}</ul>')
        else:
            m = VERSE_RE.match(block)
            if m:
                n, rest = m.group(1), m.group(2)
                out.append(
                    f'<p class="v" id="v{n}">'
                    f'<a class="vn" href="#v{n}">{n}</a>{inline(rest)}</p>'
                )
            else:
                out.append(f"<p>{inline(block)}</p>")
    return "\n".join(out)


def to_speech(body):
    """Plain text for the read-aloud player: the rendering only.

    Stops at the Notes heading — the notes are written to be read, not heard,
    and are full of transliterated Hebrew that is meaningless spoken aloud.
    Returns a list of chunks, one per verse or heading, so the player can speak
    them one at a time and highlight as it goes."""
    chunks = []
    for block in re.split(r"\n\s*\n", body):
        block = block.strip()
        if not block or block == "---":
            continue
        if block.startswith("## "):
            if block[3:].strip().lower() == "notes":
                break                      # everything after this is notes
            chunks.append({"id": "", "text": block[3:].strip()})
        elif block.startswith("# "):
            chunks.append({"id": "", "text": block[2:].strip()})
        elif block.startswith("- "):
            continue
        else:
            m = VERSE_RE.match(block)
            if not m:
                continue
            text = m.group(2).replace("  \n", " ")
            text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
            text = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"\1", text)
            chunks.append({"id": "v" + m.group(1), "text": text})
    return chunks


def main():
    manifest = json.load(open(os.path.join(ROOT, "manifest.json"), encoding="utf-8"))
    os.makedirs(os.path.join(DOCS, "data"), exist_ok=True)

    rail = []
    for book in manifest["books"]:
        folder = os.path.join(BOOKS_DIR, f"{book['order']}-{book['slug']}")
        chapters = []
        if os.path.isdir(folder):
            for name in sorted(os.listdir(folder)):
                if not name.endswith(".md"):
                    continue
                meta, body = parse_chapter(os.path.join(folder, name))
                chapters.append({
                    "n": int(meta.get("chapter", 0)),
                    "title": meta.get("title", ""),
                    "status": meta.get("status", "rendered"),
                    "html": to_html(body),
                    "speech": to_speech(body),
                })
            chapters.sort(key=lambda c: c["n"])
        with open(os.path.join(DOCS, "data", f"{book['slug']}.json"), "w",
                  encoding="utf-8") as f:
            json.dump({"book": book, "chapters": chapters}, f, ensure_ascii=False)
        rail.append({**book, "done": len([c for c in chapters
                                          if c["status"] == "rendered"])})

    with open(os.path.join(DOCS, "data", "manifest.json"), "w",
              encoding="utf-8") as f:
        json.dump({"books": rail}, f, ensure_ascii=False, indent=1)

    with open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8") as f:
        f.write(SHELL)

    done = sum(b["done"] for b in rail)
    total = sum(b["chapters"] for b in rail)
    print(f"docs/ built — {done}/{total} chapters rendered "
          f"({done / total * 100:.1f}%)" if total else "docs/ built")


SHELL = r"""<!doctype html>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="icon" href="data:,">
<title>The Ethiopian Canon — A Close Rendering</title>
<style>
  :root{
    --bg:#fbfaf7; --ink:#20211f; --muted:#6c6a63; --rule:#e2ded4;
    --accent:#7a5c2e; --panel:#f4f1ea;
  }
  @media (prefers-color-scheme:dark){
    :root{ --bg:#16171a; --ink:#e8e5dd; --muted:#9a968c; --rule:#2e3035;
           --accent:#c8a86a; --panel:#1d1f23; }
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--ink);
       font:16px/1.65 Georgia,'Iowan Old Style',serif}
  #wrap{display:flex;min-height:100vh}
  nav{width:270px;flex:none;border-right:1px solid var(--rule);
      background:var(--panel);overflow-y:auto;height:100vh;position:sticky;top:0}
  nav h1{font-size:14px;letter-spacing:.09em;text-transform:uppercase;
         color:var(--muted);margin:0;padding:20px 18px 12px;font-weight:600}
  nav a{display:block;padding:6px 18px;color:var(--ink);text-decoration:none;
        font-size:14.5px;border-left:3px solid transparent}
  nav a:hover{background:rgba(122,92,46,.09)}
  nav a.on{border-left-color:var(--accent);color:var(--accent);font-weight:700}
  nav a .ct{float:right;color:var(--muted);font-size:12px;font-weight:400}
  nav a.pending{color:var(--muted)}
  main{flex:1;min-width:0;padding:44px 6vw 120px;max-width:820px}
  .chips{display:flex;flex-wrap:wrap;gap:7px;margin:0 0 30px}
  .chips a{display:block;min-width:40px;text-align:center;padding:7px 10px;
           border:1px solid var(--rule);border-radius:4px;text-decoration:none;
           color:var(--ink);font-size:14px}
  .chips a:hover{border-color:var(--accent);color:var(--accent)}
  .chips a.on{background:var(--accent);border-color:var(--accent);color:var(--bg)}
  h1{font-size:30px;font-weight:600;margin:0 0 6px;letter-spacing:-.01em}
  h2{font-size:17px;font-weight:600;color:var(--accent);margin:34px 0 14px;
     letter-spacing:.01em}
  h2.notes-head{border-top:1px solid var(--rule);padding-top:26px;margin-top:48px}
  p.v{margin:0 0 13px;text-indent:0}
  a.vn{color:var(--muted);font:600 11px/1 ui-sans-serif,system-ui,sans-serif;
       vertical-align:super;margin-right:6px;text-decoration:none}
  a.vn:hover{color:var(--accent)}
  ul.notes{font-size:14.5px;color:var(--muted);padding-left:20px}
  ul.notes li{margin:0 0 11px}
  ul.notes strong{color:var(--ink)}
  .lede{color:var(--muted);margin:0 0 34px;font-size:15px}
  .stub{border:1px dashed var(--rule);padding:22px;color:var(--muted);
        border-radius:5px}
  p.v.speaking{background:rgba(122,92,46,.14);border-radius:3px;
               box-shadow:0 0 0 4px rgba(122,92,46,.14)}
  #player{position:fixed;left:0;right:0;bottom:0;z-index:20;display:none;
          gap:12px;align-items:center;padding:10px 14px;
          background:var(--panel);border-top:1px solid var(--rule);
          font:14px/1 ui-sans-serif,system-ui,sans-serif}
  #player.on{display:flex}
  #player button{font:inherit;cursor:pointer;border:1px solid var(--rule);
                 background:var(--bg);color:var(--ink);border-radius:6px;
                 padding:11px 16px;min-width:88px}
  #player button.primary{background:var(--accent);border-color:var(--accent);
                         color:var(--bg);font-weight:700}
  #player label{color:var(--muted);display:flex;align-items:center;gap:6px}
  #player select{font:inherit;padding:8px;border-radius:6px;
                 border:1px solid var(--rule);background:var(--bg);color:var(--ink)}
  #ptxt{flex:1;color:var(--muted);overflow:hidden;text-overflow:ellipsis;
        white-space:nowrap}
  main{padding-bottom:96px}
  @media(max-width:760px){
    #player{flex-wrap:wrap;gap:8px;padding:8px 10px}
    #player button{flex:1 1 auto;min-width:0;padding:13px 10px}
    #player label{font-size:13px}
    #ptxt{display:none}
    nav{max-height:30vh}
    main{padding-bottom:120px}
    #wrap{display:block}
    nav{width:auto;height:auto;position:static;border-right:0;
        border-bottom:1px solid var(--rule);max-height:42vh}
    main{padding:28px 20px 80px}
  }
</style>
<div id="wrap"><nav id="rail"></nav><main id="view"></main></div>
<div id="player">
  <button id="pplay" class="primary">Read aloud</button>
  <button id="pstop">Stop</button>
  <label>Speed
    <select id="prate">
      <option value="0.8">0.8</option><option value="0.9">0.9</option>
      <option value="1" selected>1.0</option><option value="1.1">1.1</option>
      <option value="1.25">1.25</option><option value="1.5">1.5</option>
    </select>
  </label>
  <label><input type="checkbox" id="pnext" checked> Keep going</label>
  <span id="ptxt"></span>
</div>
<script>
let BOOKS=[], cache={};
const rail=document.getElementById('rail'), view=document.getElementById('view');

function drawRail(slug){
  rail.innerHTML='<h1>The Ethiopian Canon</h1>'+BOOKS.map(b=>
    `<a href="#/${b.slug}" class="${b.slug===slug?'on':''}${b.done?'':' pending'}">`+
    `${b.order}. ${b.title}<span class="ct">${b.done||'—'}</span></a>`).join('');
}
async function load(slug){
  if(!cache[slug]) cache[slug]=await (await fetch(`data/${slug}.json`)).json();
  return cache[slug];
}
function chips(d,cur){
  if(!d.chapters.length) return '';
  return '<div class="chips">'+d.chapters.map(c=>
    `<a href="#/${d.book.slug}/${c.n}" class="${c.n==cur?'on':''}">`+
    `${c.status==='need_source'?'—':c.n}</a>`).join('')+'</div>';
}
async function route(){
  const [,slug,ch]=(location.hash||'').replace(/^#/,'').split('/');
  drawRail(slug);
  if(!ch){ stop(); bar.classList.remove('on'); }
  if(!slug){
    const done=BOOKS.reduce((a,b)=>a+b.done,0),
          all=BOOKS.reduce((a,b)=>a+b.chapters,0);
    view.innerHTML='<h1>A Close Rendering</h1><p class="lede">'+
      'The Ethiopian Orthodox Tewahedo canon, rendered chapter by chapter with '+
      'attention to what English normally loses. Choose a book at left.</p>'+
      `<p class="lede">${done} of ${all} chapters rendered.</p>`;
    return;
  }
  const d=await load(slug);
  if(!ch){
    view.innerHTML=`<h1>${d.book.title}</h1><p class="lede">`+
      (d.chapters.length?`${d.chapters.length} of ${d.book.chapters} chapters`
                        :'Not yet begun.')+'</p>'+chips(d);
    return;
  }
  const c=d.chapters.find(x=>x.n==ch);
  view.innerHTML=chips(d,ch)+(c?c.html:'<p class="stub">Not yet rendered.</p>');
  window.scrollTo(0,0);
  const wasPlaying=P.on;
  stop(); P.q=(c&&c.speech)||[]; P.i=0;
  bar.classList.toggle('on',P.q.length>0);
  keep('last',location.hash);
  if(innerWidth<=760) view.scrollIntoView({block:'start'});  // skip past the rail
  if(wasPlaying && P.q.length) setTimeout(play,350);   // chapter auto-advance
}

/* ---- read aloud -------------------------------------------------------- */
const P={q:[],i:0,on:false,lock:null,tick:null};
const el=id=>document.getElementById(id);
const bar=el('player'), bPlay=el('pplay'), bStop=el('pstop'),
      selRate=el('prate'), cbNext=el('pnext'), out=el('ptxt');

function say(t){ try{return localStorage.getItem(t)}catch(e){return null} }
function keep(t,v){ try{localStorage.setItem(t,v)}catch(e){} }

async function wake(want){
  try{
    if(want && 'wakeLock' in navigator && !P.lock)
      P.lock=await navigator.wakeLock.request('screen');
    if(!want && P.lock){ P.lock.release(); P.lock=null; }
  }catch(e){}
}

function stop(){
  P.on=false; speechSynthesis.cancel(); clearInterval(P.tick); P.tick=null;
  document.querySelectorAll('p.v.speaking').forEach(n=>n.classList.remove('speaking'));
  bPlay.textContent='Read aloud'; out.textContent=''; wake(false);
}

function speakAt(n){
  if(!P.on) return;
  if(n>=P.q.length){                       // chapter finished
    const [,slug,ch]=(location.hash||'').replace(/^#/,'').split('/');
    if(cbNext.checked && slug && ch){
      location.hash=`#/${slug}/${Number(ch)+1}`;   // route() restarts playback
    } else stop();
    return;
  }
  P.i=n; const chunk=P.q[n];
  document.querySelectorAll('p.v.speaking').forEach(x=>x.classList.remove('speaking'));
  if(chunk.id){
    const node=document.getElementById(chunk.id);
    if(node){ node.classList.add('speaking');
      node.scrollIntoView({block:'center',behavior:'smooth'}); }
  }
  out.textContent=chunk.text.slice(0,90);
  const u=new SpeechSynthesisUtterance(chunk.text);
  u.rate=parseFloat(selRate.value); u.onend=()=>speakAt(n+1);
  u.onerror=()=>speakAt(n+1);
  speechSynthesis.speak(u);
}

function play(){
  if(!P.q.length) return;
  P.on=true; bPlay.textContent='Pause'; wake(true);
  // some browsers suspend long speech; nudging it keeps it alive
  clearInterval(P.tick);
  P.tick=setInterval(()=>{ if(P.on && speechSynthesis.speaking && !speechSynthesis.paused)
                             { speechSynthesis.pause(); speechSynthesis.resume(); } },9000);
  speakAt(P.i);
}

bPlay.onclick=()=>{ if(P.on){ P.on=false; speechSynthesis.cancel();
                              clearInterval(P.tick); bPlay.textContent='Resume';
                              wake(false); } else play(); };
bStop.onclick=()=>{ P.i=0; stop(); };
selRate.onchange=()=>{ keep('rate',selRate.value);
                       if(P.on){ speechSynthesis.cancel(); speakAt(P.i); } };
cbNext.onchange=()=>keep('next',cbNext.checked?'1':'0');
if(say('rate')) selRate.value=say('rate');
if(say('next')==='0') cbNext.checked=false;

addEventListener('hashchange',route);
(async()=>{
  BOOKS=(await (await fetch('data/manifest.json')).json()).books;
  route();
})();
</script>
"""

if __name__ == "__main__":
    main()
