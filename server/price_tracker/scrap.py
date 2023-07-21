import lxml
import requests
from bs4 import BeautifulSoup

# url = "https://www.amazon.in/dp/B09XJ36Q27/ref=QAHzEditorial_en_IN_3?pf_rd_r=QHH4N6QY395QBP6TYP1D&pf_rd_p=945d7aac-5ce9-446c-8eea-f66746c906c7&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-7&pf_rd_t=&pf_rd_i=1389401031&ie=UTF8&ref_=CLP_MH8_BSAffordable_3"
# url = "https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5W4NNB/ref=lp_10559548031_1_1?sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D"
# url = "https://www.amazon.in/Sparx-Casual-Stripped-Sneakers-White/dp/B0B4KF6LFM/ref=zg_bs_shoes_sccl_1/260-4460794-8698619?th=1&psc=1"

# url = "https://www.flipkart.com/oraimo-20000-mah-power-bank-12-w-fast-charging/p/itm95749acddaf53?pid=PWBGFD65F9RQJC2B&lid=LSTPWBGFD65F9RQJC2BJZMMXY&marketplace=FLIPKART&store=tyy%2F4mr%2Ffu6&spotlightTagId=BestsellerId_tyy%2F4mr%2Ffu6&srno=b_1_2&otracker=hp_omu_Best%2Bof%2BElectronics_2_3.dealCard.OMU_UDG9W07DN4PD_3&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_2_NA_view-all_3&fm=neo%2Fmerchandising&iid=502956da-93c7-4455-9102-5cc9f745f973.PWBGFD65F9RQJC2B.SEARCH&ppt=browse&ppn=browse&ssid=xiqg4wmkn40000001682756922261"
# url = "https://www.flipkart.com/realme-80-cm-32-inch-hd-ready-led-smart-android-tv/p/itm56d1cf16da75b?pid=TVSFRTJQTZVKTF6Y&lid=LSTTVSFRTJQTZVKTF6YHMHXRW&marketplace=FLIPKART&store=ckf%2Fczl&spotlightTagId=FkPickId_ckf%2Fczl&srno=b_1_1&otracker=nmenu_sub_TVs%20%26%20Appliances_0_realme&fm=neo%2Fmerchandising&iid=f1448e91-3bcd-4ff4-b52d-3ca892e9b35f.TVSFRTJQTZVKTF6Y.SEARCH&ppt=browse&ppn=browse&ssid=qx0axx8nzk0000001682757260058"
# url = "https://www.flipkart.com/samsung-galaxy-a14-5g-light-green-128-gb/p/itmabe91abe7ba0c?pid=MOBGHT8UU3STRKZS&marketplace=FLIPKART"


def get_link_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Accept-Language": "en",
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    if url.startswith("https://www.amazon.in/"):
        name = soup.select_one(selector="#productTitle").getText()
        name = name.strip()

        price = soup.select_one(selector=".a-price-whole").getText()
        price = int(price.replace(",", "").replace(".", ""))

        image_tag = soup.select_one(selector="#landingImage")
        image_url = image_tag["src"]

    elif url.startswith("https://www.flipkart.com/"):
        name = soup.select_one(selector=".B_NuCI").getText()
        name = name.strip()

        price = soup.select_one(selector="._30jeq3").getText()
        price = int(price[1:].replace(",", ""))

        image_tag = soup.select_one(selector="._396cs4._2amPTt._3qGmMb")
        image_url = image_tag["src"]

    else:
        return None

    return {"name": name, "price": price, "image_url": image_url}
