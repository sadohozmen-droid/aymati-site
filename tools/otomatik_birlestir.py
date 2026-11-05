#!/usr/bin/env python3
"""Ajanların açtığı pull request'leri kontrol edip birleştirir.

GitHub Actions içinde çalışır (.github/workflows/ajan-otomatik-yayin.yml).
Bir PR yalnız şu koşulların hepsi sağlanırsa birleştirilir:
- Dal adı ajan önekleriyle başlar (blog/, bolge/, seo/, sosyal/, reklam/, pazarlama/)
- PR aynı depodan açılmıştır (fork değil) ve açan kişi depo sahibidir
- Değişen dosyalar yalnız site/, pazarlama/ veya tools/yazilar/, tools/takvim.json altındadır
- Değişen HTML sayfalarındaki JSON-LD blokları geçerli JSON'dur
- site/sitemap.xml değiştiyse geçerli XML'dir
- PR'da birleştirme çakışması yoktur
"""
import json, os, re, subprocess, sys, xml.dom.minidom

REPO = os.environ["GITHUB_REPOSITORY"]
OWNER = REPO.split("/")[0]
PREFIXES = ("blog/", "bolge/", "seo/", "sosyal/", "reklam/", "pazarlama/")
ALLOWED_PATHS = ("site/", "pazarlama/", "tools/yazilar/")
ALLOWED_FILES = ("tools/takvim.json",)


def gh(*args):
    return subprocess.run(["gh", *args], check=True, capture_output=True, text=True).stdout


def api(path):
    return json.loads(gh("api", path))


def file_at(ref, path):
    try:
        return subprocess.run(["gh", "api", f"repos/{REPO}/contents/{path}?ref={ref}",
                               "-H", "Accept: application/vnd.github.raw"],
                              check=True, capture_output=True, text=True).stdout
    except subprocess.CalledProcessError:
        return None


def check(pr):
    head = pr["head"]
    if not head["ref"].startswith(PREFIXES):
        return "ajan dalı değil"
    if not head.get("repo") or head["repo"]["full_name"] != REPO:
        return "fork'tan gelen PR"
    if pr["user"]["login"] != OWNER:
        return "PR'ı depo sahibi açmamış"
    if pr.get("draft"):
        return "taslak PR"
    files = []
    page = 1
    while True:
        batch = api(f"repos/{REPO}/pulls/{pr['number']}/files?per_page=100&page={page}")
        files += batch
        if len(batch) < 100:
            break
        page += 1
    for f in files:
        name = f["filename"]
        if not (name.startswith(ALLOWED_PATHS) or name in ALLOWED_FILES):
            return f"izin verilmeyen dosya: {name}"
    for f in files:
        name = f["filename"]
        if f["status"] == "removed":
            continue
        if name.endswith(".html"):
            text = file_at(head["sha"], name) or ""
            for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
                try:
                    json.loads(block)
                except ValueError as e:
                    return f"{name}: geçersiz JSON-LD ({e})"
        if name == "site/sitemap.xml":
            try:
                xml.dom.minidom.parseString(file_at(head["sha"], name) or "")
            except Exception as e:
                return f"sitemap.xml geçersiz ({e})"
        if name.endswith(".json"):
            try:
                json.loads(file_at(head["sha"], name) or "")
            except ValueError as e:
                return f"{name}: geçersiz JSON ({e})"
    full = api(f"repos/{REPO}/pulls/{pr['number']}")
    if full.get("mergeable") is False:
        return "birleştirme çakışması var"
    return None


def main():
    only = os.environ.get("PR_NUMBER")
    prs = [api(f"repos/{REPO}/pulls/{only}")] if only else api(f"repos/{REPO}/pulls?state=open&per_page=100")
    prs.sort(key=lambda p: p["number"])
    failed = False
    for pr in prs:
        if pr["state"] != "open":
            continue
        reason = check(pr)
        if reason:
            print(f"#{pr['number']} atlandı: {reason}")
            continue
        if os.environ.get("DRY_RUN"):
            print(f"#{pr['number']} birleştirilirdi (deneme): {pr['title']}")
            continue
        try:
            gh("pr", "merge", str(pr["number"]), "--repo", REPO, "--squash", "--delete-branch")
            print(f"#{pr['number']} birleştirildi: {pr['title']}")
        except subprocess.CalledProcessError as e:
            failed = True
            print(f"#{pr['number']} birleştirilemedi: {e.stderr.strip()}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
