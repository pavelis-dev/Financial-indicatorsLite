from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.dialog import MDDialog
from kivy.uix.image import Image

import requests
from bs4 import BeautifulSoup

import datetime

from kivy.core.window import Window

Window.size = (360, 640)
# ----------------------------- Поиск значения индикатора -------------------------------
# парсинг сайтов
def get_html(url):
    try:
        r = requests.get(url)
        print('100')
        return r.text
    except:
        print('200')    # обработать отсутствие интернета
        get_html(url)


def get_ex_valuta(html):
    soup = BeautifulSoup(html, 'lxml')
    rate = soup.find('body').find(class_="page").find('span', id='ctl00_PageContent_tbxCurrentRate')
    return rate.text


def get_cb_valuta(html):
    soup = BeautifulSoup(html, 'lxml')
    rate = soup.find('body').find(class_="l-window l-window-overflow-mob").find(
        class_="chart__info__sum")
    return rate.text


def get_investing_valuta(html):
    soup = BeautifulSoup(html, 'lxml')
    rate = soup.find('body').find('div', id="__next").find(
        class_="desktop:relative desktop:bg-background-default").find(
        class_="instrument-price_instrument-price__3uw25 flex items-end flex-wrap font-bold")
    return rate.text


def get_investing_cript(html):
    soup = BeautifulSoup(html, 'lxml')
    rate = soup.find('body').find(class_="wrapper").find(
        'section', id="fullColumn").find(
        class_="top bold inlineblock")
    return rate.text


def get_investfunds_metall(html):
    soup = BeautifulSoup(html, 'lxml')
    rate = soup.find('body').find(class_="for_fixed_footer").find(
        class_="for_fixed_footer_middle").find(
        class_="widget_roll_wrapper js_roll_wdg_wrp js_tab_parent").find(class_="widget_price")
    return rate.text


def get_investing(html):
    soup = BeautifulSoup(html, 'lxml')
    rate = soup.find('body').find(class_="wrapper").find('section', id="leftColumn").find(
        class_="top bold inlineblock")
    return rate.text


def get_key_rate(html):
    soup = BeautifulSoup(html, 'lxml')
    rate = soup.find('body').find('main', id='content').find(
        class_="indicator_el _big-value").find(class_="indicator_el_value")
    return rate.text


def get_key_rate_frs(html):
    soup = BeautifulSoup(html, 'lxml')
    rate = soup.find('body').find(class_="wrapper").find(
        class_="releaseInfo bold").find_all('span')
    return rate


def get_inflation(html):
    soup = BeautifulSoup(html, 'lxml')
    rate = soup.find('tbody').find_all('tr')
    return rate[2].text, rate[3].text


def econ_ind(indicator):    # ссылки на сайты
    if indicator == 'gold':
        url = 'https://investfunds.ru/indexes/224/'
        return get_investfunds_metall(get_html(url))

    elif indicator == 'silver':
        url = 'https://investfunds.ru/indexes/225/'
        return get_investfunds_metall(get_html(url))

    elif indicator == 'platinum':
        url = 'https://investfunds.ru/indexes/399/'
        return get_investfunds_metall(get_html(url))

    elif indicator == 'palladium':
        url = 'https://investfunds.ru/indexes/400/'
        return get_investfunds_metall(get_html(url))

    #elif indicator == 'aluminum':
    #    url = 'https://ru.investing.com/commodities/aluminum-technical'
    #    return get_investing(get_html(url))

    elif indicator == 'usd':
        url = 'https://ru.investing.com/currencies/usd-rub'
        url2 = 'https://www.moex.com/ru/derivatives/currency-rate.aspx'
        url3 = 'https://quote.rbc.ru/ticker/72413'
        return get_investing_valuta(get_html(url)), get_ex_valuta(get_html(url2)), get_cb_valuta(get_html(url3))

    elif indicator == 'eur':
        url = 'https://ru.investing.com/currencies/eur-rub'
        url2 = 'https://www.moex.com/ru/derivatives/currency-rate.aspx?currency=EUR_RUB'
        url3 = 'https://quote.rbc.ru/ticker/72383'
        return get_investing_valuta(get_html(url)), get_ex_valuta(get_html(url2)), get_cb_valuta(get_html(url3))

    elif indicator == 'cny':
        url = 'https://ru.investing.com/currencies/cny-rub'
        url2 = 'https://quote.rbc.ru/ticker/72377'
        return get_investing_valuta(get_html(url)), get_cb_valuta(get_html(url2))

    elif indicator == 'gbp':
        url = 'https://ru.investing.com/currencies/gbp-rub'
        return get_investing_valuta(get_html(url))

    elif indicator == 'chf':
        url = 'https://ru.investing.com/currencies/chf-rub'
        return get_investing_valuta(get_html(url))

    elif indicator == 'jpy':
        url = 'https://ru.investing.com/currencies/jpy-rub'
        return get_investing_valuta(get_html(url))

    elif indicator == 'try':
        url = 'https://ru.investing.com/currencies/try-rub'
        return get_investing_valuta(get_html(url))

    elif indicator == 'bitcoin':
        url = 'https://ru.investing.com/crypto/bitcoin'
        return get_investing_cript(get_html(url))

    elif indicator == 'ethereum':
        url = 'https://ru.investing.com/crypto/ethereum'
        return get_investing_cript(get_html(url))

    elif indicator == 'tether':
        url = 'https://ru.investing.com/crypto/tether'
        return get_investing_cript(get_html(url))

    elif indicator == 'usd coin':
        url = 'https://ru.investing.com/crypto/usd-coin'
        return get_investing_cript(get_html(url))

    elif indicator == 'bnb':
        url = 'https://ru.investing.com/crypto/bnb'
        return get_investing_cript(get_html(url))

    elif indicator == 'binance':
        url = 'https://ru.investing.com/crypto/bnb'
        url2 = 'https://ru.investing.com/crypto/binance-usd'
        return get_investing_cript(get_html(url)), get_investing_cript(get_html(url2))

    elif indicator == 'binance_usd':
        url = 'https://ru.investing.com/crypto/binance-usd'
        return get_investing_cript(get_html(url))

    elif indicator == 'xrp':
        url = 'https://ru.investing.com/crypto/xrp'
        return get_investing_cript(get_html(url))

    elif indicator == 'сardano':
        url = 'https://ru.investing.com/crypto/cardano'
        return get_investing_cript(get_html(url))

    elif indicator == 'solana':
        url = 'https://ru.investing.com/crypto/solana'
        return get_investing_cript(get_html(url))

    elif indicator == 'dogecoin':
        url = 'https://ru.investing.com/crypto/dogecoin'
        return get_investing_cript(get_html(url))

    elif indicator == 'sber':
        url = 'https://ru.investing.com/equities/sberbank_rts-technical'
        url2 = 'https://ru.investing.com/equities/sberbank-p_rts-technical'
        return get_investing(get_html(url)), get_investing(get_html(url2))

    elif indicator == 'gazpromneft':
        url = 'https://ru.investing.com/equities/gazprom-neft_rts-technical'
        return get_investing(get_html(url))

    elif indicator == 'gazprom':
        url = 'https://ru.investing.com/equities/gazprom_rts-technical'
        return get_investing(get_html(url))

    elif indicator == 'nornikel':
        url = 'https://ru.investing.com/equities/gmk-noril-nickel_rts-technical'
        return get_investing(get_html(url))

    elif indicator == 'magnit':
        url = 'https://ru.investing.com/equities/magnit_rts-technical'
        return get_investing(get_html(url))

    elif indicator == 'lukoil':
        url = 'https://ru.investing.com/equities/lukoil_rts-technical'
        return get_investing(get_html(url))

    elif indicator == 'aeroflot':
        url = 'https://ru.investing.com/equities/aeroflot-technical'
        return get_investing(get_html(url))

    elif indicator == 'yandex':
        url = 'https://ru.investing.com/equities/yandex?cid=102063-technical'
        return get_investing(get_html(url))

    elif indicator == 'vtb':
        url = 'https://ru.investing.com/equities/vtb_rts-technical'
        return get_investing(get_html(url))

    elif indicator == 'dets_mir':
        url = 'https://ru.investing.com/equities/detskiy-mir-pao-technical'
        return get_investing(get_html(url))

    elif indicator == 'mts':
        url = 'https://ru.investing.com/equities/mts_rts-technical'
        return get_investing(get_html(url))

    elif indicator == 'rostelecom':
        url = 'https://ru.investing.com/equities/rostelecom-technical'
        return get_investing(get_html(url))

    elif indicator == 'fsk':
        url = 'https://ru.investing.com/equities/fsk-ees_rts-technical'
        return get_investing(get_html(url))

    elif indicator == 'severstal':
        url = 'https://ru.investing.com/equities/severstal_rts-technical'
        return get_investing(get_html(url))

    elif indicator == 'tatneft':
        url = 'https://ru.investing.com/equities/tatneft_rts-technical'
        url2 = 'https://ru.investing.com/equities/tatneft-p_rts-technical'
        return get_investing(get_html(url)), get_investing(get_html(url2))

    elif indicator == 'afk_sistem':
        url = 'https://ru.investing.com/equities/afk-sistema_rts-technical'
        return get_investing(get_html(url))

    elif indicator == 'surgutneftegaz':
        url = 'https://ru.investing.com/equities/surgutneftegas_rts-technical'
        url2 = 'https://ru.investing.com/equities/surgutneftegas-p_rts-technical'
        return get_investing(get_html(url)), get_investing(get_html(url2))

    elif indicator == 'unipro':
        url = 'https://ru.investing.com/equities/e.on-russia-technical'
        return get_investing(get_html(url))

    elif indicator == 'fosagro':
        url = 'https://ru.investing.com/equities/phosagro-technical'
        return get_investing(get_html(url))

    elif indicator == 'transneft':
        url = 'https://ru.investing.com/equities/transneft-p_rts-technical'
        return get_investing(get_html(url))

    elif indicator == 'rosneft':
        url = 'https://ru.investing.com/equities/rosneft_rts-technical'
        return get_investing(get_html(url))

    elif indicator == 'polus':
        url = 'https://ru.investing.com/equities/polyus-zoloto_rts-technical'
        return get_investing(get_html(url))

    elif indicator == 'novatek':
        url = 'https://ru.investing.com/equities/novatek_rts-technical'
        return get_investing(get_html(url))

    elif indicator == 'nlmk':
        url = 'https://ru.investing.com/equities/nlmk_rts-technical'
        return get_investing(get_html(url))

    elif indicator == 'mos_bir':
        url = 'https://ru.investing.com/equities/moskovskaya-birzha-oao-technical'
        return get_investing(get_html(url))

    elif indicator == 'mmk':
        url = 'https://ru.investing.com/equities/mmk_rts-technical'
        return get_investing(get_html(url))

    elif indicator == 'mkb':
        url = 'https://ru.investing.com/equities/moskovskiy-kreditnyi-bank-oao-technical'
        return get_investing(get_html(url))

    elif indicator == 'inter_rao':
        url = 'https://ru.investing.com/equities/inter-rao-ees_mm-technical'
        return get_investing(get_html(url))

    elif indicator == 'lsr':
        url = 'https://ru.investing.com/equities/lsr-group_rts-technical'
        return get_investing(get_html(url))

    elif indicator == 'pik':
        url = 'https://ru.investing.com/equities/pik_rts-technical'
        return get_investing(get_html(url))

    elif indicator == 'alrosa':
        url = 'https://ru.investing.com/equities/alrosa-ao-technical'
        return get_investing(get_html(url))

    elif indicator == 'x5ret':
        url = 'https://ru.investing.com/equities/x5-retail-grp?cid=1061926-technical'
        return get_investing(get_html(url))

    elif indicator == 'vkontakt':
        url = 'https://ru.investing.com/equities/mail.ru-grp-wi?cid=1163363-technical'
        return get_investing(get_html(url))

    elif indicator == 'tinkof':
        url = 'https://ru.investing.com/equities/tcs-group-holding-plc?cid=1153662-technical'
        return get_investing(get_html(url))

    elif indicator == 'rosseti':
        url = 'https://ru.investing.com/equities/rosseti-ao-technical'
        return get_investing(get_html(url))

    elif indicator == 'qiwi':
        url = 'https://ru.investing.com/equities/qiwi-plc-technical?cid=960754'
        return get_investing(get_html(url))

    elif indicator == 'poly':
        url = 'https://ru.investing.com/equities/polymetal?cid=44465-technical'
        return get_investing(get_html(url))

    elif indicator == 'petropavl':
        url = 'https://ru.investing.com/equities/petropavlovsk-technical?cid=1163242'
        return get_investing(get_html(url))

    elif indicator == 'ozon':
        url = 'https://ru.investing.com/equities/ozon-holdings-plc-technical?cid=1167498'
        return get_investing(get_html(url))

    elif indicator == 'rusal':
        url = 'https://ru.investing.com/equities/united-company-rusal-plc%60-technical'
        return get_investing(get_html(url))

    elif indicator == 'headhunter':
        url = 'https://ru.investing.com/equities/headhunter-group-plc?cid=1166764-technical'
        return get_investing(get_html(url))

    elif indicator == 'globaltrans':
        url = 'https://ru.investing.com/equities/globaltrans-inv?cid=1167212-technical'
        return get_investing(get_html(url))

    elif indicator == 'rusgidro':
        url = 'https://ru.investing.com/equities/gidroogk-011d-technical'
        return get_investing(get_html(url))

    elif indicator == 'apple':
        url = 'https://ru.investing.com/equities/apple-computer-inc-technical'
        return get_investing(get_html(url))

    elif indicator == 'tesla':
        url = 'https://ru.investing.com/equities/tesla-motors-technical'
        return get_investing(get_html(url))

    elif indicator == 'meta':
        url = 'https://ru.investing.com/equities/facebook-inc-technical'
        return get_investing(get_html(url))

    elif indicator == 'microsoft':
        url = 'https://ru.investing.com/equities/microsoft-corp-technical'
        return get_investing(get_html(url))

    elif indicator == 'micron':
        url = 'https://ru.investing.com/equities/micron-tech-technical'
        return get_investing(get_html(url))

    elif indicator == 'amd':
        url = 'https://ru.investing.com/equities/adv-micro-device-technical'
        return get_investing(get_html(url))

    elif indicator == 'coca_cola':
        url = 'https://ru.investing.com/equities/coca-cola-co-technical'
        return get_investing(get_html(url))

    elif indicator == 'twitter':
        url = 'https://ru.investing.com/equities/twitter-inc-technical'
        return get_investing(get_html(url))

    elif indicator == 'amazon':
        url = 'https://ru.investing.com/equities/amazon-com-inc-technical'
        return get_investing(get_html(url))

    elif indicator == 'boeing':
        url = 'https://ru.investing.com/equities/boeing-co-technical'
        return get_investing(get_html(url))

    elif indicator == 'chevron':
        url = 'https://ru.investing.com/equities/chevron-technical'
        return get_investing(get_html(url))

    elif indicator == 'cisco':
        url = 'https://ru.investing.com/equities/cisco-sys-inc-technical'
        return get_investing(get_html(url))

    elif indicator == 'ibm':
        url = 'https://ru.investing.com/equities/ibm-technical'
        return get_investing(get_html(url))

    elif indicator == 'nvidia':
        url = 'https://ru.investing.com/equities/nvidia-corp-technical'
        return get_investing(get_html(url))

    elif indicator == 'netflix':
        url = 'https://ru.investing.com/equities/netflix,-inc.-technical'
        return get_investing(get_html(url))

    elif indicator == 'qualcomm':
        url = 'https://ru.investing.com/equities/qualcomm-inc-technical'
        return get_investing(get_html(url))

    elif indicator == 'key_rate':
        url = 'https://www.cbr.ru/dkp/'
        return get_key_rate(get_html(url))

    elif indicator == 'key_rate_frs':
        url = 'https://ru.investing.com/economic-calendar/interest-rate-decision-168'
        return get_key_rate_frs(get_html(url))

    elif indicator == 'key_rate_knr':
        url = 'https://ru.investing.com/economic-calendar/pboc-loan-prime-rate-1967'
        return get_key_rate_frs(get_html(url))

    elif indicator == 'key_rate_turk':
        url = 'https://ru.investing.com/economic-calendar/turkish-one-week-repo-rate-409'
        return get_key_rate_frs(get_html(url))

    elif indicator == 'key_rate_japan':
        url = 'https://ru.investing.com/economic-calendar/interest-rate-decision-165'
        return get_key_rate_frs(get_html(url))

    elif indicator == 'key_rate_india':
        url = 'https://ru.investing.com/economic-calendar/indian-interest-rate-decision-597'
        return get_key_rate_frs(get_html(url))

    elif indicator == 'key_rate_brazil':
        url = 'https://ru.investing.com/economic-calendar/brazilian-interest-rate-decision-415'
        return get_key_rate_frs(get_html(url))

    elif indicator == 'inflation':
        url = 'https://уровень-инфляции.рф/'
        return get_inflation(get_html(url))

    elif indicator == 'inflation_usa':
        url = 'https://ru.investing.com/economic-calendar/cpi-733'
        return get_key_rate_frs(get_html(url))

    elif indicator == 'inflation_germany':
        url = 'https://ru.investing.com/economic-calendar/german-cpi-737'
        return get_key_rate_frs(get_html(url))

    elif indicator == 'inflation_china':
        url = 'https://ru.investing.com/economic-calendar/chinese-cpi-459'
        return get_key_rate_frs(get_html(url))

    elif indicator == 'inflation_turk':
        url = 'https://ru.investing.com/economic-calendar/turkish-cpi-871'
        return get_key_rate_frs(get_html(url))

    elif indicator == 'oil':
        url = 'https://ru.investing.com/commodities/brent-oil-technical'
        url2 = 'https://ru.investing.com/commodities/crude-oil-technical'
        return get_investing(get_html(url)), get_investing(get_html(url2))

    elif indicator == 'imoex':
        url = 'https://ru.investing.com/indices/mcx-technical'
        return get_investing(get_html(url))

    elif indicator == 'snp500':
        url = 'https://ru.investing.com/indices/us-spx-500-technical'
        return get_investing(get_html(url))


def get_user_text(message):   # формирование ответов
    if 'акция' in message.lower() or 'акции' in message.lower():

        # акции рф
        if 'сбер' in message.lower():
            v = 'sber'
            return f'Акции\n   Сбербанк ПАО (SBER):\n            ' \
                   f'{econ_ind(v)[0][:7].strip()} руб. ({econ_ind(v)[0][-8:].strip()})\n' \
                   f'   Сбербанк (прив.) (SBER_p):\n            ' \
                   f'{econ_ind(v)[1][:7].strip()} руб. ({econ_ind(v)[1][-8:].strip()})'

        elif 'газпром нефт' in message.lower() or 'газпром-нефт' in message.lower() or 'газпромнефт' in message.lower():
            v = 'gazpromneft'
            return f'Акции\n   Газпром нефть (SIBN):\n            ' \
                   f'{econ_ind(v)[:7].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'газпром' in message.lower():
            v = 'gazprom'
            return f'Акции\n   Газпром ПАО (GAZP):\n            ' \
                   f'{econ_ind(v)[:7].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'норникел' in message.lower() or 'норильского никеля' in message.lower() or \
                'норильский никел' in message.lower():
            v = 'nornikel'
            return f'Акции\n   ГМК Норильский Никель ПАО\n   (GMKN):\n            ' \
                   f'{econ_ind(v)[:8].strip().replace(".", " ")} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'магнит' in message.lower():
            v = 'magnit'
            return f'Акции\n   ОАО Магнит (MGNT):\n            {econ_ind(v)[:8].strip().replace(".", " ")} руб.' \
                   f' ({econ_ind(v)[-8:].strip()})'

        elif 'лукойл' in message.lower():
            v = 'lukoil'
            return f'Акции\n   НК Лукойл ПАО (LKOH):\n            {econ_ind(v)[:8].strip().replace(".", " ")} руб.' \
                   f' ({econ_ind(v)[-8:].strip()})'

        elif 'аэрофлот' in message.lower():
            v = 'aeroflot'
            return f'Акции\n   ОАО Аэрофлот (AFLT):\n            ' \
                   f'{econ_ind(v)[:6].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'яндекс' in message.lower() or 'yandex' in message.lower():
            v = 'yandex'
            return f'Акции\n   Яндекс Н.В. (YNDX):\n            {econ_ind(v)[:8].strip().replace(".", " ")} руб.' \
                   f' ({econ_ind(v)[-8:].strip()})'

        elif 'втб' in message.lower():
            v = 'vtb'
            return f'Акции\n   ВТБ RTS ПАО (VTBR):\n            ' \
                   f'{econ_ind(v)[:9].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'детского мира' in message.lower() or 'детский мир' in message.lower():
            v = 'dets_mir'
            return f'Акции\n   Детский мир ПАО (DSKY):\n            ' \
                   f'{econ_ind(v)[:6].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'мтс' in message.lower():
            v = 'mts'
            return f'Акции\n   Мобильные ТелеСистемы ПАО\n   (MTSS):\n            {econ_ind(v)[:7].strip()} руб.' \
                   f' ({econ_ind(v)[-8:].strip()})'

        elif 'ростелеком' in message.lower():
            v = 'rostelecom'
            return f'Акции\n   Ростелеком ПАО (RTKM):\n            ' \
                   f'{econ_ind(v)[:6].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'фск' in message.lower():
            v = 'fsk'
            return f'Акции\n   ФСК ЕЭС ОАО (FEES):\n            ' \
                   f'{econ_ind(v)[:7].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'северстал' in message.lower():
            v = 'severstal'
            return f'Акции\n   ОАО Северсталь (CHMF):\n            ' \
                   f'{econ_ind(v)[:7].strip().replace(".", " ")} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'татнефт' in message.lower():
            v = 'tatneft'
            return f'Акции\n   ОАО Татнефть (TATN):\n            {econ_ind(v)[0][:7].strip()} руб.' \
                   f' ({econ_ind(v)[0][-8:].strip()})\n   Татнефть (прив.) (TATN_p):\n            ' \
                   f'{econ_ind(v)[1][:7].strip()} руб. ({econ_ind(v)[1][-8:].strip()})'

        elif 'систем' in message.lower():
            v = 'afk_sistem'
            return f'Акции\n   ОАО АФК Система (AFKS):\n            ' \
                   f'{econ_ind(v)[:6].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'сургутнефтегаз' in message.lower():
            v = 'surgutneftegaz'
            return f'Акции\n   Сургутнефтегаз ПАО (SNGS):\n            {econ_ind(v)[0][:7].strip()} руб.' \
                   f' ({econ_ind(v)[0][-8:].strip()})\n   Сургутнефтегаз (прив.) (SNGS_p):\n            ' \
                   f'{econ_ind(v)[1][:7].strip()} руб. ({econ_ind(v)[1][-8:].strip()})'

        elif 'юнипро' in message.lower():
            v = 'unipro'
            return f'Акции\n   Юнипро ПАО (UPRO):\n            ' \
                   f'{econ_ind(v)[:6].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'фосагро' in message.lower():
            v = 'fosagro'
            return f'Акции\n   ОАО ФосАгро (PHOR):\n            ' \
                   f'{econ_ind(v)[:8].strip().replace(".", " ")} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'транснефт' in message.lower():
            v = 'transneft'
            return f'Акции\n   Транснефть (прив.) (TRNF_p):\n            ' \
                   f'{econ_ind(v)[:8].strip().replace(".", " ")} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'роснефт' in message.lower():
            v = 'rosneft'
            return f'Акции\n   Роснефть (ROSN):\n            ' \
                   f'{econ_ind(v)[:7].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'полюс' in message.lower():
            v = 'polus'
            return f'Акции\n   Полюс Золото ПАО (PLZL):\n            ' \
                   f'{econ_ind(v)[:9].strip().replace(".", " ")} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'новатэк' in message.lower() or 'акции новатек' in message.lower():
            v = 'novatek'
            return f'Акции\n   ОАО НОВАТЭК (NVTK):\n            ' \
                   f'{econ_ind(v)[:9].strip().replace(".", " ")} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'нлмк' in message.lower():
            v = 'nlmk'
            return f'Акции\n   Новолипецкий металлургический\n   комбинат НЛМК (NLMK):\n            ' \
                   f'{econ_ind(v)[:7].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'мосбирж' in message.lower() or 'московской бирж' in message.lower() or \
                'московская бирж' in message.lower():
            v = 'mos_bir'
            return f'Акции\n   Московская биржа\n   ОАО ММВБ (MOEX):\n            ' \
                   f'{econ_ind(v)[:6].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'ммк' in message.lower():
            v = 'mmk'
            return f'Акции\n   Магнитогорский металлургический\n   комбинат ПАО (MAGN):\n            ' \
                   f'{econ_ind(v)[:6].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'мкб' in message.lower():
            v = 'mkb'
            return f'Акции\n   Московский кредитный\n   банк (CBOM):\n            ' \
                   f'{econ_ind(v)[:6].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'интер рао' in message.lower():
            v = 'inter_rao'
            return f'Акции\n   Интер РАО ЕЭС ОАО (IRAO):\n            ' \
                   f'{econ_ind(v)[:7].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'лср' in message.lower():
            v = 'lsr'
            return f'Акции\n   Группа ЛСР (LSRG):\n            ' \
                   f'{econ_ind(v)[:7].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'пик' in message.lower():
            v = 'pik'
            return f'Акции\n   ОАО Группа Компаний ПИК (PIKK):\n            ' \
                   f'{econ_ind(v)[:7].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'алрос' in message.lower():
            v = 'alrosa'
            return f'Акции\n   ОАО АК АЛРОСА (ALRS):\n            ' \
                   f'{econ_ind(v)[:6].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'X5' in message.lower() or 'пятерочки' in message.lower() or 'five' in message.lower():
            v = 'x5ret'
            return f'Акции\n   X5 Retail Group (FIVEDR):\n            ' \
                   f'{econ_ind(v)[:7].strip().replace(".", " ")} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'vk' in message.lower() or 'вк' in message.lower():
            v = 'vkontakt'
            return f'Акции\n   VK Company Ltd DRC (VKCODR):\n            ' \
                   f'{econ_ind(v)[:7].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'тинькоф' in message.lower() or 'tcs' in message.lower():
            v = 'tinkof'
            return f'Акции\n   TCS Group Holding PLC (TCSGDR):\n            ' \
                   f'{econ_ind(v)[:9].strip().replace(".", " ")} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'rossiyskiye seti' in message.lower() or 'российские сети' in message.lower() or \
                'росийские сети' in message.lower() or 'российских сет' in message.lower() or \
                'акция росийских сет' in message.lower() or 'рос сет' in message.lower() or 'россет' in message.lower():
            v = 'rosseti'
            return f'Акции\n   Rossiyskiye Seti PAO (RSTI):\n            ' \
                   f'{econ_ind(v)[:6].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'киви' in message.lower() or 'qiwi' in message.lower():
            v = 'qiwi'
            return f'Акции\n   QIWI plc (QIWIDR):\n            ' \
                   f'{econ_ind(v)[:7].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'полиметал' in message.lower() or 'poly' in message.lower():
            v = 'poly'
            return f'Акции\n   Polymetal International PLC (POLY):\n            ' \
                   f'{econ_ind(v)[:7].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'петропавловск' in message.lower() or 'petropavlovsk' in message.lower():
            v = 'petropavl'
            return f'Акции\n   Petropavlovsk PLC (POGR):\n            ' \
                   f'{econ_ind(v)[:5].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'озон' in message.lower() or 'ozon' in message.lower():
            v = 'ozon'
            return f'Акции\n   Ozon Holdings PLC (OZONDR):\n            ' \
                   f'{econ_ind(v)[:7].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'русал' in message.lower() or 'rusal' in message.lower():
            v = 'rusal'
            return f'Акции\n   OK Rusal MKPAO (RUAL):\n            ' \
                   f'{econ_ind(v)[:7].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'хеадхантер' in message.lower() or 'headhunter' in message.lower() or 'хедхантер' in message.lower():
            v = 'headhunter'
            return f'Акции\n   HeadHunter Group PLC\n   ADR (HHRUDR):\n            ' \
                   f'{econ_ind(v)[:9].strip().replace(".", " ")} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'глобалтранс' in message.lower() or 'globaltrans' in message.lower():
            v = 'globaltrans'
            return f'Акции\n   Globaltrans Investment PLC (GLTRDR):\n            ' \
                   f'{econ_ind(v)[:7].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        elif 'русгидр' in message.lower() or 'rusgidr' in message.lower():
            v = 'rusgidro'
            return f'Акции\n   FGK Rusgidro PAO (HYDR):\n            ' \
                   f'{econ_ind(v)[:7].strip()} руб. ({econ_ind(v)[-8:].strip()})'

        # иностранные акции
        elif 'apple' in message.lower() or 'эппл' in message.lower():
            v = 'apple'
            return f'Акции\n   Apple Inc (AAPL):\n            {econ_ind(v)[:7].strip()} $ ({econ_ind(v)[-8:].strip()})'

        elif 'tesla' in message.lower() or 'тесла' in message.lower() or 'теслы' in message.lower():
            v = 'tesla'
            return f'Акции\n   Tesla Inc (TSLA):\n            {econ_ind(v)[:7].strip()} $ ({econ_ind(v)[-8:].strip()})'

        elif 'meta plat' in message.lower() or 'facebook' in message.lower() or 'фейсбук' in message.lower():
            v = 'meta'
            return f'Акции\n   Meta Platforms Inc (FB):\n            ' \
                   f'{econ_ind(v)[:7].strip()} $ ({econ_ind(v)[-8:].strip()})'

        elif 'microsoft' in message.lower() or 'майкрософт' in message.lower():
            v = 'microsoft'
            return f'Акции\n   Microsoft Corporation (MSFT):\n            ' \
                   f'{econ_ind(v)[:7].strip()} $ ({econ_ind(v)[-8:].strip()})'

        elif 'micron' in message.lower() or 'микрон' in message.lower():
            v = 'micron'
            return f'Акции\n   Micron Technology Inc (MU):\n            ' \
                   f'{econ_ind(v)[:7].strip()} $ ({econ_ind(v)[-8:].strip()})'

        elif 'amd' in message.lower():
            v = 'amd'
            return f'Акции\n   Advanced Micro Devices Inc (AMD):\n            ' \
                   f'{econ_ind(v)[:7].strip()} $ ({econ_ind(v)[-8:].strip()})'

        elif 'кока кол' in message.lower() or 'coca col' in message.lower() or 'кока-кол' in message.lower() or \
                'coca-col' in message.lower() or 'кокакол' in message.lower():
            v = 'coca_cola'
            return f'Акции\n   Coca-Cola Co (KO):\n            ' \
                   f'{econ_ind(v)[:7].strip()} $ ({econ_ind(v)[-8:].strip()})'

        elif 'twitter' in message.lower() or 'twiter' in message.lower() or 'твитер' in message.lower() or \
                'акции твиттер' in message.lower():
            v = 'twitter'
            return f'Акции\n   Twitter Inc (TWTR):\n            ' \
                   f'{econ_ind(v)[:7].strip()} $ ({econ_ind(v)[-8:].strip()})'

        elif 'amazon' in message.lower() or 'амазон' in message.lower():
            v = 'amazon'
            return f'Акции\n   Amazon.cоm Inc (AMZN):\n            {econ_ind(v)[:9].strip().replace(".", " ")} $' \
                   f' ({econ_ind(v)[-8:].strip()})'

        elif 'boeing' in message.lower() or 'боинг' in message.lower():
            v = 'boeing'
            return f'Акции\n   Boeing Co (BA):\n            ' \
                   f'{econ_ind(v)[:7].strip()} $ ({econ_ind(v)[-8:].strip()})'

        elif 'chevron' in message.lower():
            v = 'chevron'
            return f'Акции\n   Chevron Corp (CVX):\n            ' \
                   f'{econ_ind(v)[:7].strip()} $ ({econ_ind(v)[-8:].strip()})'

        elif 'cisco' in message.lower():
            v = 'chevron'
            return f'Акции\n   Cisco Systems Inc (CSCO):\n            ' \
                   f'{econ_ind(v)[:7].strip()} $ ({econ_ind(v)[-8:].strip()})'

        elif 'ibm' in message.lower():
            v = 'ibm'
            return f'Акции\n   International Business Machines\n   (IBM):  ' \
                   f'{econ_ind(v)[:7].strip()} $ ({econ_ind(v)[-8:].strip()})'

        elif 'nvidia' in message.lower():
            v = 'nvidia'
            return f'Акции\n   NVIDIA Corporation (NVDA):\n            ' \
                   f'{econ_ind(v)[:7].strip()} $ ({econ_ind(v)[-8:].strip()})'

        elif 'netflix' in message.lower():
            v = 'netflix'
            return f'Акции\n   Netflix Inc (NFLX):\n            ' \
                   f'{econ_ind(v)[:7].strip()} $ ({econ_ind(v)[-8:].strip()})'

        elif 'qualcom' in message.lower():
            v = 'qualcomm'
            return f'Акции\n   Qualcomm Incorporated (QCOM):\n            ' \
                   f'{econ_ind(v)[:7].strip()} $ ({econ_ind(v)[-8:].strip()})'

        else:
            return 'Акция не найдена'

    # металлы
    elif 'золот' in message.lower():
        v = 'gold'
        return f'Золото\n   Банк России (ЦБ):  {econ_ind(v).strip()[:8].replace(".", ",")} руб./г.'

    elif 'серебр' in message.lower():
        v = 'silver'
        return f'Серебро\n   Банк России (ЦБ):  {econ_ind(v).strip()[:5].replace(".", ",")} руб./г.'

    elif 'платин' in message.lower():
        v = 'platinum'
        return f'Платина\n   Банк России (ЦБ):  {econ_ind(v).strip()[:8].replace(".", ",")} руб./г'

    elif 'паллади' in message.lower():
        v = 'palladium'
        return f'Палладий\n   Банк России (ЦБ):  {econ_ind(v).strip()[:8].replace(".", ",")} руб./г'

    #elif 'алюмини' in message.lower():
    #    v = 'aluminum'
    #    return f'Алюминий - (MAL3):\n            {econ_ind(v)[:9].strip().replace(".", " ")} ' \
    #           f'$/тонна ({econ_ind(v)[-8:].strip()})'

    # валюта
    elif 'доллар' in message.lower():
        v = 'usd'
        return f'Доллар\n   Форекс:  {econ_ind(v)[0][:5]} руб. {econ_ind(v)[0][-8:]}\n   Биржа:' \
               f' {econ_ind(v)[1][18:24]} руб.\n   Банк России (ЦБ):  {econ_ind(v)[2][1:6]} руб.'

    elif 'евро' in message.lower():
        v = 'eur'
        return f'Евро\n   Форекс:  {econ_ind(v)[0][:5]} руб. {econ_ind(v)[0][-8:]}\n   ' \
               f'Биржа: {econ_ind(v)[1][18:24]} руб.\n   Банк России (ЦБ):  {econ_ind(v)[2][1:6]} руб.'

    elif 'юань' in message.lower() or 'юаня' in message.lower() or 'юани' in message.lower():
        v = 'cny'
        return f'Китайский Юань\n   Форекс:  {econ_ind(v)[0][:4]} руб. {econ_ind(v)[0][-8:]}\n   ' \
               f'Банк России (ЦБ):  {econ_ind(v)[1][1:5]} руб.'

    elif 'фунт' in message.lower():
        v = 'gbp'
        return f'Британский Фунт\n   Форекс:  {econ_ind(v)[:5]} руб. {econ_ind(v)[-8:]}'

    elif 'франк' in message.lower():
        v = 'chf'
        return f'Швейцарский Франк\n   Форекс:  {econ_ind(v)[:5]} руб. {econ_ind(v)[-8:]}'

    elif 'йена' in message.lower() or 'йены' in message.lower() or \
            'иена' in message.lower() or 'иены' in message.lower():
        v = 'jpy'
        return f'Японская Иена\n   Форекс:  {econ_ind(v)[:4]} руб. {econ_ind(v)[-8:]}'

    elif 'турецкая лира' in message.lower() or 'турецкие лиры' in message.lower():
        v = 'try'
        return f'Турецкая Лира\n   Форекс:  {econ_ind(v)[:5]} руб. {econ_ind(v)[-8:]}'

    # криптовалюты
    elif 'биткоин' in message.lower() or 'bitcoin' in message.lower():
        v = 'bitcoin'
        return f'Криптовалюта  Bitcoin:  {econ_ind(v)[2:11].replace(".", " ")} $'

    elif 'эфириум' in message.lower() or 'ethereum' in message.lower():
        v = 'ethereum'
        return f'Криптовалюта  Ethereum:  {econ_ind(v)[2:11].replace(".", " ")} $'

    elif 'tether' in message.lower() or 'usdt' in message.lower():
        v = 'tether'
        return f'Криптовалюта  Tether:  {econ_ind(v)[2:9].replace(".", " ")} $'

    elif 'usd c' in message.lower() or 'usdc' in message.lower():
        v = 'usd coin'
        return f'Криптовалюта  USD Coin:  {econ_ind(v)[2:9]} $'

    elif 'bnb' in message.lower():
        v = 'bnb'
        return f'Криптовалюта  BNB:  {econ_ind(v)[2:9]} $'

    elif 'binance usd' in message.lower():
        v = 'binance_usd'
        return f'Криптовалюта\n            Binance USD:  {econ_ind(v)[2:9]} $'

    elif 'binance' in message.lower():
        v = 'binance'
        return f'Криптовалюта\n            BNB:  {econ_ind(v)[0][2:9]} $\n            ' \
               f'Binance USD:  {econ_ind(v)[1][2:9]} $'

    elif 'xrp' in message.lower() or 'ripple' in message.lower():
        v = 'xrp'
        return f'Криптовалюта  XRP:  {econ_ind(v)[2:9]} $'

    elif 'cardano' in message.lower():
        v = 'сardano'
        return f'Криптовалюта  Cardano:  {econ_ind(v)[2:9]} $'

    elif 'solana' in message.lower():
        v = 'solana'
        return f'Криптовалюта  Solana:  {econ_ind(v)[2:9]} $'

    elif 'dogecoin' in message.lower():
        v = 'dogecoin'
        return f'Криптовалюта  Dogecoin:  {econ_ind(v)[2:11]} $'

    # финансовые показатели
    elif 'ключевая ставка цб' in message.lower() or 'ключевая ставка рф' in message.lower() or\
            'ключевая ставка росси' in message.lower() or\
            'ключевая ставка центрального банка' in message.lower():
        v = 'key_rate'
        return f'Ключевая ставка\n   Центрального Банка РФ:  {econ_ind(v).strip()}'

    elif 'ставка фрс' in message.lower() or 'фрс сша' in message.lower() or 'ставка сша' in message.lower() or\
            'ключевая ставка сша' in message.lower() or 'ключевая ставка америк' in message.lower():
        v = 'key_rate_frs'
        return f'Ключевая ставка\n   ФРС США:  {econ_ind(v)[1].text[5:]}'

    elif 'ставка кита' in message.lower() or 'ставка кнр' in message.lower() or\
            'ставка народного банка кита' in message.lower():
        v = 'key_rate_knr'
        return f'Ключевая ставка\n   Народного банка Китая: {econ_ind(v)[1].text[5:]}'

    elif 'ставка турци' in message.lower() or 'ставка цб турци' in message.lower() or \
            'ставка банка турци' in message.lower() or 'ставка центрального банка турци' in message.lower():
        v = 'key_rate_turk'
        return f'Ключевая ставка\n   Центрального Банка Турции: {econ_ind(v)[1].text[5:]}'

    elif 'ставка япони' in message.lower() or 'ставка цб япони' in message.lower() or \
            'ставка банка япони' in message.lower() or 'ставка центрального банка япони' in message.lower():
        v = 'key_rate_japan'
        return f'Ключевая ставка\n   Центрального Банка Японии: {econ_ind(v)[1].text[5:]}'

    elif 'ставка инди' in message.lower() or 'ставка цб инди' in message.lower() or \
            'ставка банка инди' in message.lower() or 'ставка резервного банка инди' in message.lower():
        v = 'key_rate_india'
        return f'Ключевая ставка\n   Резервного Банка Индии: {econ_ind(v)[1].text[5:]}'

    elif 'ставка бразили' in message.lower() or 'ставка цб бразили' in message.lower() or \
            'ставка банка бразили' in message.lower() or 'ставка центрального банка бразили' in message.lower():
        v = 'key_rate_brazil'
        return f'Ключевая ставка\n   Центрального Банка Бразилии: {econ_ind(v)[1].text[5:]}'

    elif 'ключевая ставка' in message.lower():
        return 'запрос'

    elif 'инфляция рф' in message.lower() or 'инфляция в рф' in message.lower() or\
            'инфляция росси' in message.lower() or 'инфляция в росси' in message.lower():
        v = 'inflation'
        return f'Инфляция в РФ:\n   За последние 12 месяцев: {econ_ind(v)[0][-6:].replace(".", ",")}\n   ' \
               f'С начала года: {econ_ind(v)[1][-6:].replace(".", ",")}'

    elif 'инфляция сша' in message.lower() or 'инфляция америк' in message.lower() or \
            'инфляция в сша' in message.lower() or 'инфляция в америк' in message.lower() or \
            'индекс потребительских цен сша' in message.lower() or \
            'индекс потребительских цен америк' in message.lower() or \
            'индекс потребительских цен в сша' in message.lower() or \
            'индекс потребительских цен в америк' in message.lower():
        v = 'inflation_usa'
        return f'Индекс потребительских цен\n   в США: {econ_ind(v)[1].text[5:]}'

    elif 'инфляция германи' in message.lower() or 'инфляция в германи' in message.lower() or \
            'индекс потребительских цен германи' in message.lower() or \
            'индекс потребительских цен в германи' in message.lower():
        v = 'inflation_germany'
        return f'Индекс потребительских цен\n   в Германии: {econ_ind(v)[1].text[5:]}'

    elif 'инфляция китая' in message.lower() or 'инфляция в китае' in message.lower() or \
            'индекс потребительских цен китай' in message.lower() or \
            'индекс потребительских цен в китае' in message.lower() or 'инфляция китай' in message.lower():
        v = 'inflation_china'
        return f'Индекс потребительских цен\n   в Китае: {econ_ind(v)[1].text[5:]}'

    elif 'инфляция турци' in message.lower() or 'инфляция в турци' in message.lower() or \
            'индекс потребительских цен турци' in message.lower() or \
            'индекс потребительских цен в турци' in message.lower():
        v = 'inflation_turk'
        return f'Индекс потребительских цен\n   в Турции: {econ_ind(v)[1].text[5:]}'

    elif 'инфляция' in message.lower():
        return 'запрос2'

    elif 'нефть' in message.lower() or 'нефти' in message.lower():
        v = 'oil'
        return f'Фьючерс на нефть\n   Brent:' \
               f'  {econ_ind(v)[0][:7].strip()} $/баррель ({econ_ind(v)[0][-8:].strip()})\n   WTI:' \
               f'  {econ_ind(v)[1][:7].strip()} $/баррель ({econ_ind(v)[1][-8:].strip()})'

    # индексы
    elif 'индекс мосбирж' in message.lower() or 'imoex' in message.lower() or 'индекс мос бирж' in message.lower() or \
            'индекс московской бирж' in message.lower() or 'индекс moex' in message.lower():
        v = 'imoex'
        return f'Индекс\n   ММВБ – Индекс Мосбиржи\n   (IMOEX):  {econ_ind(v)[:9].strip().replace(".", " ")} $' \
               f' ({econ_ind(v)[-8:].strip()})'

    elif 'индекс s&p 500' in message.lower() or 's&p 500' in message.lower() or 's&p500' in message.lower() or \
            'индекс s&p500' in message.lower() or 'индекс snp 500' in message.lower() or \
            'snp 500' in message.lower() or 'snp500' in message.lower() or 'индекс snp500' in message.lower() or \
            'индекс spx' in message.lower():
        v = 'snp500'
        return f'Индекс\n   S&P 500 (SPX):\n            {econ_ind(v)[:9].strip().replace(".", " ")} $' \
               f' ({econ_ind(v)[-8:].strip()})'

    else:
        return 'Неверный запрос'
# ---------------------------------------------------------------------------------------


class FinancialIndicatorsLiteApp(MDApp):
    dialog = None

    def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="формат поиска:",
                text='   "инфляция <страна>"\n   "ключевая ставка <страна>"\n   "акции <компания>"\n   '
                     '"<название валюты>"\n   "<название криптовалюты>"\n   "<название металла>"\n   '
                     '"<специальные показатели>\n                   '
                     '(например: нефть)"\n   и т.д. экспериментируйте! :)',
                radius=[25, 7, 25, 7],
                pos_hint={'center_x': 0.5, 'center_y': 0.7}
                )
        self.dialog.open()

    def color_change(self):
        if self.theme_cls.primary_palette == 'Blue':
            self.theme_cls.primary_palette = 'DeepOrange'
            with open('settings.txt', 'w', encoding='utf-8') as file:
                file.write(f'DeepOrange')
        else:
            self.theme_cls.primary_palette = 'Blue'
            with open('settings.txt', 'w', encoding='utf-8') as file:
                file.write(f'Blue')

    def tx(self, args):
        self.label2.text = 'Ожидайте'
        self.answer.text = ''
        self.label.text = ''

    def change_text(self, args):
        try:
            internet = requests.get('https://www.google.com/')  # проверка интернет соединения
            now = datetime.datetime.now()
            print('прошло')
            val = self.input.text
            val2 = get_user_text(val)
            if val2 == 'Неверный запрос':
                self.label2.text = ''
                self.answer.text = ''
                self.label.text = 'Неверный запрос'
            elif val2 == 'запрос':
                self.label2.text = ''
                self.answer.text = ''
                self.label.text = 'Формат запроса:\n\n   "Ключевая ставка  <СТРАНЫ>"'
            elif val2 == 'запрос2':
                self.label2.text = ''
                self.answer.text = ''
                self.label.text = 'Формат запроса:\n\n   "Инфляция  <СТРАНЫ>"'
            elif val2 == 'Акция не найдена':
                self.label2.text = ''
                self.answer.text = ''
                self.label.text = 'Акция не найдена'
            else:
                self.label2.text = ''
                self.answer.text = val2
                self.label.text = 'Выполнено ' + now.strftime("%d.%m.%Y в %H:%M")
        except:  # интернет остутствует
            self.label2.text = ''
            self.answer.text = ''
            self.label.text = 'Проверьте интернет соединение'

    def build(self):
        with open('settings.txt', 'r', encoding='utf-8') as file:
            theme_color = file.read()
        self.theme_cls.primary_palette = theme_color
        screen = MDScreen()

        # верхний бар
        self.toolbar = MDToolbar(title='Financial Indicators Lite')
        self.toolbar.pos_hint = {'top': 1}
        self.toolbar.right_action_items = [
            ['comment-question-outline', lambda x: self.show_confirmation_dialog()],
            ['format-paint', lambda x: self.color_change()]]
        screen.add_widget(self.toolbar)

        # ввод пользователя
        self.input = MDTextField(
            hint_text='Введите название индикатора',
            halign='left',
            size_hint=(0.8, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            font_size=22)
        screen.add_widget(self.input)

        # вывод информации пользователю

        self.label2 = MDLabel(
            halign='left',
            size_hint=(0.8, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.45},
            theme_text_color='Secondary'
            )
        self.label = MDLabel(
            halign='left',
            size_hint=(0.8, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.45},
            theme_text_color='Secondary'
            )
        self.answer = MDLabel(
            halign='left',
            size_hint=(0.8, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.35},
            theme_text_color='Primary',
            font_size=12
            )

        screen.add_widget(self.label2)
        screen.add_widget(self.label)
        screen.add_widget(self.answer)

        # поисковая кнопка
        screen.add_widget(MDFillRoundFlatButton(
            text='     ПОИСК     ',
            font_size=22,
            pos_hint={'center_x': 0.5, 'center_y': 0.15},
            on_press=self.tx,
            on_release=self.change_text))

        # логотип
        screen.add_widget(Image(source='ph_1.webp',
                                pos_hint={'center_x': 0.5, 'center_y': 0.76},
                                size_hint_x=None, width=130))

        return screen


if __name__ == '__main__':
    FinancialIndicatorsLiteApp().run()
