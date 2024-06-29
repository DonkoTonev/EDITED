import scrapy
import json


class MarksAndSpencerSpider(scrapy.Spider):
    name = "marksandspencer"
    allowed_domains = ["marksandspencer.com"]
    start_urls = ["https://www.marksandspencer.com"]
    custom_settings = {
        "REQUEST_FINGERPRINTER_IMPLEMENTATION": "2.7"
    }

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Cookie": "GlobalE_Data=%7B%22countryISO%22%3A%22BG%22%2C%22cultureCode%22%3A%22en-GB%22%2C%22currencyCode%22%3A%22BGN%22%2C%22apiVersion%22%3A%222.1.4%22%7D; dwanonymous_1cb58b269223fbc31a670f29b400d0c0=cfmaI5hBkdxCMfl2b0DDYOEUPc; MS_PREFERRED_COUNTRY=en_BG; MS_ORIGIN_COUNTRY=BG; cleared-onetrust-cookies-flagship=cleared; CONSENTMGR=consent:true%7Cts:1719223938047; BVBRANDID=e57345c4-5a4e-40f1-8b69-2f0c2531d890; OptanonAlertBoxClosed=2024-06-24T10:12:20.274Z; PIM-SESSION-ID=NJo94E3p3OB1UEYx; __cq_dnt=1; dw_dnt=1; akacd_PIM-prd_ah_rollout=3896869351~rv=73~id=6789a7d9281d1480471b597a065d406b; BVImplmain_site=17573; GlobalE_Full_Redirect=false; akacd_PRODHOME=2147483647~rv=42~id=1592a3680917fa3b33978cf734ce81dd; 95-5-cheq-split=cheq_95_test; _cq_duid=1.1719479773.OltW7M8i55XA89nK; _cq_suid=1.1719479773.gIAg56IyTZNLMEfj; experimentsUserId=1719479774288181746; MS-SESSION-ID=928f0d81-3bc7-44d3-ac99-1dfdd605d7be; __Host-next-auth.csrf-token=5ab312adbfbc7a194dc27010e3dd198894b682a9e5c98d687a91d43772228c17%7Cec4136de6110d7899ff951636a3dea3837ee6613f0d3901e361d676289cdd241; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.marksandspencer.com; akacd_prdauth=2147483647~rv=85~id=a84c9fec72d0b761c1f7b440765ba182; akacd_PRODPLP=2147483647~rv=49~id=a595eea9f9b4926b518aee6ab516fe6b; akacd_PRODINTLPLP=2147483647~rv=3~id=d55675fe5cf306fce44ff740ba52dfbb; akavpau_PROD_PLP_VP=1719480568~id=323503bd058e1ce9b04e882bb9ed86af; sid=dwCSMRrhoDRXG0FDBjSQyeTAfNXYy7wjlT0; dwsid=bGiA_qsps7biH6Ugxyiomf-obhppA6-hIDkBDs5NFEytQCQ3S43KxvFiDoVqo9y1soEjomVkcuUEXnbwmdYkDw==; _abck=87A21A96A09FB3D6E3D1AECBC37F496A~0~YAAQRC0UArxA2FWQAQAAgDFeXQw2pREbIeMAI7dOVbK8DaJiVxo5JPQBUmZekPOY/YvUq+j7bNkA0UOKzxDfsfRjayeEXDBSm0/gbuA5hZ1lLLUoenr0KhPAv9hzme1vl8A4UuzFiZp9Z8YledJgO6sG1cKePZTSsYtJLoPkMEnzOe4oiTrCmB9ER3mqXzVUSkSRK+CL7pGdpmHPIC1e7dsqrZwUfmU9VLP8RKFgVWYqedud4NdUID7B4MKebkUy6rPjuOykZWKW3z41AyO8/WtxY5PUaLmSRUwKHnV/exkkGAUKeQaMFjezFe2Qg+ZHyqWJOEHlbj+PZUPUfkmSbQwGktnLu1gYmrsKX5FmceqQWleJLdqgDoMJtNxp8QPsIE3nccQnGyRAY4eVbwuBax/0AcoPWQ+yEMyy32esiVZO~-1~-1~-1; bm_sz=D0A0B656BF76FD3FFD8ABC6F23C43678~YAAQRC0UAten2VWQAQAAQfqiXRjtcpWnSs8hJsBw2uM27txNdMOQ5Ncf8ENTXIb57kSK3pgo/vBFgP6rYLu77w7R/VVQIOTJesrEwxQkcVErK0n5bBzzluU0HLadE6ba1kT82Jq5ssqHszDe79DzcZ6rji8TSFRkivbD2u0BS/BtE3qZ07360dcRaJkMcQ3CCjCgTwkf5bx5XZjGqk5BbKpO0jFAZ03xJDkuSqYujk0UjzS4O4QGmyM03zoFfIwYdIZQCuErsL5MPYiBxmsg3VHFle4+LyIv78vzk9X8JPtvsUMWwdshIgpgQblzw6DwXPkyXQEh+oSapdCLZIoSo3hwayZ+oChHRf5zNumQ+AWB4GGlsEtqdAboLZwf9u91yKFsWjohK4oBeiqOXGaBbWgbBkvST50E9NMwhwlrtlRMCe/9akYSc1s2O31cGtfH~4339257~3686982; ak_bmsc=2FEA4E8ED5EA6F2222C0F047E5C18E6E~000000000000000000000000000000~YAAQRC0UAk+z2lWQAQAASF/QXRiFwJ5B7R30Sey+Nlk3TsfYDVKZ09837iBL9CAaNKuTedVI4+QC3XHbxXJOddobnJthjgYAArO4y4O5Qds+LeXuYSJpGgP/xQNlcBFYPqrN/PMy1kIRejmR5tRo2lU6iNV1R+h9IsIDlNLidAIb7AEoFsxxxxC7Z4iMK3VyRpZoPsP1Wi6gc8BkDHhF7D1OPHSwcvSiFb/Dx7QgnK3+Antgb9E5AcgnWNq8780z219B/SCNq2EddNG1r9Sft9CFhOkucO6PHf7eS4ubSzxfAsMYZuL6PbQNbDfx9n1efyrid12DhGXeL1Nvzau5SqG9YPQcIa8pTh0BOE5tzPWHQTACJweRCttH8Pk52W2HBw3Tzx7DLi3y2oNAjW9ofC8=; lux_uid=171956087488779533; BVBRANDSID=1a72667f-4f2c-40a7-a9e5-bc24c4bde492; akavpau_www=1719561614~id=3ecdd4910bbc1b0ac7350f6219bed74b; GlobalE_CT_Data=%7B%22CUID%22%3A%7B%22id%22%3A%22826640077.450503824.91%22%2C%22expirationDate%22%3A%22Fri%2C%2028%20Jun%202024%2008%3A20%3A15%20GMT%22%7D%2C%22CHKCUID%22%3Anull%2C%22GA4SID%22%3A822741858%2C%22GA4TS%22%3A1719561015323%2C%22Domain%22%3A%22www.marksandspencer.com%22%7D; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Jun+28+2024+10%3A50%3A15+GMT%2B0300+(Eastern+European+Summer+Time)&version=202308.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=100802a3-c593-458f-821c-e65bdd24bdc0&interactionCount=1&landingPath=NotLandingPage&groups=C0002%3A0%2CC0004%3A0%2CC0001%3A1%2CC0005%3A0%2CC0003%3A0&geolocation=BG%3B&AwaitingReconsent=false; utag_main=v_id:019049bb6bf80020ffd87b667c980506f005306700978$_sn:11$_se:24$_ss:0$_st:1719562820095$ses_id:1719560875254%3Bexp-session$_pn:4%3Bexp-session; akavpau_INTL_PROD_WAITING=1719562138~id=6f48e9d8fecf0029050d290d016c9620; bm_sv=152D2A99F10E5844383E94EF5F882F0D~YAAQRC0UAjb42lWQAQAAl8zaXRgeZKV1LNzlB3fT5DA9fYR1gW7I3+nkJTeGiO6QoiOxpiuh+MdR5foXJxZUiG5hwwf3TDJ3AknT0VBmFP6aof4Y7g/lS6C1aCXQaS0qH2PQnv2NJbjH5od3NnI2V/lRKrTQxfQwaBjtZmz2x1PmL7wYtJQ4Z9hsEmFjl46/HtL+3FYEXf4RXAw+50vj4IhqBVwF4r72tTFRrX7zMZ61GIJ0zNkgXDV7VsKy2QeLtNaQcANpFZ9IaQ==~1",
        "Priority": "u=1, i",
        "Referer": "https://www.marksandspencer.com/bg/easy-iron-geometric-print-shirt/p/P60639302.html",
        "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "Windows",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    def parse(self, response): 
        option = response.css('#country-selector-country option[value="BG"]')

        if option:
            value = option.css('::attr(value)').get().lower()
            bg_version_url = f"{response.url}/{value}/"
            self.logger.info(f"BG URL found: {bg_version_url}")
            yield response.follow(bg_version_url, callback=self.parse_bg_version_url)
        else:
            self.logger.warning("BG option not found on the homepage.")

    def parse_bg_version_url(self, response):
        men_page_link = response.css(
            '.nav-item.dropdown.order-lg-3 .subcategory a::attr(href)').get()
        if men_page_link:
            self.logger.info(f"Men's link found: {men_page_link}")
            yield response.follow(men_page_link, callback=self.parse_mens_page)
        else:
            self.logger.warning("Men's section link not found on the BG page.")

    def parse_mens_page(self, response):
        casual_shirts_link = response.xpath(
            '//a[contains(text(), "Casual shirts")]/@href').get()
        if casual_shirts_link:
            self.logger.info(f"Casual shirts link found: {casual_shirts_link}")
            yield response.follow(casual_shirts_link, callback=self.parse_casual_shirts)
        else:
            self.logger.warning("Casual shirts link not found on the Men's page.")

    def parse_casual_shirts(self, response):
        product_link = response.css(
            'div.pdp-link a:contains("Easy Iron Geometric Print Shirt")::attr(href)').get()
        if product_link:
            self.logger.info(f"Product link found: {product_link}")
            yield response.follow(product_link, callback=self.parse_product_page)
        else:
            self.logger.warning(
                "Product link not found in the Casual Shirts section."
            )

    def parse_product_page(self, response):
        product_name = response.css('.product-name::text').get()
        price = response.css('.value::attr(content)').get()
        size = response.css('#plp-select').get()

        if price:
            try:
                price = float(price)
            except ValueError:
                price = None
        else:
            price = None

        sizes = []
        if size:
            select_element = scrapy.Selector(text=size, type="html")
            option_tags = select_element.css('option')
            for option in option_tags:
                option_text = option.xpath('normalize-space(text())').get()
                if option_text != "Select Size":
                    cleaned_size = option_text.split(" Out of Stock")[0].split(" Low in Stock")[0]
                    sizes.append(cleaned_size)

        product_data = {
            "name": str(product_name) or '',
            "price": float(price) or '',
            "color": str(''),
            "size": list(sizes),
            "reviews_count": int(0),
            "reviews_score": float(0.0),
        }

        color_api_url = 'https://www.marksandspencer.com/on/demandware.store/Sites-mandslondon-Site/en_BG/Product-Variation?pid=P60639302&isCompleteTheLookABTest=false'
        reviews_api_url = 'https://www.marksandspencer.com/on/demandware.store/Sites-mandslondon-Site/en_BG/BazaarVoiceReviews-ReviewSummary?pid=P60639302&locale=en_BG&offset=0'

        yield scrapy.Request(
            color_api_url,
            callback=self.parse_api_color,
            cb_kwargs={'product_data': product_data, 'reviews_api_url': reviews_api_url},
            dont_filter=True,
            headers=self.headers
        )

    def parse_api_color(self, response, **cb_kwargs):
        product_data = cb_kwargs['product_data']
        reviews_api_url = cb_kwargs['reviews_api_url']

        raw_data = response.body
        data = json.loads(raw_data)

        default_color = data.get('product', {}).get('defaultColor', 'N/A')
        product_data['color'] = default_color

        yield scrapy.Request(
            url=reviews_api_url,
            callback=self.parse_api_reviews,
            cb_kwargs={'product_data': product_data},
            dont_filter=True
        )

    def parse_api_reviews(self, response, **cb_kwargs):
        product_data = cb_kwargs['product_data']

        raw_data = response.body
        data = json.loads(raw_data)

        reviews_html = data.get('bvDetailReviewsHTML', '')
        reviews_selector = scrapy.Selector(text=reviews_html)

        average_rating = reviews_selector.css('span.review-summary__rating::text').get()
        if average_rating:
            try:
                average_rating = float(average_rating)
            except ValueError:
                average_rating = 0.0
        else:
            average_rating = 0.0

        review_count_text = reviews_selector.css('span.review-summary__total-review::text').get()
        review_count = review_count_text.split()[2] if review_count_text else '0'
        if review_count:
            try:
                review_count = int(review_count)
            except ValueError:
                review_count = 0
        else:
            review_count = 0

        product_data['reviews_score'] = average_rating
        product_data['reviews_count'] = review_count

        yield product_data
