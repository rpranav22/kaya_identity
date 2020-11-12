def compute_score(pop, gdp, enInt, carbInt):
    '''

    :param pop: Population
    :param gdp: Gross Domestic Product
    :param enInt: Energy Intensity
    :param carbInt: Carbon Intensity
    :return: CO2 emmissions
    '''
    return pop * gdp * enInt * carbInt