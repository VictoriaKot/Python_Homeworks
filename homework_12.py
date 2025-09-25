import requests
from lxml import html
"""
Написати 50 XPath локаторів для обраного сайту 
"""
def get_html_content(url:str) -> str:
    response = requests.get(url)
    return response.text

def get_tree(html_text:str):
    if response.status_code == 200:
         return html.fromstring(html_text)
    
def find_by(tree, locator, by_text=True):
    if by_text:
        return tree.findtext(locator)
    else:
        return tree.xpath(locator)
    
if __name__ == "__main__":
    url1 = f"https://tekstura.ua/"
    response = requests.get(url1)
    content1 = get_html_content(url1)
    tree = get_tree(content1)
    """Main menu"""
    
    logo = find_by(tree, '//div[@class="tmenu-mobile__burgerlogo"]//img[@class="tmenu-mobile__imglogo"]', False)
    print("Логотип сторінки:", logo)
    main_menu_button = find_by(tree, '//div[@class="tmenu-mobile__container"]//button[@type="button"]', False)
    print("Кнопка меню", main_menu_button)
    button_to_catalogue1 = find_by(tree, '//*[@id="carousel_286511632"]//a[@tabindex="0"]//span[@class ="t-btnflex__text"]', False)
    kids_furniture_menu = find_by(tree, '//div[@field="li_title__1753369041254"]//span[text() ="Дитячі меблі"]', False)
    tables_chairs_menu = find_by(tree, '//div[@field="li_title__9042308404731"]//span[text() ="Столи та стільці"]', False)
    bedroom_furniture_menu = find_by(tree, '//div[@field="li_title__9042308404732"]//span[text() ="Меблі в спальню"]', False)
    mattress_menu = find_by(tree, '//div[@field="li_title__9042308404730" ]', False)
    print("Матраци меню", mattress_menu)
    textile_menu = find_by(tree, '//div[@field="li_title__9042308404733" ]', False)
    soft_furniture_menu = find_by(tree, '//div[@field="li_title__1753368724093" ]', False)
    
    """Footer of the main page"""
    oplata_button = find_by(tree, '//a[@href="https://tekstura.ua/oplata" ]', False)
    feedback_button = find_by(tree, '//a[@href="https://tekstura.ua/feedbackpage" ]', False)
    made_in_Ukr_button = find_by(tree, '//a[@href="https://tekstura.ua/vyrobleno-v-ukrayini"]', False)
    recommendations_button = find_by(tree, '//a[@href="https://tekstura.ua/rekomendatsiyi-z-dohlyadu" ]', False)
    garant_buton = find_by(tree, '//a[@href="https://tekstura.ua/garant" ]', False)
    dogovir_button = find_by(tree, '//a[@href="https://tekstura.ua/dogovir" ]', False)
    materials_button = find_by(tree, '//a[@href="https://tekstura.ua/material" ]', False)
    kids_furniture_link_button = find_by(tree, '//a[@href="https://tekstura.ua/dytiachi-mebli" ]', False)
    tables_chairs_link_button = find_by(tree, '//a[@href="https://tekstura.ua/stoly-ta-stiltsi" ]', False)
    bedroom_link_button = find_by(tree, '//a[@href="https://tekstura.ua/spalnia/" ]', False)
    mattress_link_button = find_by(tree, '//a[@href="https://tekstura.ua/matratsy" ]', False)
    soft_furn_link_button= find_by(tree, '//a[@href="https://tekstura.ua/soft-furniture" ]', False)
    kids_wooden_beds_menu = find_by(tree, '//div[@field="li_title__5811835606960" ]', False)
    
    """Kids furniture submenu"""
    url2 = f"https://tekstura.ua/matratsy/kids"
    response = requests.get(url2)
    content2 = get_html_content(url2)
    tree2 = get_tree(content2)
   
    filter_button = find_by(tree2, '//*[@class = "js-store-filter-mob-btn t-store__filter__opts-mob-btn t-name t-name_xs"]', False)
    sorting_default_checkbox = find_by(tree2, 'div[@class="t-store__filter__item-controls-wrap js-store-filter-item-controls-wr"]//*[contains(text(),"Сортування: за замовчуванням")]',False)
    print("sorting_default_checkbox: ", sorting_default_checkbox)
    search_button = find_by(tree2, '//*[@class="t-store__filter__search-mob-btn-icon"]', False)
    print("search:", search_button)
    matress_picture = find_by(tree2, '//div[@data-original="https://static.tildacdn.one/stor3537-3732-4839-b737-663164653637/79189610.jpg"]', False)
    print("matress", matress_picture)
    coconut_kid_matress = find_by(tree2, '//div[text()="Матрац дитячий Tekstura Soft Latex"]', False)
    air_eco_matress_picture_link = find_by(tree2, '//div[@data-original="https://static.tildacdn.one/stor3230-6637-4135-a636-653333313034/69787194.jpg"]', False)
    air_eco_matress_button = find_by(tree2, '//div[text()="Матрац Air Eco latex"]', False)
    search_input_filed = find_by(tree2, '//input[@type="text" and @placeholder="Пошук товарів"]', False)
    search_button_in_input= find_by(tree2, '//*[@class="t-store__search-icon js-store-filter-search-btn"]', False)
    