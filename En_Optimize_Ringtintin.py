import folium

map_center = [38.817473003788635, 30.534564935840955]
map = folium.Map(location=map_center, zoom_start=15.28)

stops = [
    {"name": "Rektörlük Durağı", "location": [38.81314535722232, 30.536205125683427], "icon": "user"},
    {"name": "Ara Durak", "location": [38.81478333783357, 30.535045468245222], "icon": "stop"},
    {"name": "Mühendislik Fakültesi Durağı", "location": [38.81698722768425, 30.53448538319871], "icon": "cog"},
    {"name": "Veterinerlik Fakültesi", "location": [38.82049725096702, 30.534160317990985], "icon": "cat"},
    {"name": "İlahiyat Fakültesi Durağı", "location": [38.822496556668646, 30.533322834168054], "icon": "mosque"},
    {"name": "Konservatuvar Durağı", "location": [38.82411559401791, 30.532936279785584], "icon": "music"},
    {"name": "Hukuk Fakültesi Durağı", "location": [38.827872788898354, 30.531864182114496], "icon": "balance-scale"},
    {"name": "Güzel Sanatlar Durağı", "location": [38.82415964346543, 30.5327195953422], "icon": "paint-brush"},
    {"name": "Ara Durak", "location": [38.82262095917927, 30.53306861505181], "icon": "stop"},
    {"name": "Veterinerlik Fakültesi Durağı", "location": [38.82082456841975, 30.533780406076215], "icon": "cat"},
    {"name": "Mühendislik Fakültesi Durağı", "location": [38.817706258405124, 30.53423578154881], "icon": "cog"},
    {"name": "Ara Durak", "location": [38.81480574403074, 30.534804873383017], "icon": "stop"},
    {"name": "Rektörlük Durağı", "location": [38.812584921949664, 30.536022015009255], "icon": "user"},
    {"name": "Fen Edebiyat Fakültesi Durağı", "location": [38.80939832404729, 30.535948456536772], "icon": "book"},
    {"name": "Fen Edebiyat Fakültesi Durağı", "location": [38.80942211969003, 30.536124128056855], "icon": "book"},
    {"name": "Üni Yurt", "location": [38.806276460227444, 30.53325842968936], "icon": "building"}
]

icon_prefix = "fa"
icon_color = "black"

def add_marker(stop):
    folium.Marker(
        location=stop["location"],
        popup=stop["name"],
        icon=folium.Icon(icon=stop["icon"], prefix=icon_prefix, color=icon_color)
    ).add_to(map)

for stop in stops:
    add_marker(stop)

map.save("Optimize_Ringtintin_no_polyline.html")

map.show_in_browser()