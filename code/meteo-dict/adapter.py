class SpecialAdapter(object):
  
  def __init__(self, legacy_weather, adapted_methods):
        self.legacy_weather = legacy_weather
        self.__dict__.update(adapted_methods)