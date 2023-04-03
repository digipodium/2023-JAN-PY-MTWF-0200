from dputils.scrape import Scraper, Tag
import pandas as pd

class MyScraper:
    def __init__(self, query, page=1):
        self.query = query
        self.page = page
        self.url = f'https://www.flipkart.com/search?q={query}&page={page}'
        self.dataset = []

    def collect(self):
        print(f'Collecting page {self.page}...')
        sc = Scraper(self.url)
        target = Tag(cls='_1YokD2 _3Mn1Gg')
        items = Tag(cls='_1AtVbE col-12-12')
        title = Tag(cls='_4rR01T')
        price = Tag(cls='_30jeq3 _1_WHN1')
        rating = Tag('span', cls='_2_R_DZ')
        out = sc.get_all(target, items, name=title, price=price, rr=rating)
        return out
    
    def collect_all(self):
        while True:
            result = self.collect()
            if len(result) >= 1:
                self.dataset.extend(result)
                self.page += 1
                self.url = f'https://www.flipkart.com/search?q={self.query}&page={self.page}'
                print(self.url)
            else:
                break
    def save(self, filename):
        df = pd.DataFrame(self.dataset)
        df.dropna(how='all', inplace=True)
        df.to_csv(filename, index=False)


if __name__ == '__main__':
    # create object
    sc = MyScraper('laptops')
    # collect data
    sc.collect_all()
    # save data
    sc.save('laptops.csv')
    