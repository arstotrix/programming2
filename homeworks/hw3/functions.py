##locate files in folders:
def write_plain_texts(articles_data):
    for article in articles_data:
        clear_date = re_date.search(article["date"])
        day = clear_date.group(1)
        month = month_map[clear_date.group(2)]
        year = clear_date.group(3)
        path = os.path.join(".", "газета", "plain", year, month)
        escaped_name = html.escape(article["heading"]) + ".txt"
        with open(os.path.join(path, escaped_name), 'w', encoding = 'utf-8') as f:
            f.write(article["text"])


def make_dirs():
    base_path = ".\газета"
    os.mkdir(os.path.join(base_path, "plain"))
    os.mkdir(os.path.join(base_path, "mystem-xml"))
    os.mkdir(os.path.join(base_path, "mystem-plain"))
    for subfolder in ("plain", "mystem-xml", "mystem-plain"):
        for year in range(2010, 2018):
            for month in range(1, 13):
                os.mkdir(os.path.join(base_path, subfolder,
                         str(year), str(month)))