from ..utils.types import FuelType, ObservationType

# Environment configuration defaults
DEFAULT_NUM_TAXIS = 1
DEFAULT_NUM_PASSENGERS = 1
DEFAULT_DOMAIN_MAP = None
DEFAULT_PICKUP_ONLY = False
DEFAULT_INTERMEDIATE_DROPOFF_REWARD_BY_DISTANCE = False
DEFAULT_DISTINCT_TAXI_INITIAL_LOCATIONS = True
DEFAULT_DISTINCT_PASSENGER_INITIAL_PICKUPS = True
DEFAULT_DISTINCT_PASSENGER_DROPOFFS = True
DEFAULT_ALLOW_COLLIDED_TAXIS_ON_RESET = False
DEFAULT_ALLOW_ARRIVED_PASSENGERS_ON_RESET = False
DEFAULT_CLEAR_DEAD_TAXIS = False

# taxi configuration defaults
DEFAULT_MAX_CAPACITY = float('inf')
DEFAULT_MAX_FUEL = float('inf')
DEFAULT_FUEL_TYPE = FuelType.FUEL
DEFAULT_CAN_STANDBY = False
DEFAULT_HAS_ENGINE_CONTROL = False
DEFAULT_ENGINE_OFF_ON_EMPTY_TANK = False
DEFAULT_CAN_COLLIDE = False
DEFAULT_SPECIFY_PASSENGER_PICKUP = False
DEFAULT_SPECIFY_PASSENGER_DROPOFF = False
DEFAULT_REWARD_TABLE = None
DEFAULT_STOCHASTIC_ACTIONS = None
DEFAULT_OBSERVATION_TYPE = ObservationType.SYMBOLIC
DEFAULT_CAN_SEE_OTHER_TAXI_INFO = False
DEFAULT_FIELD_OF_VIEW = None
