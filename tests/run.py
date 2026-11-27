# usage: python3 run.py questions.json out.json sonnet,opus,haiku 1
import json, subprocess, sys, pathlib, tempfile, concurrent.futures as cf
base = pathlib.Path(__file__).resolve().parent
F = base.parent
INSTR = "You are the onboarder described in identity.md. Follow rules.md in every reply. Answer only from the files in reference/."
files = ["identity.md","rules.md","examples.md"] + sorted(f"reference/{p.name}" for p in (F/"reference").glob("*.md"))
SYS = INSTR + "\n\nProject knowledge:\n" + "".join(f'\n<document name="{n}">\n{(F/n).read_text()}</document>\n' for n in files)
cwd = tempfile.mkdtemp()
def turn(model, text, sid=None):
    cmd=["claude","-p","--model",model,"--tools","","--strict-mcp-config","--disable-slash-commands","--setting-sources","","--system-prompt",SYS,"--output-format","json"]
    if sid: cmd += ["--resume",sid]
    r=subprocess.run(cmd,input=text,capture_output=True,text=True,cwd=cwd,timeout=300)
    d=json.loads(r.stdout); return d["result"], d["session_id"], d
def session(job):
    cid, model, i, turns = job
    sid=None; log=[]; meta=None
    try:
        for t in turns:
            a,sid,d=turn(model,t,sid); log.append((t,a)); meta=meta or list(d.get("modelUsage",{}))
    except Exception as e: log.append(("ERROR",repr(e)))
    return {"case":cid,"model":model,"run":i,"models_used":meta,"turns":log}
if __name__=="__main__":
    cases=json.loads((base/sys.argv[1]).read_text()); models=sys.argv[3].split(","); n=int(sys.argv[4])
    jobs=[(c,m,i,t) for c,t in cases.items() for m in models for i in range(n)]
    with cf.ThreadPoolExecutor(6) as ex: out=list(ex.map(session,jobs))
    (base/sys.argv[2]).write_text(json.dumps(out,indent=1,ensure_ascii=False))
    for o in out:
        print(f"\n=== {o['case']} [{o['model']} #{o['run']}]")
        for q,a in o["turns"]: print(f"> {q}\n{a}")
