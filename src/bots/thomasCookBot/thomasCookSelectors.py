from src.common.selectors import selectors
from src.common.selectorType import selectorType

rowSelector = selectors()\
    .withSelector('//div[@class="divTableRow clearfix"]')\
    .withType(selectorType.XPATH)


currencySelector = selectors()\
    .withType(selectorType.XPATH)\
    .withSelector('.//div[@class="divTableCell tabhead "]')


currencyValueSelector = selectors()\
    .withSelector('(.//span[@class="mls"])[2]')\
    .withType(selectorType.XPATH)
