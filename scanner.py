import requests

def check_sql_injection(url):
    payload = "' OR '1'='1"
    try:
        r = requests.get(url, params={"id": payload}, timeout=5)
        if "error" in r.text.lower() or "syntax" in r.text.lower():
            return {"vulnerability": "SQL Injection", "severity": "High"}
    except Exception:
        pass
    return None

def check_csrf(url):
    try:
        r = requests.get(url, timeout=5)
        if "<form" in r.text and "csrf" not in r.text.lower():
            return {"vulnerability": "CSRF (Missing Token)", "severity": "Medium"}
    except Exception:
        pass
    return None

def check_xss(url):
    payload = "<script>alert(1)</script>"
    try:
        r = requests.get(url, params={"q": payload}, timeout=5)
        if payload in r.text:
            return {"vulnerability": "Cross-Site Scripting (XSS)", "severity": "High"}
    except Exception:
        pass
    return None

def run_scanner(url):
    results = []
    for check in [check_sql_injection, check_csrf, check_xss]:
        res = check(url)
        if res:
            results.append(res)
    return results
