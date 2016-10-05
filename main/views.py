from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

from main.models import Player

REFERENCE_URL = "http://www.basketball-reference.com/play-index/pgl_finder.cgi?request=1&player_id=&match=game&year_min=2016&year_max=2016&age_min=0&age_max=99&team_id=&opp_id=&is_playoffs=N&round_id=&game_num_type=&game_num_min=&game_num_max=&game_month=&game_day=&game_location=&game_result=&is_starter=&is_active=&is_hof=&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&c1stat=&c1comp=&c1val=&c2stat=&c2comp=&c2val=&c3stat=&c3comp=&c3val=&c4stat=&c4comp=&c4val=&is_dbl_dbl=Y&is_trp_dbl=&order_by=pts&order_by_asc=&offset="


def index(request):
    if request.method == "POST":
        date = request.POST["date"]
        players = Player.objects.filter(date=date)
        return render(request, "index.html", locals())
    else:
        players = Player.objects.filter()
        if not players:
            create_db()
        return render(request, "index.html")


def create_db():
    for d in range(0, 10000000, 100):
        response = requests.get(REFERENCE_URL + str(d))
        soup = BeautifulSoup(response.text, "lxml")
        trs = soup.find_all("tr")
        for tr in trs:
            tr = BeautifulSoup(str(tr), "lxml")
            try:
                Player.objects.create(name=tr.find_all(attrs={"data-stat": "player"})[0].text,
                                      game=tr.find_all(attrs={"data-stat": "team_id"})[0].text + "-" + tr.find_all(attrs={"data-stat": "opp_id"})[0].text,
                                      date=tr.find_all(attrs={"data-stat": "date_game"})[0].text)
            except Exception as e:
                print e.message