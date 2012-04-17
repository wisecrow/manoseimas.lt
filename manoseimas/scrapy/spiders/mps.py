from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule
from scrapy.selector import HtmlXPathSelector

from manoseimas.scrapy.items import Person
from manoseimas.scrapy.loaders import Loader
from manoseimas.scrapy.spiders import ManoSeimasSpider


class MpsSpider(ManoSeimasSpider):
    name = 'mps'
    allowed_domains = ['lrs.lt']

    start_urls = [
        'http://www3.lrs.lt/pls/inter/w5_show?p_r=6113&p_k=1',
    ]

    rules = (
        Rule(SgmlLinkExtractor(allow=['p_asm_id=\d+']), 'parse_person'),
    )

    def _parse_person_details(self, response):
        xpath = '//table[@summary="Kadencijos"]'
        hxs = HtmlXPathSelector(response).select(xpath)[0]

        source = self._get_source(response.url, 'p_asm_id')
        _id = source['id']

        person = Loader(self, response, Person(), hxs, required=('name',))
        person.add_value('_id', '%sp' % _id)
        person.add_xpath('name', 'tr/td[2]/div/b/font[2]/text()')
        person.add_xpath('email', 'tr[2]/td[2]/b[6]/a/text()')
        person.add_xpath('phone', 'tr[2]/td[2]/b[4]/text()')
        person.add_xpath('home_page', 'tr[2]/td[2]/a[1]/@href')
        person.add_value('source', source)
        return person.load_item()

    def parse_person(self, response):
        yield self._parse_person_details(response)
