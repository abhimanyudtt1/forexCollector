from src.common.selectors import selectors
from src.common.selectorType import selectorType

rowSelector = selectors()\
    .withSelector('//div[@class="table-responsive"]//tr')\
    .withType(selectorType.XPATH)


currencySelector = selectors()\
    .withType(selectorType.XPATH)\
    .withSelector('.//td[1]')


currencyValueSelector = selectors()\
    .withSelector('.//td[2]')\
    .withType(selectorType.XPATH)
