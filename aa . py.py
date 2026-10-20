from flask import Flask, render_template_string

app = Flask(__name__)

# الصور مدموجة داخل الملف
LOGO = "data:image/png;base64,ضع_كود_الشعار_هنا"
IMAGE1 = "data:image/png;base64,ضع_كود_الصورة_الأولى_هنا"
IMAGE2 = "data:image/png;base64,ضع_كود_الصورة_الثانية_هنا"

HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>m5r Store</title>

<!-- Vercel Speed Insights -->
<script>
  window.si = window.si || function () { (window.siq = window.siq || []).push(arguments); };
</script>
<script defer src="/_vercel/speed-insights/script.js"></script>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    color: white;
    background:
        radial-gradient(circle at top, #4b0b86, #12001f 45%, #050008);
}

header {
    text-align: center;
    padding: 30px 15px;
}

.logo {
    width: 140px;
    height: 140px;
    border-radius: 50%;
    object-fit: cover;
    box-shadow: 0 0 40px #9b25ff;
}

h1 {
    font-size: 38px;
    margin: 15px 0 5px;
}

.subtitle {
    color: #d8b8ff;
    font-size: 17px;
}

nav {
    text-align: center;
    padding: 15px;
    background: rgba(10, 0, 20, .7);
    border-top: 1px solid #63219a;
    border-bottom: 1px solid #63219a;
}

nav a {
    color: white;
    text-decoration: none;
    margin: 0 15px;
    font-weight: bold;
}

.hero {
    width: 92%;
    max-width: 1100px;
    margin: 30px auto;
    text-align: center;
}

.hero h2 {
    font-size: 32px;
    margin-bottom: 8px;
}

.hero p {
    color: #cdb4df;
}

.gallery {
    width: 92%;
    max-width: 1100px;
    margin: auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 25px;
}

.card {
    padding: 10px;
    border-radius: 22px;
    background: rgba(25, 5, 40, .8);
    border: 1px solid #8b28d1;
    box-shadow: 0 0 25px rgba(145, 35, 255, .25);
}

.card img {
    width: 100%;
    display: block;
    border-radius: 15px;
}

footer {
    margin-top: 50px;
    padding: 30px;
    text-align: center;
    color: #a993b5;
    background: rgba(10, 0, 20, .8);
}
</style>
</head>

<body>

<header>
    <img class="logo" src="{{ logo }}" alt="m5r">
    <h1>m5r Store</h1>
    <div class="subtitle">مرحباً بك في موقع m5r</div>
</header>

<nav>
    <a href="/">الرئيسية</a>
    <a href="#images">الصور</a>
    <a href="#contact">تواصل</a>
</nav>

<section class="hero">
    <h2>مرحباً بك في m5r</h2>
    <p>تصاميمنا وهويتنا البنفسجية في مكان واحد</p>
</section>

<section class="gallery" id="images">

    <div class="card">
        <img src="{{ image1 }}" alt="m5r">
    </div>

    <div class="card">
        <img src="{{ image2 }}" alt="m5r">
    </div>

</section>

<footer id="contact">
    © 2026 m5r Store
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        HTML,
        logo=LOGO,
        image1=IMAGE1,
        image2=IMAGE2
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)