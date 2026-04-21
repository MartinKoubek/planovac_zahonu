from flask import Flask, render_template, request

app = Flask(__name__)

VEGETABLES = {
    "bazalka": {
        "label": "Bazalka",
        "compatible": ["rajce", "paprika", "salat"],
        "incompatible": ["ruta"],
    },
    "rajce": {
        "label": "Rajče",
        "compatible": ["bazalka", "cibule", "cesnek", "mrkev", "salat"],
        "incompatible": ["brambory", "fenykl", "kukurice"],
    },
    "paprika": {
        "label": "Paprika",
        "compatible": ["bazalka", "cibule", "cesnek", "mrkev", "salat"],
        "incompatible": ["fenykl", "brambory"],
    },
    "mrkev": {
        "label": "Mrkev",
        "compatible": ["cibule", "cesnek", "hrasek", "porek", "salat"],
        "incompatible": ["kopr"],
    },
    "cibule": {
        "label": "Cibule",
        "compatible": ["mrkev", "cervena_repa", "salat", "rajce", "jahody"],
        "incompatible": ["fazole", "hrasek"],
    },
    "kopr": {
        "label": "Kopr",
        "compatible": ["okurka", "zeli", "rajce"],
        "incompatible": ["mrkev"],
    },
    "cesnek": {
        "label": "Česnek",
        "compatible": ["mrkev", "okurka", "rajce", "jahody", "cervena_repa"],
        "incompatible": ["fazole", "hrasek", "zeli"],
    },
    "porek": {
        "label": "Pórek",
        "compatible": ["mrkev", "celer", "jahody", "salat"],
        "incompatible": ["fazole", "hrasek"],
    },
    "salat": {
        "label": "Salát",
        "compatible": ["mrkev", "okurka", "redkvicka", "rajce", "jahody"],
        "incompatible": ["petrzel"],
    },
    "hlavkovy_salat": {
        "label": "Hlávkový salát",
        "compatible": ["mrkev", "okurka", "redkvicka", "rajce", "jahody"],
        "incompatible": ["petrzel"],
    },
    "spenat": {
        "label": "Špenát",
        "compatible": ["mrkev", "redkvicka", "zeli", "jahody"],
        "incompatible": [],
    },
    "okurka": {
        "label": "Okurka",
        "compatible": ["fazole", "hrasek", "kopr", "salat", "cesnek"],
        "incompatible": ["brambory", "rajce", "redkvicka"],
    },
    "cuketa": {
        "label": "Cuketa",
        "compatible": ["fazole", "cibule", "kukurice"],
        "incompatible": ["brambory"],
    },
    "dyne": {
        "label": "Dýně",
        "compatible": ["fazole", "kukurice", "redkvicka"],
        "incompatible": ["brambory"],
    },
    "fazole": {
        "label": "Fazole",
        "compatible": ["okurka", "kukurice", "redkvicka", "zeli"],
        "incompatible": ["cibule", "cesnek", "porek"],
    },
    "hrasek": {
        "label": "Hrášek",
        "compatible": ["mrkev", "redkvicka", "okurka", "kukurice"],
        "incompatible": ["cibule", "cesnek", "porek"],
    },
    "zeli": {
        "label": "Zelí",
        "compatible": ["celer", "fazole", "kopr", "cibule"],
        "incompatible": ["cesnek", "rajce", "jahody"],
    },
    "kedluben": {
        "label": "Kedluben",
        "compatible": ["celer", "spenat", "redkvicka", "cibule"],
        "incompatible": ["rajce"],
    },
    "brambory": {
        "label": "Brambory",
        "compatible": ["fazole", "kren", "kukurice", "zeli"],
        "incompatible": ["okurka", "rajce", "dyne"],
    },
    "redkvicka": {
        "label": "Ředkvička",
        "compatible": ["mrkev", "okurka", "salat", "hrasek"],
        "incompatible": ["yzop"],
    },
    "petrzel": {
        "label": "Petržel",
        "compatible": ["rajce", "porek", "redkvicka"],
        "incompatible": ["salat"],
    },
    "celer": {
        "label": "Celer",
        "compatible": ["zeli", "porek", "fazole", "kedluben"],
        "incompatible": ["kukurice"],
    },
    "cervena_repa": {
        "label": "Červená řepa",
        "compatible": ["cibule", "cesnek", "salat", "okurka"],
        "incompatible": ["popinavy_fazole"],
    },
    "jahody": {
        "label": "Jahody",
        "compatible": ["cesnek", "cibule", "porek"],
        "incompatible": ["zeli"],
    },
    "kukurice": {
        "label": "Kukuřice",
        "compatible": ["fazole", "hrasek", "cuketa", "dyne"],
        "incompatible": ["rajce", "celer"],
    },
}

LABELS = {key: value["label"] for key, value in VEGETABLES.items()}


def labels_for(keys: list[str]) -> list[str]:
    return [LABELS.get(key, key.replace("_", " ").title()) for key in keys]


@app.route("/", methods=["GET", "POST"])
def index():
    selected_key = request.form.get("vegetable", "")
    selected_item = VEGETABLES.get(selected_key)
    result = None

    if selected_item is not None:
        result = {
            "name": selected_item["label"],
            "compatible": labels_for(selected_item["compatible"]),
            "incompatible": labels_for(selected_item["incompatible"]),
        }

    vegetables = [
        {"key": key, "label": value["label"]}
        for key, value in sorted(VEGETABLES.items(), key=lambda item: item[1]["label"])
    ]
    return render_template(
        "index.html",
        vegetables=vegetables,
        selected_key=selected_key,
        result=result,
    )


if __name__ == "__main__":
    app.run(debug=True)
