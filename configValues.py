import argparse
import seedsValues

def parse_arguments():
    parser = argparse.ArgumentParser(description="Simulation Configuration")
    parser.add_argument("--distance_x", type=int, default=2000, help="Distance X")
    parser.add_argument("--b2_location", type=int, default=5000, help="B2 Location")
    parser.add_argument("--end_of_path", type=int, default=3000, help="End of Path")
    parser.add_argument("--report_interval", type=int, default=20, help="Report Interval (ms)")
    parser.add_argument("--ttt", type=int, default=1, help="TTT value")
    parser.add_argument("--alpha", type=int, default=3, help="Alpha value")
    parser.add_argument("--disconnect_threshold", type=int, default=-20, help="Disconnect Threshold")
    parser.add_argument("--initial_phase", type=int, default=5, help="Initial Phase")
    parser.add_argument("--lambda_value", type=int, default=1250, help="Lambda value")
    parser.add_argument("--user_limit", type=int, default=104, help="User Limit")
    parser.add_argument("--constant_speed", type=int, default=55, help="Constant Speed")
    parser.add_argument("--global_id", type=int, default=1, help="Global ID")
    parser.add_argument("--global_time", type=int, default=0, help="Global Time")
    parser.add_argument("--system_time", type=int, default=0, help="System Time")
    parser.add_argument("--average_distance", type=int, default=0, help="Average Distance")
    parser.add_argument("--disconnections", type=int, default=0, help="Disconnections")
    parser.add_argument("--initialization_count", type=int, default=0, help="Initialization Count")
    parser.add_argument("--switch_count", type=int, default=0, help="Switch Count")
    parser.add_argument("--total_distance", type=int, default=0, help="Total Distance")
    parser.add_argument("--seed_set", type=str, default="s1", help="Seed set name (e.g., s1, s2, s3)")

    args = parser.parse_args()
    return args

# Parse arguments and set configuration values
args = parse_arguments()

# Odległości
DISTANCE_X = args.distance_x
B2_LOCATION = args.b2_location
END_OF_PATH = args.end_of_path

# Czas raportowania
REPORT_INTERVAL = args.report_interval  # ms

# Handover
TTT = args.ttt  # ttt=1 to 20ms
ALPHA = args.alpha
DISCONNECT_THRESHOLD = args.disconnect_threshold

# Faza lambda
INITIAL_PHASE = args.initial_phase
LAMBDA = args.lambda_value

# Ograniczenie symulacji
USER_LIMIT = args.user_limit  # +1 ->200

# Stała prędkość
CONSTANT_SPEED = args.constant_speed

# Zmienne pomocnicze
GLOBAL_ID = args.global_id
GLOBAL_TIME = args.global_time
SYSTEM_TIME = args.system_time
AVERAGE_DISTANCE = args.average_distance
DISCONNECTIONS = args.disconnections
INITIALIZATION_COUNT = args.initialization_count
SWITCH_COUNT = args.switch_count
TOTAL_DISTANCE = args.total_distance

# Seeds
SEEDS = seedsValues.get_seeds(args.seed_set)
