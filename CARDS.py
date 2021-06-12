from BLUECARDS import WheatField, Farm, Cornfield, FlowerGarden, Vineyard, Reserve, Mine, FishingBoat, Trawler, \
    AppleOrchard
from GRINCARDS import DepartmentStore, Bakery, Supermarket, CreditBureaus, DemolitionCompany, FlowerShop, CheeseDiary, \
    FurnitureFactory, WineFactory, TransportCompany, BeverageFactory, VegetableMarket, GroceryWarehouse
from REDCARDS import SushiBar, Cafe, Restaurant, Pizzeria, BurgerJoint, Eatery, LuxuryBar
from VIOLETCARDS import Stadium, Telecentre, BusinessCenter, Publishing, BuildingRepairCompany, TaxService, VentureFund, \
    ConcertCenter, Park
from Card import CARD_TYPE

CARDS = {
    'B1': WheatField(name="Пшеничное поле", cost=1, roll=[1], type=CARD_TYPE.get('Синяя')),
    'B2': Farm(name="Ферма", cost=1, roll=[2], type=CARD_TYPE.get('Синяя')),
    'B3': Cornfield(name='Кукурузное поле', cost=2, roll=[3, 4], type=CARD_TYPE.get('Синяя')),
    'B4': FlowerGarden(name='Цветник', cost=2, roll=[4], type=CARD_TYPE.get('Синяя')),
    'B5': Vineyard(name='Виноградник', cost=3, roll=[7], type=CARD_TYPE.get('Синяя')),
    'B6': Reserve(name='Заповедник', cost=3, roll=[5], type=CARD_TYPE.get('Синяя')),
    'B7': Mine(name='Рудник', cost=6, roll=[9], type=CARD_TYPE.get('Синяя')),
    'B8': FishingBoat(name='Рыбацкий баркас', cost=2, roll=[8], type=CARD_TYPE.get('Синяя')),
    'B9': Trawler(name='Траулер', cost=5, roll=[12, 13, 14], type=CARD_TYPE.get('Синяя')),
    'B10': AppleOrchard(name='Яблоневый сад', cost=3, roll=[10], type=CARD_TYPE.get('Синяя')),

    'G1': DepartmentStore(name="Универмаг", cost=1, roll=[2], type=CARD_TYPE.get('Зеленая')),
    'G2': Bakery(name="Пекарня", cost=1, roll=[2], type=CARD_TYPE.get('Зеленая')),
    'G3': Supermarket(name="Супермаркет", cost=2, roll=[4], type=CARD_TYPE.get('Зеленая')),
    'G5': CreditBureaus(name="Кредитное бюро", cost=0, roll=[5, 6], type=CARD_TYPE.get('Зеленая')),
    'G4': DemolitionCompany(name="Компания по сносу зданий", cost=2, roll=[4],
                            type=CARD_TYPE.get('Зеленая')),
    'G6': FlowerShop(name="Цветочный магазин", cost=1, roll=[6], type=CARD_TYPE.get('Зеленая')),
    'G7': CheeseDiary(name="Сыроварня", cost=5, roll=[7], type=CARD_TYPE.get('Зеленая')),
    'G8': FurnitureFactory(name="Мебельная фабрика", cost=3, roll=[8], type=CARD_TYPE.get('Зеленая')),
    'G9': WineFactory(name="Винный завод", cost=2, roll=[9], type=CARD_TYPE.get('Зеленая')),
    'G10': TransportCompany(name="Транспортная компания", cost=2, roll=[9, 10],
                            type=CARD_TYPE.get('Зеленая')),
    'G11': BeverageFactory(name="Фабрика напитков", cost=5, roll=[11], type=CARD_TYPE.get('Зеленая')),
    'G12': VegetableMarket(name="Овощной рынок", cost=2, roll=[11, 12], type=CARD_TYPE.get('Зеленая')),
    'G13': GroceryWarehouse(name="Продуктовый склад", cost=2, roll=[12, 13],
                            type=CARD_TYPE.get('Зеленая')),

    'R1': SushiBar(name="Суши бар", cost=4, roll=[1], type=CARD_TYPE.get('Красная')),
    'R2': Cafe(name="Кафе", cost=2, roll=[3], type=CARD_TYPE.get('Красная')),
    'R3': Restaurant(name="Ресторан", cost=3, roll=[5], type=CARD_TYPE.get('Красная')),
    'R4': Pizzeria(name="Пиццерия", cost=1, roll=[7], type=CARD_TYPE.get('Красная')),
    'R5': BurgerJoint(name="Бургерная", cost=1, roll=[8], type=CARD_TYPE.get('Красная')),
    'R6': Eatery(name="Закусочная", cost=3, roll=[9, 10], type=CARD_TYPE.get('Красная')),
    'R7': LuxuryBar(name="Элитный бар", cost=4, roll=[12, 13, 14], type=CARD_TYPE.get('Красная')),

    'V1': Stadium(name="Стадион", cost=6, roll=[6], type=CARD_TYPE.get('Фиолетовая')),
    'V2': Telecentre(name="Телецентр", cost=7, roll=[6], type=CARD_TYPE.get('Фиолетовая')),
    'V3': BusinessCenter(name="Бизнес цетр", cost=8, roll=[6], type=CARD_TYPE.get('Фиолетовая')),
    'V4': Publishing(name="Издательство", cost=5, roll=[7], type=CARD_TYPE.get('Фиолетовая')),
    'V5': BuildingRepairCompany(name="Компания по ремонту зданий", cost=4, roll=[8],
                                type=CARD_TYPE.get('Фиолетовая')),
    'V6': TaxService(name="Налоговая", cost=4, roll=[8, 9], type=CARD_TYPE.get('Фиолетовая')),
    'V7': VentureFund(name="Венчурный фонд", cost=1, roll=[10], type=CARD_TYPE.get('Фиолетовая')),
    'V8': ConcertCenter(name="Концерт центр", cost=7, roll=[10], type=CARD_TYPE.get('Фиолетовая')),
    'V9': Park(name="Парк", cost=3, roll=[11, 12, 13], type=CARD_TYPE.get('Фиолетовая'))
}
