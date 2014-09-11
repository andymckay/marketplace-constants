# List of valid country codes: http://en.wikipedia.org/wiki/ISO_3166-1_alpha-3
COUNTRIES = [
    'AFG', 'ALA', 'ALB', 'DZA', 'ASM', 'AND', 'AGO', 'AIA', 'ATA', 'ATG',
    'ARG', 'ARM', 'ABW', 'AUS', 'AUT', 'AZE', 'BHS', 'BHR', 'BGD', 'BRB',
    'BLR', 'BEL', 'BLZ', 'BEN', 'BMU', 'BTN', 'BOL', 'BES', 'BIH', 'BWA',
    'BVT', 'BRA', 'IOT', 'BRN', 'BGR', 'BFA', 'BDI', 'KHM', 'CMR', 'CAN',
    'CPV', 'CYM', 'CAF', 'TCD', 'CHL', 'CHN', 'CXR', 'CCK', 'COL', 'COM',
    'COG', 'COD', 'COK', 'CRI', 'CIV', 'HRV', 'CUB', 'CUW', 'CYP', 'CZE',
    'DNK', 'DJI', 'DMA', 'DOM', 'ECU', 'EGY', 'SLV', 'GNQ', 'ERI', 'EST',
    'ETH', 'FLK', 'FRO', 'FJI', 'FIN', 'FRA', 'GUF', 'PYF', 'ATF', 'GAB',
    'GMB', 'GEO', 'DEU', 'GHA', 'GIB', 'GRC', 'GRL', 'GRD', 'GLP', 'GUM',
    'GTM', 'GGY', 'GIN', 'GNB', 'GUY', 'HTI', 'HMD', 'VAT', 'HND', 'HKG',
    'HUN', 'ISL', 'IND', 'IDN', 'IRQ', 'IRL', 'IMN', 'ISR', 'ITA',  # IRN
    'JAM', 'JPN', 'JEY', 'JOR', 'KAZ', 'KEN', 'KIR', 'KOR', 'KOS',  # PRK
    'KWT', 'KGZ', 'LAO', 'LVA', 'LBN', 'LSO', 'LBR', 'LBY', 'LIE', 'LTU',
    'LUX', 'MAC', 'MKD', 'MDG', 'MWI', 'MYS', 'MDV', 'MLI', 'MLT', 'MHL',
    'MTQ', 'MRT', 'MUS', 'MYT', 'MEX', 'FSM', 'MDA', 'MCO', 'MNG', 'MNE',
    'MSR', 'MAR', 'MOZ', 'MMR', 'NAM', 'NRU', 'NPL', 'NLD', 'NCL', 'NZL',
    'NIC', 'NER', 'NGA', 'NIU', 'NFK', 'MNP', 'NOR', 'OMN', 'PAK', 'PLW',
    'PSE', 'PAN', 'PNG', 'PRY', 'PER', 'PHL', 'PCN', 'POL', 'PRT', 'PRI',
    'QAT', 'REU', 'ROU', 'RUS', 'RWA', 'BLM', 'SHN', 'KNA', 'LCA', 'MAF',
    'SPM', 'VCT', 'WSM', 'SMR', 'STP', 'SAU', 'SEN', 'SRB', 'SCG', 'SYC',
    'SLE', 'SGP', 'SXM', 'SVK', 'SVN', 'SLB', 'SOM', 'ZAF', 'SGS', 'SSD',
    'ESP', 'LKA', 'SDN', 'SUR', 'SJM', 'SWZ', 'SWE', 'CHE', 'SYR', 'TWN',
    'TJK', 'TZA', 'THA', 'TLS', 'TGO', 'TKL', 'TON', 'TTO', 'TUN', 'TUR',
    'TKM', 'TCA', 'TUV', 'UGA', 'UKR', 'ARE', 'GBR', 'USA', 'UMI', 'URY',
    'UZB', 'VUT', 'VEN', 'VNM', 'VGB', 'VIR', 'WLF', 'ESH', 'YEM', 'ZMB',
    'ZWE',
]

COUNTRY_DETAILS = {
    'ARG': {
        'adolescent': True,
        'default_currency': 'ARS',
        'default_language': 'es',
        'id': 20,
        'legacy': 'AR',
        'mcc': 722,
        'ratingsbody': 'ESRB',
        'slug': 'ar',
        'special': False,
        'weight': 0
    },
    'BGD': {
        'adolescent': True,
        'default_currency': 'BDT',
        'default_language': 'en',
        'id': 31,
        'legacy': 'BD',
        'mcc': 470,
        'slug': 'bd',
        'special': False,
        'weight': 0
    },
    'BRA': {
        'adolescent': False,
        'default_currency': 'BRL',
        'default_language': 'pt-BR',
        'id': 7,
        'legacy': 'BR',
        'mcc': 724,
        'ratingsbody': 'CLASSIND',
        'slug': 'br',
        'special': False,
        'weight': 0
    },
    'CHL': {
        'adolescent': True,
        'default_currency': 'CLP',
        'default_language': 'es',
        'id': 23,
        'legacy': 'CL',
        'mcc': 730,
        'ratingsbody': 'ESRB',
        'slug': 'cl',
        'special': False,
        'weight': 0
    },
    'CHN': {
        'adolescent': True,
        'default_currency': 'RMB',
        'default_language': 'zh-CN',
        'id': 21,
        'legacy': 'CN',
        'mcc': 460,
        'slug': 'cn',
        'special': True,
        'weight': 0
    },
    'COL': {
        'adolescent': False,
        'default_currency': 'COP',
        'default_language': 'es',
        'id': 9,
        'legacy': 'CO',
        'mcc': 732,
        'ratingsbody': 'ESRB',
        'slug': 'co',
        'special': False,
        'weight': 0
    },
    'CRI': {
        'adolescent': True,
        'default_currency': 'CRC',
        'default_language': 'es',
        'id': 27,
        'legacy': 'CR',
        'mcc': 712,
        'ratingsbody': 'ESRB',
        'slug': 'cr',
        'special': False,
        'weight': 0
    },
    'CZE': {
        'adolescent': True,
        'default_currency': 'CZK',
        'default_language': 'cs',
        'id': 34,
        'legacy': 'CZ',
        'mcc': 230,
        'slug': 'cz',
        'special': False,
        'weight': 0
    },
    'DEU': {
        'adolescent': True,
        'default_currency': 'EUR',
        'default_language': 'de',
        'id': 14,
        'legacy': 'DE',
        'mcc': 262,
        'ratingsbody': 'USK',
        'slug': 'de',
        'special': False,
        'weight': 0
    },
    'ECU': {
        'adolescent': True,
        'default_currency': 'USD',
        'default_language': 'es',
        'id': 26,
        'legacy': 'EC',
        'mcc': 740,
        'ratingsbody': 'ESRB',
        'slug': 'ec',
        'special': False,
        'weight': 0
    },
    'ESP': {
        'adolescent': True,
        'default_currency': 'EUR',
        'default_language': 'es',
        'id': 8,
        'legacy': 'SPAIN',
        'mcc': 214,
        'ratingsbody': 'PEGI',
        'slug': 'es',
        'special': False,
        'weight': 0
    },
    'FRA': {
        'adolescent': True,
        'default_currency': 'EUR',
        'default_language': 'fr',
        'id': 30,
        'legacy': 'FR',
        'mcc': 208,
        'ratingsbody': 'PEGI',
        'slug': 'fr',
        'special': False,
        'weight': 0
    },
    'GBR': {
        'adolescent': True,
        'default_currency': 'GBP',
        'default_language': 'en-US',
        'id': 4,
        'legacy': 'UK',
        'mcc': 235,
        'ratingsbody': 'PEGI',
        'slug': 'uk',
        'special': False,
        'weight': 0
    },
    'GRC': {
        'adolescent': True,
        'default_currency': 'EUR',
        'default_language': 'el',
        'id': 17,
        'legacy': 'GR',
        'mcc': 202,
        'ratingsbody': 'PEGI',
        'slug': 'gr',
        'special': False,
        'weight': 0
    },
    'GTM': {
        'adolescent': True,
        'default_currency': 'GTQ',
        'default_language': 'es',
        'id': 25,
        'legacy': 'GT',
        'mcc': 704,
        'ratingsbody': 'ESRB',
        'slug': 'gt',
        'special': False,
        'weight': 0
    },
    'HUN': {
        'adolescent': True,
        'default_currency': 'HUF',
        'default_language': 'hu',
        'id': 13,
        'legacy': 'HU',
        'mcc': 216,
        'ratingsbody': 'PEGI',
        'slug': 'hu',
        'special': False,
        'weight': 0
    },
    'IND': {
        'adolescent': True,
        'default_currency': 'INR',
        'default_language': 'en',
        'id': 32,
        'legacy': 'IN',
        'low_memory': True,
        'mcc': 405,
        'ratingsbody': None,
        'slug': 'in',
        'weight': 0
    },
    'ITA': {
        'adolescent': True,
        'default_currency': 'EUR',
        'default_language': 'it',
        'id': 22,
        'legacy': 'IT',
        'mcc': 222,
        'ratingsbody': 'PEGI',
        'slug': 'it',
        'special': False,
        'weight': 0
    },
    'JPN': {
        'adolescent': True,
        'default_currency': 'JPY',
        'default_language': 'ja',
        'id': 33,
        'legacy': 'JP',
        'mcc': 440,
        'slug': 'jp',
        'special': False,
        'weight': 0
    },
    'MEX': {
        'adolescent': False,
        'default_currency': 'MXN',
        'default_language': 'es',
        'id': 12,
        'legacy': 'MX',
        'mcc': 334,
        'ratingsbody': 'ESRB',
        'slug': 'mx',
        'special': False,
        'weight': 0
    },
    'MNE': {
        'adolescent': True,
        'default_currency': 'EUR',
        'default_language': 'srp',
        'id': 15,
        'legacy': 'ME',
        'mcc': 297,
        'slug': 'me',
        'special': False,
        'weight': 0
    },
    'NIC': {
        'adolescent': True,
        'default_currency': 'NIO',
        'default_language': 'es',
        'id': 29,
        'legacy': 'NI',
        'mcc': 710,
        'ratingsbody': 'ESRB',
        'slug': 'ni',
        'special': False,
        'weight': 0
    },
    'PAN': {
        'adolescent': True,
        'default_currency': 'USD',
        'default_language': 'es',
        'id': 28,
        'legacy': 'PA',
        'mcc': 714,
        'ratingsbody': 'ESRB',
        'slug': 'pa',
        'special': False,
        'weight': 0
    },
    'PER': {
        'adolescent': True,
        'default_currency': 'PEN',
        'default_language': 'es',
        'id': 18,
        'legacy': 'PE',
        'mcc': 716,
        'ratingsbody': 'ESRB',
        'slug': 'pe',
        'special': False,
        'weight': 0
    },
    'POL': {
        'adolescent': True,
        'default_currency': 'PLN',
        'default_language': 'pl',
        'id': 11,
        'legacy': 'PL',
        'mcc': 260,
        'ratingsbody': 'PEGI',
        'slug': 'pl',
        'special': False,
        'weight': 0
    },
    'SLV': {
        'adolescent': True,
        'default_currency': 'USD',
        'default_language': 'es',
        'id': 24,
        'legacy': 'SV',
        'mcc': 706,
        'ratingsbody': 'ESRB',
        'slug': 'sv',
        'special': False,
        'weight': 0
    },
    'SRB': {
        'adolescent': True,
        'default_currency': 'RSD',
        'default_language': 'sr',
        'id': 16,
        'legacy': 'RS',
        'mcc': 220,
        'slug': 'rs',
        'special': False,
        'weight': 0
    },
    'URY': {
        'adolescent': True,
        'default_currency': 'UYU',
        'default_language': 'es',
        'id': 19,
        'legacy': 'UY',
        'mcc': 748,
        'ratingsbody': 'ESRB',
        'slug': 'uy',
        'special': False,
        'weight': 0
    },
    'USD': {
        'adolescent': True,
        'default_currency': 'USD',
        'default_language': 'en-US',
        'id': 2,
        'legacy': 'US',
        'mcc': 310,
        'ratingsbody': 'ESRB',
        'slug': 'us',
        'special': False,
        'weight': 1
    },
    'VEN': {
        'adolescent': True,
        'default_currency': 'USD',
        'default_language': 'es',
        'id': 10,
        'legacy': 'VE',
        'mcc': 734,
        'ratingsbody': 'ESRB',
        'slug': 've',
        'special': False,
        'weight': 0
    },
}
